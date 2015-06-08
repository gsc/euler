#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 3: Largest Prime factor
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def compute_prime_factors(num, floor=1):
    """
    Computes the prime factor of a number by brute force.
    Two small optimizations: only checks the odd factors (even are never prime,
    except for 2), and floor is the lowest possible prime (so it doesn't start
    counting on 3 on each call.
    """

    if num % 2 == 0:
        return [2] + compute_prime_factors(num / 2, 3)

    if floor % 2 == 0:
        # All the possible prime factors are odd, so the search will start in
        # the next one
        floor += 1

    while floor < num:
        floor += 2
        if num % floor == 0:
            return [floor] + compute_prime_factors(num / floor, floor)

    return [1]

if __name__ == "__main__":
    NUM = 600851475143
    FACTORS = compute_prime_factors(NUM, 1)

    print "The largest prime factor of %d is %d " % (NUM, max(FACTORS))
