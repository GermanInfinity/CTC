"""
    zero_matrix: set all rows and columns with zeroes to zero
"""
import unittest
def zero_matrix(matrix): 
    # record columns, set row to zeros
    # go back and set columns to zeroes

    columns = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0: 
                columns.add(col)


    for row in range(len(matrix)): 
        if 0 in matrix[row]: 
            matrix[row] = [0] * len(matrix[0])


    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if col in columns: 
                matrix[row][col] = 0
                #columns.remove(col)

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    data = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    #print (zero_matrix(data))
    unittest.main()