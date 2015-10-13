#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler,problem 23: Non-abundant sums (http://projecteuler.net/problem=23)
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

def get_proper_divisors(num):
    return [i for i in xrange(1, num) if num % i == 0]

def is_abundant(num):
    return sum(get_proper_divisors(num)) > num

def main():
    abundant = [i for i in range(12, 28113) if is_abundant(i)]

    res = 0

    for num in xrange(1, 28124):
        print "Can %d num can be expressed as the sum of two abundants? " % num
        is_sum = False

        for i in abundant:
            if num - i in abundant:
                is_sum = True
                break

        if not is_sum:
            res += num

    print ("The sum of all the positive integers that cannot be written as two"
            "abundant numbers is %d") % res

    return res

if __name__ == "__main__":
    main()
