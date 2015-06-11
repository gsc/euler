#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 10: Summation of primes
(http://projecteuler.net/problem=10).

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from sets import Set

def is_prime(num):
    """
    Determines whether a number is a prime
    """
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

def sieve(top):
    """
    Eratosthenes sieve: after verifying that a number is a prime, mark all its
    factors as non primes.
    """

    not_primes = Set([])
    primes = []

    for num in range(2, top+1):
        if num % 10000 == 0:
            print "Verifying: %d first numbers" % num

        if num not in not_primes and is_prime(num):

            primes.append(num)

            for i in range(2, top / num +1):
                not_primes.add(i*num)

    return primes

def main():
    """
    Compute the list of all primes below 2 millions using the erathostenes sieve
    and add it up.
    """
    primes = sieve(2000000)
    print "The sum of all primes below 2 million is %d " % sum(primes)

if __name__ == "__main__":
    main()
