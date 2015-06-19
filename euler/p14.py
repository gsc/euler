#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 14: Longest Collatz sequence
http://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n  -> n/2 (n is even)
n  -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.


Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

def main():
    """
    Brute force. Even though the sequence would have repetitions over time, it's
    more efficient like this than trying to manually cache (sub)sequences.
    """

    max_length = 0

    start = time.time()

    for num in range(1, 1000000):
        sequence_length = 0
        next_number = num

        while next_number > 1:
            if next_number % 2 == 0:
                next_number = next_number / 2
            else:
                next_number = 3 * next_number + 1

            sequence_length += 1

        if sequence_length > max_length:
            max_length = sequence_length
            max_factor = num

    end = time.time()
    print ("The longest collatz sequence below 1 million is generated by %d"
            " (length: %d, time: %f)") % (max_factor, max_length, end -start)

if __name__ == "__main__":
    main()
