#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 10: Summation of primes
(http://projecteuler.net/problem=10).

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import euler

def main():
    """
    Compute the list of all primes below 2 millions using the erathostenes sieve
    and add it up.
    """
    primes = euler.eratosthenes_sieve(2000000)
    print "The sum of all primes below 2 million is %d " % sum(primes)

if __name__ == "__main__":
    main()
