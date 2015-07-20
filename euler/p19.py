#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 19: Counting Sundays
(http://projecteuler.net/problem=19).

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
"""

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
          11: 30, 12: 31}

def is_leap_year(year):
    if year % 100 == 0:
        return (year % 400 == 0)
    else:
        return (year % 4 == 0)

def get_month_days(month, year):
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return months[month]

def get_mondays():
    day = 1
    month = 1
    year = 1900

    days_of_month = get_month_days(month, year)

    count = 0

    while year < 2001:
        day += 7
        if day > days_of_month:
            month += 1
            day = day - days_of_month

            if month > 12:
                month = 1
                year += 1

            days_of_month = get_month_days(month, year)

        if day == 1:
            count += 1

    return count

def main():
    res = get_mondays()
    print "There was %d mondays between 1900 and 2000" % res

if __name__ == "__main__":
    main()
