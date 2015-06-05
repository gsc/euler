#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler, problem 1 Multiples of 3 and 5
# http://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def calc_multiples(x, y, roof):
    num_multiples = 2
    acum = 0
    multiples = []
    while True:
        #Multiples from x, and x only.
        # (i.e. excluding those that are also multiples of x).
        if num_multiples % y != 0 and x * num_multiples < roof:
            print x*num_multiples
            acum += (x*num_multiples)
            multiples.append(x*num_multiples)

        if x * num_multiples > roof:
            break
        else:
            num_multiples += 1

    num_multiples = 2
    while True:
        #Multiples from y, and y only (i.e. excluding those that are
        # also multiples of x).
        if num_multiples % x != 0 and y * num_multiples < roof:
            print y*num_multiples
            acum += y*num_multiples
            multiples.append(y*num_multiples)
        if y * num_multiples > roof:
            break
        else:
            num_multiples += 1
    a = 1
    b = 1
    # True => inc a, False => inc b

    # Multiples of x and y.
    while True:
        b = a
        while True:
            if a * x * b * y < roof:
                if not a * x * b *y in multiples:
                    multiples.append(a*x*b*y)
                    print a*x*b*y
                    acum += a * x* b*y
                b += 1
            else:
                break
        a += 1
        if a >= (roof - y) / x:
            break

    # 8 (3+5) is added, to include the 'base' factors in the sum.
    return acum + 8

if __name__ == "__main__":

    X = 3
    Y = 5

    #threshold, only multiples below 'roof' are to be summed up.
    ROOF = 1000

    calc_multiples(X, Y, ROOF)
