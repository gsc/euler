import unittest
import p11

class TestP11(unittest.TestCase):

    def test_get_segment_directions(self):

        # For segement of size == 1, every point will have all the directions.
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertEquals(
                    p11.get_segment_directions(x, y, 1, (10, 10)),
                    ['NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE']
                )

        #Top left corner
        self.assertEquals(
            p11.get_segment_directions(0, 0, 5, (10, 10)),
            ['E', 'S', 'SE']
        )

        #Top right corner
        self.assertEquals(
            p11.get_segment_directions(0, 9, 5, (10, 10)),
            ['W', 'SW', 'S']
            )

        #Bottom left corner
        self.assertEquals(
            p11.get_segment_directions(9, 0, 5, (10, 10)),
            ['N', 'NE', 'E']
        )

        #Bottom right corner
        self.assertEquals(
            p11.get_segment_directions(9, 9, 5, (10, 10)),
            ['NW', 'N', 'W']
        )

    def test_get_segment(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        #First row, from the top left
        self.assertEquals(p11.get_segment(matrix, 0, 0, 3, 'E'), [1, 2, 3])

        #First row, from the top right
        self.assertEquals(p11.get_segment(matrix, 0, 2, 3, 'W'), [3, 2, 1])

        #First column, from the top left.
        self.assertEquals(p11.get_segment(matrix, 0, 0, 3, 'S'), [1, 4, 7])

        #First column, from the bottom left.
        self.assertEquals(p11.get_segment(matrix, 2, 0, 3, 'N'), [7, 4, 1])

        #Diagonal SE from the top left
        self.assertEquals(p11.get_segment(matrix, 0, 0, 3, 'SE'), [1, 5, 9])

        #Diagonal SW from the top right
        self.assertEquals(p11.get_segment(matrix, 0, 2, 3, 'SW'), [3, 5, 7])

        #Diagonal NW frm the bottom right
        self.assertEquals(p11.get_segment(matrix, 2, 2, 3, 'NW'), [9, 5, 1])

        #Diagonal NE frm the bottom left
        self.assertEquals(p11.get_segment(matrix, 2, 0, 3, 'NE'), [7, 5, 3])

        #Test retrieving the vector of length == 1 for every cell and direction.
        for direction in ['NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE']:
            for i in range(0, 3):
                for j in range(0, 3):
                    self.assertEquals(
                        p11.get_segment(matrix, i, j, 1, direction),
                        [matrix[i][j]]
                        )

