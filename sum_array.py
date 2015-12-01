#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Given two integer arrays that represent an int, write a function that adds them.

For example,
    (1) [1, 2, 3] + [4, 5, 6] => [5, 7, 9]
    (2) [1, 2, 3] + [4, 5, 6, 7] => [4, 6, 9, 0]

Note: Each number is a single integer.
"""

__author__ = 'Hwasung Lee'

def sum_array(array1, array2):
    """Given two array of single integers, sum them and return an array."""
    i = len(array1)-1
    j = len(array2)-1
    carry = 0
    result = []
    while 0 <= i and 0 <= j:
        sumed = array1[i] + array2[j]
        digit = sumed % 10 + carry
        carry = sumed // 10
        result.append(digit)
        i -= 1
        j -= 1

    if 0 <= i:
        array1[i] += carry
        result = result + array1[:i+1]
    elif 0 <= j:
        array2[j] += carry
        result = result + array2[:j+1]

    return result[::-1]
