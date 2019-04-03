#!/bin/python3
import unittest


def compareTriplets(a, b):
    """
    Given a and b, determine their respective comparison points.
    For example, a = [1,2,3] and b = [3,2,1]. For elements 0, Bob is awarded a point because a[0] < b[0].
    For the equal elements, no points are earned.

    Parameters:
        a,b: int array

    Returns:
        int array

    """

    score_a = score_b = 0
    for a_val, b_val in zip(a, b):
        if a_val > b_val:
            score_a += 1
        elif a_val < b_val:
            score_b += 1
    return [score_a, score_b]


if __name__ == '__main__':

    a = [10, 25, 9]
    b = [67, 81, 8]

    c = [5, 46, 1]
    d = [9, 22, 1]
    # print(compareTriplets(a, b))
    # print(compareTriplets(c, d))

    result1 = [1, 2]
    result2 = [1, 1]

    tc = unittest.TestCase('__init__')
    tc.assertEqual(compareTriplets(a, b), result1)
    tc.assertEqual(compareTriplets(c, d), result2)
