import requests
from copy import deepcopy

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
            # TODO: filter through this to make sure data types are as they should be (numbers are numbers, dates are dates, etc.)
            return map(__clean__, list(rsections.json()))
        else:
            raise Exception('Request returned invalid status code ' + rsections.status_code + '.')
    else:
        raise Exception(term + ' is not a valid term code!')


def __clean__(section):
    """
    Takes a list of dictionaries as input and returns a cleaned up version where the values aren't all strings
    """
    weekdays = {
        "M": 0,
        "T": 1,
        "W": 2,
        "R": 3,
        "F": 4,
    }

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

    clean_section = deepcopy(section) # TODO: find a way to selectively copy key val pairs that can stay as strings
    clean_section["maxEnrollment"] = int(section["maxEnrollment"])
    clean_section["currentEnrollment"] = int(section["currentEnrollment"])
    # TODO: Find a way to add a "roomloc" key that just has like "NB 102" as a val
    # TODO: make sure we handle this if it's a list of daytimelocations

    clean_section["daysTimeLocation"]["day"] = weekdays[section["daysTimeLocation"]["day"]]

    return clean_section



# TODO: function to read in all data as `DuckSchedule` objects.


