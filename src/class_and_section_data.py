import requests
from copy import deepcopy
from src.date_util import convert_time

def terms():
    """
    Returns a list of valid term codes.
    """
    rterms = requests.get('https://stevens-scheduler.cfapps.io/p/terms')

    if rterms.status_code == 200:
        return list(rterms.json())
    else:
        raise Exception('Request returned invalid status code ' + rterms.status_code + '.')

def term_sections(term):
    """
    Takes in a string `term` representing a valid termcode (2019S for example)
    and returns a list of maps representing all of the classes available in
    that term.
    NOTE: atm all values are strings.
    """
    if term in terms():
        rsections = requests.get('https://stevens-scheduler.cfapps.io/p/' + term)
        if rsections.status_code == 200:
            return map(__clean__, list(rsections.json()))
        else:
            raise Exception('Request returned invalid status code ' + rsections.status_code + '.')
    else:
        raise Exception(term + ' is not a valid term code!')


def __clean__(section):
    """
    Takes a list of dictionaries as input and returns a cleaned up version where the values aren't all strings
    """
    # To keep track of keys that have to be handled and not copied over
    unsafe_keys = ["maxEnrollment", "currentEnrollment", "daysTimeLocation", "prereqs", "coreqs", "status"]
    clean_section = {}

    for key in list(section.keys()):
        if key not in unsafe_keys:
            clean_section[key] = deepcopy(section[key])
        elif key == "maxEnrollment":
            clean_section["maxEnrollment"] = int(section["maxEnrollment"])
        elif key == "currentEnrollment":
            clean_section["currentEnrollment"] = int(section["currentEnrollment"])
        elif key == "status":
            clean_section["status"] = "Closed" if section["status"] == "C" \
                else "Open" if section["status"] == "O" else "Unknown"

        elif key == "daysTimeLocation":
            if type(section["daysTimeLocation"]) is dict:
                clean_section["daysTimeLocation"] = __clean_days_time_location__(section["daysTimeLocation"])
            elif type(section["daysTimeLocation"]) is list:
                clean_section["daysTimeLocation"] = list(map(__clean_days_time_location__, section["daysTimeLocation"]))
            else:
                raise Exception("daysTimeLocation should either be a dictionary or a list!")

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


def __clean_days_time_location__(days_time_location):
    """Helper function for __clean__, handles daysTimeLocation key."""
    unsafe_keys = ["day", "room", "building"]
    clean_dtl = {}

    for key in list(days_time_location.keys()):
        if key not in unsafe_keys:
            clean_dtl[key] = deepcopy(days_time_location[key])
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

            clean_dtl["day"] = [weekdays[day_code] for day_code in days_time_location["day"]]

            if (days_time_location["startTime"] and days_time_location["endTime"]):
                clean_dtl["startTime"] = convert_time(days_time_location["startTime"])
                clean_dtl["endTime"] = convert_time(days_time_location["endTime"])

            # List of `days_time_location["site"]` vals:
            #   - Castle Point: on-campus class
            #   - WS: web class (no date time info, building will be "OFF" and room will be "WEB")
            #   - LE: idk yet (building will be "OFF" and room will be "CLOSED")
            if days_time_location["site"] == "Castle Point" and days_time_location["site"] != "TBA":
                # `room` key is handled before `building` b/c `room` relies on the building
                # code, which would be written over if `building` was handled first.
                clean_dtl["room"] = str(days_time_location["building"] + " " + days_time_location["room"])
                clean_dtl["building"] = buildings[days_time_location["building"]]
            else:
                print("Class not supported yet!")
                # TODO: add some kind of optionality here so it can
                #  still handle web classes and 2nd half-semester MA classes
    return clean_dtl
