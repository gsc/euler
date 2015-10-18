#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 21: Amicable numbers
(http://projecteuler.net/problem=21).

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

d(a) == b && d(b) == a
sum[a] == sum[sum[a]]

Evaluate the sum of all the amicable numbers under 10000.
"""

def get_proper_divisors(num):
    """
    The proper divisors are the numbers less than num which divide evenly into
    num
    """
    return [i for i in range(1, num) if num % i == 0]

def main():
    """
    Compute all the amicable numbers, storing them on a dictionary without
    duplicates (every couple of amicable numbres is stored only once.
    """

    amicable = {}
    sum_amicable = 0

    for i in range(2, 10000):
        if i in amicable.values():
            continue

        divisors_sum = sum(get_proper_divisors(i))
        if i != divisors_sum and i == sum(get_proper_divisors(divisors_sum)):
            amicable[i] = divisors_sum
            sum_amicable += (i + divisors_sum)

    print "The sum of the amicable numbers is %d " % sum_amicable

if __name__ == "__main__":
    main()
