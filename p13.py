#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 13: Large Sum (http://projecteuler.net/problem=13).
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.
"""

def main():
    """
    As 50-digit numbers aren't supported, implement the manual addition.
    """
    #Read the series
    f = open("p13-number.txt", "r")

    number = {}

    for i, line in enumerate(f):
        number[i] = map(int, line.rstrip('\n'))

    sum_col = {}
    for i in range(0, 50):
        sum_col[i] = sum([number[j][i] for j in range(0, len(number))])

    carry = 0
    res = {}
    for i in reversed(range(1, 50)):
        rest = sum_col[i] + carry
        res[i] = rest % 10
        carry = rest / 10

    res[0] = sum_col[0] + carry

    first_ten_digits = "".join(map(str, res.values()))[0:10]
    print "The first 10 digits of the sum are " + first_ten_digits

if __name__ == "__main__":
    main()
