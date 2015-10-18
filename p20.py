#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 20: Factorial digital sum
(http://projecteuler.net/problem=20).

n! means n x (n  1) x  ...  3 x 2 x 1

For example, 10! = 10 x  9  ...  3  x  2  x  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(num):
    """
    The factorial can be expressed as a reduce over the list of terms.
    """
    return reduce(lambda x, y: x*y, [x for x in reversed(range(1, num + 1))])

def sum_terms(num):
    """
    Split the number into a list of terms, and aggregate them.
    """
    return sum(map(int, str(num)))

def main():

    print "The sum of the terms of 100! is %d" % sum_terms(factorial(100))

if __name__ == "__main__":
    main()
