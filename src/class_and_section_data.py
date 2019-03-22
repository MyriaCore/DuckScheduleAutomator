import requests
from copy import deepcopy
import xmltodict as xml
from src.date_util import convert_time, convert_date
import re

def slurp(path):
    """
    Reads a file in as a string, and literally just returns the string.
    :param path: filepath for the file, used by `open`.
    :return: String representing the contents of the file.
    """
    with open(path, "r") as file:
        return file.read()

def spit(path, content):
    """
    Writes a file from a string. Returns None.
    :param path: Filepath for the file, as used by `open`.
    :param content: String representing content to write to file.
    :return: None.
    """
    with open(path, "w") as file:
        file.write(content)



def terms():
    """
    Returns a list of valid term codes.
    """
    rterms = requests.get("https://web.stevens.edu/scheduler/core/core.php?cmd=terms")

    if rterms.status_code == 200:
        return list(map(lambda d: {"code": d["@Code"], "name": d["@Name"]},xml.parse(rterms.text)["Terms"]["Term"]))
    else:
        raise Exception("Request returned invalid status code " + rterms.status_code + ".")

def semester(term_code):
    """
    Returns a dictionary representing a semester, and the courses and sections offered in it.
    :param term_code:
    :return:
    """
    if term_code in list(map(lambda d: d["code"], terms())):
        rsections = requests.get("https://web.stevens.edu/scheduler/core/core.php?cmd=getxml&terms=" + term_code)
        if rsections.status_code == 200:
            data = xml.parse(rsections.text)["Semester"]
            result = {
                "semester": data["@Semester"],
                "courses": int(data["@Courses"]),
                "meetings": int(data["@Meetings"]),
                "requirements": int(data["@Requirements"]),
                "courses":  list(map(lambda d: __clean__(d), data["Course"]))
            }

        else:
            raise Exception("Request returned invalid status code " + rsections.status_code + ".")
    else:
        raise ValueError("The provided term code was invalid. \nExpected one of the following:" +
                         ", ".join(list(map(lambda d: d["code"], terms()))) + "\nReceived: " + term_code)\


def __clean_key__(key):
    """
    Helper function used in clean
    :param key: String, representing a key in a dictionary
    :return: String, representing a cleaned key in a dictionary
    """
    return str(re.sub("([a-z])([A-Z])", lambda m: m.group(1) + "-" + str(m.group(2)).lower(), str(key).replace("@", ""))).lower()


def __clean__(section):
    """
    Takes a list of dictionaries as input and returns a cleaned up version where the values aren't all strings
    """
    # To keep track of keys that have to be handled and not copied over

    unsafe_keys = ["@StartDate", "@EndDate", "@Status", "@CurrentEnrollment", "@MaxEnrollment", "@MinCredit", "@MaxCredit", "Meeting"]
    clean_section = {}

    for key in list(section.keys()):
        if key not in unsafe_keys:
            clean_section[__clean_key__(key)] = deepcopy(section[key])
        elif key in ["@CurrentEnrollment", "@MaxEnrollment", "@MinCredit", "@MaxCredit"]:
            clean_section[__clean_key__(key)] = int(section[key])
        elif key in ["@StartDate", "@EndDate"]:
            clean_section[__clean_key__(key)] = convert_date(section[key])
        elif key == "@Status":
            clean_section["status"] = \
                "Closed" if section["@Status"] == "C" \
                else "open" if section["@Status"] == "O" \
                else "hold" if section["@Status"] == "H" \
                else "cancelled" if section["@Status"] == "X" \
                else "unknown"
        elif key == "Meeting":
            if type(section["Meeting"]) is dict:
                clean_section["meeting"] = __clean_meeting__(section["Meeting"])
            elif type(section["Meeting"]) is list:
                clean_section["meetings"] = list(map(__clean_meeting__, section["Meeting"]))
            else:
                # TODO: ensure this doesnt crash (since the xml uses Ordered Dicts)
                raise Exception("Meeting should either be a dictionary or a list!")

        # For notes on prereqs and coreqs, visit the docs section of `sitsched.md`
        # TODO: use nested lists for dealing with ands and ors.
        #  Example: ["or", ["and", "CS 123", "CS 135"], ["and", "MA 123", "MA 124"]]
        #    This represents that you can have CS 123 and CS 135, or MA 123 and MA 124 to satisfy this condition
        elif key == "prereqs":
            clean_section["prereqs"] = list(map(lambda x: x.strip(), section["prereqs"]
                                                .replace("Prerequisite:", "").replace("<br>", " ").split("or")))
        elif key == "coreqs":
            clean_section["coreqs"] = list(map( lambda x: x.strip(), section["coreqs"]
                                                .replace("Corequisite:", "").replace("<br>", " ")
                                                .replace("--- ", "").split("and")))

    # TODO: find a way to match this to actual human-readable subjects, instead of things like "MA" or "PEP".
    clean_section["subject"] = clean_section["section"].split(" ")[0].strip()
    return clean_section


def __clean_meeting__(meeting):
    """Helper function for __clean__, handles daysTimeLocation key."""
    # TODO: implement and test
    unsafe_keys = ["@Day", "@StartTime", "@EndTime"]
    clean_meeting = {}

    for key in list(meeting.keys()):
        if key not in unsafe_keys:
            clean_meeting[__clean_key__(key)] = deepcopy(meeting[key])
        else:
            # Used for the `day` key.
            weekdays = {
                "M": "Monday",
                "T": "Tuesday",
                "W": "Wednesday",
                "R": "Thursday",
                "F": "Friday",
                "TBA": "TBA"
            }

            # Converts building codes into addresses for the `building` key.
            buildings = {
                "E": "Edwin A. Stevens Hall Hoboken, NJ 07030",
                "B": "Burchard Bldg Hoboken, NJ 07030",
                "BC": "Babbio Center, River Street, Hoboken, NJ 07030",
                "NB": "North Building, Castle Point Terrace, Hoboken, NJ 07030",
                "K": "Kiddie Building, Hoboken, NJ 07030",
                "M": "Morton Building, Hoboken, NJ 07030",
                "P": "607 River St, Hoboken, NJ 07030", # TODO: get google maps to change this shit lmao
                "X": "McLean Hall, Hoboken, NJ 07030",
                "TBA": "TBA"
            }

            clean_meeting["day"] = [weekdays[day_code] for day_code in meeting["@Day"]]

            if (meeting["startTime"] and meeting["endTime"]):
                clean_meeting["startTime"] = convert_time(meeting["startTime"])
                clean_meeting["endTime"] = convert_time(meeting["endTime"])

            # List of `meeting["site"]` vals:
            #   - Castle Point: on-campus class
            #   - WS: web class (no date time info, building will be "OFF" and room will be "WEB")
            #   - LE: idk yet (building will be "OFF" and room will be "CLOSED")
            if meeting["site"] == "Castle Point" and meeting["site"] != "TBA":
                # `room` key is handled before `building` b/c `room` relies on the building
                # code, which would be written over if `building` was handled first.
                clean_meeting["room"] = str(meeting["building"] + " " + meeting["room"])
                clean_meeting["building"] = buildings[meeting["building"]]
            else:
                print("Class not supported yet!")
                # TODO: add some kind of optionality here so it can
                #  still handle web classes and 2nd half-semester MA classes
    return clean_meeting
