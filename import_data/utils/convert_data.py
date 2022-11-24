from datetime import date, time


def convert_date(string):
    year = string[0:4]
    month = string[4:6]
    day = string[6:8]

    return f"{month}/{day}/{year}"


def convert_hour(string):
    hour = string[0:2]
    min = string[2:4]
    sec = string[4:6]

    return f"{hour}:{min}:{sec}"
