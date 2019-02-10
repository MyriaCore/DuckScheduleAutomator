from datetime import datetime



def convert_date(time):
    """
    `time` is a timestamp string ending in Z (Ex: '11:50:00Z')
    """

    return datetime.strptime(time, '%H:%M:%S' + 'Z').time()


def get_hour(time):
    """
    `time` is a timestamp string ending in Z (Ex: '11:50:00Z')
    """

    return datetime.strptime(time, '%H:%M:%S' + 'Z').hour

def get_minutes(time):
    """
    `time` is a timestamp string ending in Z (Ex: '11:50:00Z')
    """

    return datetime.strptime(time, '%H:%M:%S' + 'Z').minute





