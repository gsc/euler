#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 5: smallest multiple
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def is_prime(num):
    """
    Determines whether a number is a prime
    """
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def get_factors(num):
    """
    Return the prime factors of a number.
    """
    res = []
    for factor in range(1, num+1):
        if num % factor == 0:
            if is_prime(factor):
                res.append(factor)
            elif num != factor:
                res = get_factors(factor)
    return res

def main():
    """
    Compute the smallest positive number  evenly divisible by all of the
    numbers from 1 to 20 by brute force.
    """

    primes = [x for x in range(1, 21) if is_prime(x)]

    target = reduce(lambda x, y: x*y, primes)

    for i in range(1, 21):
        rest = target % i
        if rest != 0:
            if is_prime(rest):
                target = target * rest
            else:
                factors = get_factors(rest)
                for factor in factors:
                    target = target * factor

    print "The smallest number divisible by the first 20 is %d " % target

if __name__ == "__main__":
    main()
