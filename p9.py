#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 9: Special pythagorean triplet
(http://projecteuler.net/problem=9).

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    """
    Solution: try by brute force all the possible combinations.
    """
    for a in range(1, 500):
        for b in range(2, 500):
            for c in range(3, 500):
                if is_pythagorean_triplet(a, b, c) and verifies_equation(a, b, c):
                    print ("Is (%d, %d, %d) is a pythagorean triple that "
                            "verifies a + b + c = 1000") %  (a, b, c)
                    print "And its product is %d" % (a*b*c)
                    return

def is_pythagorean_triplet(a, b, c):
    """
    A Pythagorean triplet is a set of three natural numbers,
    (a < b < c), for which:

        a^2 + b^2 = c^2
    """
    return a**2 + b**2 == c**2

def verifies_equation(a, b, c):
    """
    Returns true if the passed values verify the equation:
        a  + b + c = 1000
    """
    return a + b + c == 1000

if __name__ == "__main__":
    main()

