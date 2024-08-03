# Understanding the functions

## after()

```

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

```
List comprehension is a shorter way of writing code. The following line:

```
int(x) for x in date.split('/')

```

Becomes this:

```

result = []
for x in date.split('/'):
    result.append(int(x))

```

The above result = [] list will actually bceome a tuple.

The tuple will be unpacked into day, mon, year.

```

day, mon, year = (int(x) for x in date.split('/'))

```

date.split will create a list from a date: 

19/04/1993 becomes list of strings: ['19', '04', '1993'] 

(['19', '04', '1993']) will be transformed into (19, 4, 1993) -> a touple of int, thanks to int(x)

day, mon, year through tuple unpacking will receive the values in the specifc order