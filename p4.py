#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 4: Largest palindrome product
(http://projecteuler.net/problem=4).

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    """
    Determines if a number is a palindrome.
    """
    str_num = str(num)

    if len(str_num) == 1:
        return True
    elif len(str_num) == 2:
        return str_num[0] == str_num[1]

    if str_num[0] == str_num[len(str_num)-1]:
        return  is_palindrome(str_num[1:len(str_num)-1])
    else:
        return False

def main():
    """
    Computes the largest palindrome of two 3-digit numbers by brute force.
    """
    largest = 0
    for i in range(100, 999):
        for j in range(100, 999):
            if i * j > largest and is_palindrome(i * j):
                largest = i * j

    print "The largest palindrome product of two 3-digits nums is %d " % largest

if __name__ == "__main__":
    main()

