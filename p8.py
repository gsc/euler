#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 8: Largest product in a series
(http://projecteuler.net/problem=8).

The four adjacent digits in the 1000-digit number that have the greatest product
are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""

def main():
    """
    Solution: split the series in sequences of 13 and compute the product. This
    can be efficiently implemented using map (for casting to int) and reduce
    (for computing the product).
    """

    #Read the series
    f = open("p8-series.txt", "r")

    series = ""

    for line in f:
        series += line.rstrip('\n')

    max_value = 0

    for i in range(0, 1000-12, 1):
        group_value = reduce(lambda x, y: x * y, map(int, series[i:(i+13)]))

        if group_value > max_value:
            max_value = group_value

    print ("The greatest product of 13 adjacent numbers in the sequence is %d  "
           ) % max_value

if __name__ == "__main__":
    main()
