#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 25: 1000-digit Fibonacci number (https://projecteuler.net/problem=25)

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""

def fibonacci(num):
    """
    Fibonacci function, with memoization.
    """

    if num in cache.keys():
        return cache[num]

    if num == 1:
        return 1
    if num == 2:
        return 2
    else:
        term1 = fibonacci(num-1)
        term2 = fibonacci(num-2)
        cache[num] = term1 + term2

        return cache[num]

cache = {}

def main():
    """
    Solution: Brute force fibonnaci generation, with memoization.
    """

    seq_found = False
    i = 0

    while not seq_found:
        i += 1
        term = fibonacci(i)
        seq_found = len(str(term)) == 1000

    if seq_found:
        print ("The first term in the Fibonacci seq with 1000 digits is the %d "
                "-th term") %  (i + 1)

if __name__ == "__main__":
    main()
