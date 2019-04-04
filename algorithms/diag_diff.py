#!/bin/python3
import unittest

# Complete the diagonalDifference function below.


def diagonalDifference(arr):
    """
    Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
    """

    sum_diag1 = 0
    sum_diag2 = 0

    j = len(arr) - 1
    for i in range(len(arr)):
        sum_diag1 += arr[i][i]
        sum_diag2 += arr[i][j]
        j -= 1
    return abs(sum_diag1 - sum_diag2)


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = 15

    tc = unittest.TestCase('__init__')
    tc.assertEqual(diagonalDifference(arr), result)
