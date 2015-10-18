#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 16: Power digit sum (http://projecteuler.net/problem=16).
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def main():
    """
    The sum can be solved efficiently using map.
    """

    res = sum(map(int, list(str(2**1000))))

    print "The sum of the digits of the number 2^1000 is %d " % res

if __name__ == "__main__":
    main()

