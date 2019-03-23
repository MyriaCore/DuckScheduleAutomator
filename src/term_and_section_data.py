import requests
from copy import deepcopy
import xmltodict as xml
from src.date_util import convert_time, convert_date
import re
import random
from collections import OrderedDict

def __clean_key__(key):
    """
    Helper function used in clean
    :param key: String, representing a key in a dictionary
    :return: String, representing a cleaned key in a dictionary
    """
    return str(re.sub("([a-z])([A-Z1-9])", lambda m: m.group(1) + "_" + str(m.group(2)).lower(), str(key).replace("@", ""))).lower()


def __clean__(section):
    """
    Private helper function used by `sections`. Goes through an individual dictionary describing a section and
    makes sure the data types, structures, etc described by the raw dictionary are correct and properly pythonic.
    """
    unsafe_keys = ["Requirement", "@StartDate", "@EndDate", "@Status", "@CurrentEnrollment", "@MaxEnrollment", "@MinCredit", "@MaxCredit", "Meeting"]
    clean_section = {}

    for key in list(section.keys()):
        if key not in unsafe_keys:
            clean_section[__clean_key__(key)] = deepcopy(section[key])
        if key in ["@CurrentEnrollment", "@MaxEnrollment", "@MinCredit", "@MaxCredit"]:
            clean_section[__clean_key__(key)] = int(section[key])
        if key == "@StartDate":
            clean_section["date_span"] = (convert_date(section["@StartDate"]), convert_date(section["@EndDate"]))
        if key == "@Status":
            clean_section["status"] = \
                "Closed" if section[key] == "C" \
                else "open" if section[key] == "O" \
                else "hold" if section[key] == "H" \
                else "cancelled" if section[key] == "X" \
                else "unknown"
        if key == "Meeting":
            if type(section[key]) is dict or type(section[key]) is OrderedDict:
                clean_section["meetings"] = [__clean_meeting__(section[key])]
            elif type(section[key]) is list:
                clean_section["meetings"] = list(map(__clean_meeting__, section[key]))
            else:
                raise Exception("Meetings should either be a dictionary or a list!\nReceived: " + str(type(section[key])))
        if key == "Requirement":
            if type(section[key]) is dict or type(section[key]) is OrderedDict:
                clean_section["requirements"] = [__clean_requirements__(section[key])]
            elif type(section[key]) is list:
                clean_section["requirements"] = list(map(__clean_requirements__, section[key]))
            else:
                raise Exception("Requirements should either be a dictionary or a list!\nReceived: " + str(type(section[key])))

    return clean_section


def __clean_requirements__(requirement):
    """
    Helper function used in __clean__, handles `@Requirement` key.
    """
    control_codes = {
        "(BLANK)": "",
        "CC": "Course corequisite required",
        "CS": "Section corequisite required",
        "CA": "Activity corequisite required",
        "RQ": "Prerequisite course required",
        "R&": "(cont.) Prerequisite course reqd",
        "RQM": "Prereq course reqd w/ min grade",
        "RM&": "(cont.) Prereq reqd w/ min grade",
        "RQT": "Prerequisite test required",
        "RT&": "(cont.) Prerequisite test required",
        "NQ": "Concurrent Prereq course required",
        "N&": "(cont.) Concur Prereq course reqd",
        "NQM": "Concur Prereq reqd w/ min grade",
        "NM&": "(cont.) Concur Prereq w/ min grade",
        "MB": "By Application Only",
        "MP": "Prerequisite Required",
        "MC": "Corequisite Required",
        "ML": "Lab Fee Required",
        "MA": "Permission of Advisor Required",
        "MI": "Permission of Instructor Required",
        "MH": "Department Head Approval Required",
        "MN": "No Credit Course for Departmental Majors",
        "MS": "Studio course; No general Humanities credit",
        "MW": "Women Only",
        "PAU": "Auditors need instructor permission",
        "PCG": "Permission needed from Continuing ED",
        "PDP": "Permission needed from department",
        "PIN": "Permission needed from instructor",
        "PUN": "Undergrads need instructor permission",
        "PUA": "UGs need permission of Dean of UG Academics"
    }
    return {
        "description": control_codes[requirement["@Control"]] + ": " + requirement["@Value1"]
            + (", " + requirement["@Value2"] if requirement["@Value2"] != "" else ""),
        "code_list": list(filter(lambda s: s != "",
            [requirement["@Control"], requirement["@Value1"], requirement["@Value2"]])),
    }

def __clean_meeting__(meeting):
    """
    Private helper function used by `__clean__`, handles `@Meeting` key.
    """
    unsafe_keys = ["@Day", "@StartTime", "@EndTime"]
    clean_meeting = {}

    for key in list(meeting.keys()):
        if key not in unsafe_keys:
            clean_meeting[__clean_key__(key)] = deepcopy(meeting[key])
        else:
            weekdays = {
                "M": "monday",
                "T": "tuesday",
                "W": "wednesday",
                "R": "thursday",
                "F": "friday",
                "TBA": "tba"
            }
            if key == "@Day":
                clean_meeting["day"] = [weekdays[day_code] for day_code in meeting[key]]
            if key == "@StartTime":
                clean_meeting["time_span"] = (convert_time(meeting["@StartTime"]), convert_time(meeting["@EndTime"]))

    return clean_meeting


def terms():
    """
    Returns a list of python dictionaries representing valid terms to query.
    The two valid keys in each dictionary are `"code"`, which is the term code described,
    and `"description"`, which is a short description of what the term is.
    :return: (list of dict's) A list of terms the server knows about
    """
    rterms = requests.get("https://web.stevens.edu/scheduler/core/core.php?cmd=terms")

    if rterms.status_code == 200:
        return list(map(lambda d: {"code": d["@Code"], "description": d["@Name"]},xml.parse(rterms.text)["Terms"]["Term"]))
    else:
        raise Exception("Request returned invalid status code " + rterms.status_code + ".")

def sections(term_code):
    """
    Returns a python dictionary representing the course sections available in a term.
    See docs/home.md for details about possible keys and values the dictionaries can have.
    :param term_code:
    :return:
    """
    if term_code in list(map(lambda d: d["code"], terms())):
        rsections = requests.get("https://web.stevens.edu/scheduler/core/core.php?cmd=getxml&terms=" + term_code)
        if rsections.status_code == 200:
            data = xml.parse(rsections.text)["Semester"]
            return {
                "semester": data["@Semester"], # semester code, like 2019F
                "courses":  list(map(lambda d: __clean__(d), data["Course"]))
            }
        else:
            raise Exception("Request returned invalid status code " + rsections.status_code + ".")
    else:
        raise ValueError("The provided term code was invalid. \nExpected one of the following:" +
                         ", ".join(list(map(lambda d: d["code"], terms()))) + "\nReceived: " + term_code)

def test():
    with open("data/2019F.xml", "r") as f:
        myxml = xml.parse(f.read())["Semester"]
        f.close()
    ex_class = dict(random.choice(list(filter(lambda x: "CS 284A" in x["@Section"], myxml["Course"]))))
    return __clean__(ex_class)

