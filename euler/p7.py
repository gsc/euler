#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 7: 10001st prime (http://projecteuler.net/problem=7).

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.


What is the 10001st prime number?
"""
import euler

def main():
    
    primes = [1, 2, 3]
    last_prime = 3

    while len(primes) < 10002:
        last_prime += 2
        if euler.is_prime(last_prime):
            primes.append(last_prime)

    print "The 10.001st prime is %d " % last_prime

if __name__ == "__main__":
    main()
