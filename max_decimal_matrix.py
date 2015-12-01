#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Given 2D array of only 0s and 1s, find the row which gives the max value.

Input: array = [[0, 1, 0], [1, 1, 0], [1, 0, 1]]
Output: 1 (second row)
"""

__author__ = 'Hwasung Lee'


def to_decimal(array):
    """Given an array of 1s and 0s, return the value in decimal."""
    return int(''.join(map(str, array)), 2)


def max_decimal(matrix):
    """Given a matrix of 1s and 0s representing a binary number, find the max value."""
    return max(range(len(matrix)), key=lambda i: to_decimal(matrix[i]))
