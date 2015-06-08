#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 1 Multiples of 3 and 5
http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from sets import Set

def multiples(num, roof):
    """
    Computes the multiples of a number (below a certain roof).

    Args:
        num: the number which multiples are to be computed.
        roof: determines the largest possible multiple to be computed.
    """
    return [factor * num for factor in range(1, roof) if factor * num < roof]

if __name__ == "__main__":

    NUM1, NUM2 = 3, 5
    ROOF = 1000

    COMMON_MULTIPLES = Set(multiples(NUM1, ROOF) + multiples(NUM2, ROOF))

    print ("The sum of the natural numbers below %d that are multiple of %d or "
            "%d below 1000 is %d") % (ROOF, NUM1, NUM2, sum(COMMON_MULTIPLES))

