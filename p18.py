#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 18: Maximum path sum I
(http://projecteuler.net/problem=18).

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""

def is_valid_point(pyramid, x, y):
    """
    Verifies that a point coordinates (x,y) belong into the pyramid.
    """
    return x < len(pyramid) and y < len(pyramid)

def find_max_path(pyramid, x, y):
    """
    The largest path from any given point can be computed recursively, by
    computing the path value for each leaf (without prunning).
    """
    if is_valid_point(pyramid, x + 1, y):
        left_path = find_max_path(pyramid, x + 1, y)
    else:
        left_path = 0

    if is_valid_point(pyramid, x + 1, y + 1):
        right_path = find_max_path(pyramid, x + 1, y + 1)
    else:
        right_path = 0

    if right_path > left_path:
        return pyramid[x][y] + right_path
    else:
        return pyramid[x][y] + left_path

def main():
    """
    Computes the values of all the possible paths from the top, and select the
    largest one.
    """

    #Read the pyramid from the csv file
    f = open("p18-pyramid.csv", "r")

    pyramid = []

    for line in f:
        row = map(int, line.split(","))
        pyramid.append(row)

    max_path = find_max_path(pyramid, 0, 0)
    print "The max path in the pyramid has a size of %d " % max_path

if __name__ == "__main__":
    main()
