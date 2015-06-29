#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 15: Lattice paths (http://projecteuler.net/problem=15).

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import numpy as np

def main():
    """
    Solution: the number of routes of a point (x, y) is  equal to the sum of the
    routes of (x, y - 1) and (x -1, y).
    """

    lattice_size = 21

    matrix = np.ones((lattice_size, lattice_size))

    for i in range(1, lattice_size):
        for j in range(1, lattice_size):
            matrix[i, j] = matrix[i -1, j] + matrix[i, j-1]

    print "Number of routes through a %dx%d grid: %d" % (lattice_size - 1,
        lattice_size - 1, matrix[lattice_size - 1, lattice_size - 1])

if __name__ == "__main__":
    main()
