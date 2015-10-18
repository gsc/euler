#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 67: Maximum path sum II
(http://projecteuler.net/problem=67).


By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and 'Save
Link/Target As...'), a 15K text file containing a triangle with one-hundred
rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve
it. ;o)
"""

def is_valid_point(pyramid, x, y):
    """
    Verifies that a point coordinates (x,y) belong into the pyramid.
    """
    return x < len(pyramid) and y < len(pyramid)

def find_max_path(pyramid, paths, x, y):
    """
    The largest path from any given point can be computed recursively, by
    computing the path value for each leaf.
    """

    if is_valid_point(pyramid, x + 1, y):
        try:
            left_path = paths[x + 1][y]
        except:
            left_path, paths = find_max_path(pyramid, paths, x + 1, y)
    else:
        left_path = 0

    if is_valid_point(pyramid, x + 1, y + 1):
        try:
            right_path = paths[x+1][y + 1]
        except:
            right_path, paths = find_max_path(pyramid, paths, x + 1, y + 1)
    else:
        right_path = 0

    if right_path > left_path:
        max_path = pyramid[x][y] + right_path
    else:
        max_path = pyramid[x][y] + left_path

    paths[x][y] = max_path

    return max_path, paths

def main():
    """
    Computes the values of all the possible paths from the top, and select the
    largest one. This is the same approach as in problem 18, but caching the
    paths, to deal with a bigger pyramid.
    """

    #Read the pyramid from the csv file
    f = open("triangle.txt", "r")

    pyramid = []

    for line in f:
        row = map(int, line.split(" "))
        pyramid.append(row)


    paths = [[None for _ in range(0, i+1)] for i in range(0, len(pyramid))]

    max_path, paths = find_max_path(pyramid, paths, 0, 0)
    print "The max path in the pyramid has a size of %d " % max_path

if __name__ == "__main__":
    main()
