#!/bin/python3

import unittest

"""
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.
"""

# brute force


def birthday_brute(s, d, m):
    ncomb = 0
    for i in range(len(s)+1 - m):
        sum = s[i]
        for j in range(i+1, i+m):
            sum += s[j]
        if sum == d:
            ncomb += 1
    return ncomb

# O(n) solution


def birthday(s, d, m):
    sub_array = []
    sum = 0
    ncomb = 0

    for count, ele in enumerate(s):
        # append to sub_arry and sum
        # till elements in sub_array equals m
        if (count < m):
            sub_array.append(ele)
            sum += ele
        # once done check if the sum equals d
        if count == m and sum == d:
            ncomb += 1
        # now reset sum to the sum of last m-1 elements
        # and add the current element
        if count >= m and count < len(s)+1-m:
            sum = sum - sub_array.pop(0)  # O(1)
            sum += ele
            if sum == d:
                ncomb += 1
    return ncomb


if __name__ == '__main__':
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2

    result = birthday(s, d, m)
    # print(result)
    t = unittest.TestCase('__init__')
    t.assertEqual(birthday(s, d, m), 2)
