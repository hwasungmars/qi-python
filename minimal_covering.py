#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""You are given two arrays with integers.  The first array is always larger and contains the second
array integers.  Find the smallest segment of first array that contains all of the integers in the
second.

For example,
first = [1, 3, 5, 2, 3, 1, 4, 5]
second = [1, 2, 3]

Answer: (3, 5)
"""

__author__ = 'Hwasung Lee'


def grow(array, numbers, beginning):
    """Grow the segment until we covered all the numbers."""
    i = beginning
    unseen = set(numbers)
    while len(unseen) > 0 and i < len(array):
        if array[i] in unseen:
            unseen -= {array[i]}
        i += 1

    if not unseen:
        return beginning, i
    else:
        return None


def find_minimum_cover(first, second):
    """Find the minimum cover of the second array."""
    def length(segment):
        """Return the length of a segment."""
        return segment[1] - segment[0]

    candidates = [grow(first, second, i) for i in range(len(first)) if first[i] in second]
    return min([c for c in candidates if c], key=length)
