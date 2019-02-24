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

    unsafe_keys = ["maxEnrollment", "currentEnrollment", "daysTimeLocation"]

    clean_section = {}

    for key in list(section.keys()):
        if key not in unsafe_keys:
            clean_section[key] = deepcopy(section[key])
        else:
            clean_section["maxEnrollment"] = int(section["maxEnrollment"])
            clean_section["currentEnrollment"] = int(section["currentEnrollment"])

            if type(section["daysTimeLocation"]) is dict:
                clean_section["daysTimeLocation"] = __clean_days_time_location__(section["daysTimeLocation"])
            elif type(section["daysTimeLocation"]) is list:
                clean_section["daysTimeLocation"] = map(__clean_days_time_location__, section["daysTimeLocation"])
            else:
                pass #TODO: implement

    return clean_section

def __clean_days_time_location__(days_time_location):
    """Helper function for __clean__, handles daysTimeLocation key."""

    # Weekdays are the same enumerations that date.weekday() uses
    # date.weekday() docs: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
    # Used for the `day` key.
    weekdays = {
        "M": 0,
        "T": 1,
        "W": 2,
        "R": 3,
        "F": 4,
    }

    # Converts building codes into addresses for the `building` key.
    buildings = {
        "E": "Edwin A. Stevens Hall Hoboken, NJ 07030",
        "B": "Burchard Bldg Hoboken, NJ 07030",
        "BC": "Babbio Center, River Street, Hoboken, NJ 07030",
        "NB": "North Building, Castle Point Terrace, Hoboken, NJ 07030",
        "K": "607 River St, Hoboken, NJ 07030",
        "M": "607 River St, Hoboken, NJ 07030",
        "P": "607 River St, Hoboken, NJ 07030",
        "X": "McLean Hall, Hoboken, NJ 07030"
    }

    clean_dtl = {}

    clean_dtl["day"] = weekdays[days_time_location["day"]]
    clean_dtl["startDate"] = None # TODO: implement
    clean_dtl["endDate"] = None # TODO: implement

    clean_dtl["startTime"] = convert_time(days_time_location["startTime"])
    clean_dtl["endTime"] = convert_time(days_time_location["endTime"])

    # `room` key is handled before `building` b/c `room` relies on the building
    # code, which would be written over if `building` was handled first.
    clean_dtl["room"] = str(days_time_location["building"] + " " + days_time_location["room"])
    clean_dtl["building"] = buildings[days_time_location["building"]]

    return clean_dtl
