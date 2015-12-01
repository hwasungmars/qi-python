#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Find the maximum subarray of a given array.

For example, [1, -3, 4, 5, -2, 3] => [4, 5, -2, 3]
"""

__author__ = 'Hwasung Lee'


import logging


def kadane(array):
    """Implementation of Kadane's maximum subarray algorithm."""
    max_so_far = max_ending_here = array[0]
    max_ending_here_array = max_subarray = [array[0]]
    for x in array[1:]:
        if max_ending_here + x > x:
            max_ending_here += x
            max_ending_here_array.append(x)
        else:
            max_ending_here = x
            max_ending_here_array = [x]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_subarray = max_ending_here_array

    return max_subarray
