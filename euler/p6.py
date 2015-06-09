#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 6: Sum square difference
(http://projecteuler.net/problem=6).

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
     (1 + 2 + ... + 10)^2 = 552 = 3025

 Hence the difference between the sum of the squares of the first ten natural
 numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def main():
    sum_of_squares = reduce(lambda x, y: x + y**2, [x for x in range(1, 101)])
    square_of_sums = sum([x for x in range(1, 101)])**2

    print ("The difference between the sum of the squares (%d) and the square "
           "of the sums (%d) of the first 100 natural numbers is %d "
        ) % (square_of_sums, sum_of_squares, square_of_sums - sum_of_squares)

if __name__ == "__main__":
    main()
