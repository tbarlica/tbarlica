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

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # leap year check
        return True
    return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year): # check if leap year to determine max days in Feb
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    if day > mon_max(mon, year):
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    if day == 0:
        mon -= 1
        if mon == 0:
            year -= 1
            mon = 12
        day = mon_max(mon, year)  # if tmp_day = 0, reset to last month's max
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    try:
        day, month, year = (int(x) for x in date.split('/'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    i = 0 # counter will increment or decrement to num
    if num > 0:
        while i < num:
            start_date = after(start_date)
            i += 1
    else:
        while i > num:
            start_date = before(start_date)
            i -= 1
    return start_date

if __name__ == "__main__":
    # check length of arguments
    if len(sys.argv) != 3:
        usage()
    # check first arg is a valid date
    # check that second arg is a valid number (+/-)
    # call day_iter function to get end date, save to x
    # print(f'The end date is {day_of_week(x)}, {x}.')
    pass