#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 22: Names scores (http://projecteuler.net/problem=22).

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

import string

def get_name_value(name):
    """
    The alphabetical value of a name, is the sume of the alphabetical positions
    of each letter.
    """
    return sum(map(lambda x: string.uppercase.index(x) + 1, name))

def main():
    """
    1. Read the names from the text file into a names list (sorted and trimmed).
    2. Compute the name value for each name
    3. Aggregate the name values * position in the file.
    """

    names = []

    with open('names.txt', 'r') as f:
        names = f.read().split(',')
        names = sorted(map(lambda x: str.replace(x, "\"", ''), names))

    sum_name_values = 0

    for i, name in enumerate(names):
        sum_name_values += (i+1) * get_name_value(name)

    print "The sum of the name values is %d " % sum_name_values

if __name__ == "__main__":
    main()
