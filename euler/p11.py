#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 11: (http://projecteuler.net/problem=11).

In the 20x20 grid below, four numbers along a diagonal line have been marked in
red.  The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
"""

import csv

def get_segment_directions(x, y, segment_size, matrix_dimensions):
    """
    For a given point in the matrix (x,y), returns the directions where there is
    a segment of a given size.

    Args:
        x, y: the coordinates of the point  within the matrix
        segment_size: the length of the possible segments
        matrix_dimensions: a tuple with the width and length of the matrix.
    """
    if x < 0 or y < 0 or x > matrix_dimensions[0] or y > matrix_dimensions[1]:
        raise Exception("The point (%d, %d) doesn't belong into the matrix" %
            (x, y))

    distance = segment_size - 1
    directions = []

    if x - distance >= 0 and y - distance >= 0:
        directions += ['NW']

    if x - distance >= 0:
        directions += ['N']

    if x - distance >= 0 and y + distance < matrix_dimensions[1]:
        directions += ['NE']

    if y - distance >= 0:
        directions += ['W']

    if y + distance < matrix_dimensions[1]:
        directions += ['E']

    if x + distance < matrix_dimensions[0] and y - distance >= 0:
        directions += ['SW']

    if x + distance < matrix_dimensions[0]:
        directions += ['S']

    if (x + distance < matrix_dimensions[0] and
        y + distance < matrix_dimensions[1]):
        directions += ['SE']

    return directions

def get_segment(matrix, x, y, segment_size, direction):
    """
    Returns a segment consisting of the n adjacent cells to a point P in a
    given direction

    Args:
        matrix: the matrix from which the segment is to be extracted.
        x, y: the coordinates of the point P where the segment starts.
        segment_size: the number of cells that will be part of the segment.
        direction:
    """

    if direction == 'N':
        segment = [matrix[x - i][y] for i in range(0, segment_size)]

    elif direction == 'S':
        segment = [matrix[x + i][y] for i in range(0, segment_size)]

    elif direction == 'W':
        segment = [matrix[x][y - i] for i in range(0, segment_size)]

    elif direction == 'E':
        segment = [matrix[x][y + i] for i in range(0, segment_size)]

    elif direction == 'NW':
        segment = [matrix[x - i][y - i] for i in range(0, segment_size)]

    elif direction == 'NE':
        segment = [matrix[x - i][y + i] for i in range(0, segment_size)]

    elif direction == 'SW':
        segment = [matrix[x + i][y - i] for i in range(0, segment_size)]

    elif direction == 'SE':
        segment = [matrix[x + i][y + i] for i in range(0, segment_size)]

    return segment

def get_segments(matrix, x, y, segment_size):
    """
    Compute all the valid segments of a given size that start at a point P.
    """
    matrix_dimentions = (len(matrix), len(matrix[0]))
    directions = get_segment_directions(x, y, segment_size, matrix_dimentions)

    segments = []

    for direction in directions:
        segments.append(get_segment(matrix, x, y, segment_size, direction))

    return segments

def main():
    """
    Solution: compute all the 4-digit segments, and its products.
    For a 20x20 grid (400 cells), the number of  possible segments is less 2800
    (7*400, without discounting the edge cells, which don't have 7 possible
    segments), so it can be computed in a reasonable timeframe.
    """

    # Read the matrix from the csv file.
    matrix = []
    with open('p11-matrix.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            matrix.append(map(int, row))


    max_product = 0
    max_segment = []

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            segments = get_segments(matrix, x, y, 4)
            for segment in segments:
                product = reduce(lambda x, y: x*y, segment)
                if product > max_product:
                    max_product = product
                    max_segment = segment

    print "The larget product in the matrix is %d " % max_product
    print "from the segment %s " % max_segment

if __name__ == "__main__":
    main()
