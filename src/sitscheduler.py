import requests

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
            return list(rsections.json())
        else:
            raise Exception('Request returned invalid status code ' + rsections.status_code + '.')
    else:
        raise Exception(term + ' is not a valid term code!')
