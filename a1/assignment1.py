#!/usr/bin/env python3

'''
Author: Traian Barlica
Description: OPS445 Assignment 1 Version C - Summer 2024
Program: assignment1.py 
The python code in this file is original work written by
Traian Barlica. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: 
-This program takes a date in the format DD/MM/YYYY and returns the date after or before a given number of days.
-The program also returns the day of the week for a given date.
-The program checks for leap years and validates the date input.
'''

import sys

def parse_date(date: str):
    """
    Parses a date string in DD/MM/YYYY format into day, month, and year integers.
    Additional function in assignment1 for code refactoring
    Function takes a date string in DD/MM/YYYY format and returns a tuple of day, month, and year as integers
    """
    day, month, year = (int(x) for x in date.split('/'))
    return day, month, year

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = parse_date(date)
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    '''
    leap day occur in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400
    return true if the year is a leap year
    '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # leap year check
        return True
    return False

def mon_max(month:int, year:int) -> int:
    '''
    mon_max() -> int
    returns the days in a month for a given month
    calls leap_year check when month is February and adjusts days accordingly
    '''
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year): # check if leap year to determine max days in Feb
        return 29 # change Feb to 29 days
    else:
        return mon_dict[month] # return days in month

def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format
    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    Calls mon_max() to determine the max days in a month

    The function will increment the day by 1, if the day is greater than the max days in the month, 
    it will increment the month by 1 and reset the day to 1 
    and if the month is 12, it will increment the year by 1
    '''
    day, mon, year = parse_date(date)
    day += 1  # next day increment

    if day > mon_max(mon, year): # check to see if month needs to be incremented
        mon += 1
        if mon > 12: # check to see if year needs to be incremented
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    '''
    Returns previous day's date as DD/MM/YYYY
    Calls mon_max() to determine the max days in a month

    The function will decrement the day by 1, if the day is less than 1,
    it will decrement the month by 1 and reset the day to the max days in the previous month,
    if the month is 1, it will decrement the year by 1 and set the month to 12
    '''
    day, mon, year = parse_date(date)
    day -= 1  # previous day decrement

    if day == 0: # check to see if month needs to be decremented
        mon -= 1
        if mon == 0: # check to see if year needs to be decremented
            year -= 1
            mon = 12
        day = mon_max(mon, year)  # if tmp_day = 0, reset to last month's max
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user if the arguments are invalid"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    try:
        day, month, year = parse_date(date)
        if month < 1 or month > 12: # check month range 1-12
            return False
        if day < 1 or day > mon_max(month, year): # check day range 1-max days in month
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    i = 0 # counter will increment or decrement to num
    if num > 0: # check if num is positive or negative to determine if we increment or decrement
        while i < num:
            start_date = after(start_date)
            i += 1
    else:
        while i > num:
            start_date = before(start_date)
            i -= 1
    return start_date

if __name__ == "__main__":
    # check number of arguments
    if len(sys.argv) != 3:
        usage()
    # check first arg is a valid date (DD/MM/YYYY)
    if not valid_date(sys.argv[1]):
        usage()
    # check that second arg is a valid number (+/-) and assign to num
    try:
        num = int(sys.argv[2])
    except ValueError:
        usage()
    # call day_iter function to get end date, save to x, and print day of week
    x = day_iter(sys.argv[1], num)
    print(f'The end date is {day_of_week(x)}, {x}.')