#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Given a list of integers, select k integers that add up to a multiple of m.  There might be
multiple possibilities, return the minimum if possible if not return None.

For example, consider a list of integers [1, 2, 3, 4, 5].
    (1) For k = 3 and m = 3, we should return (1, 2, 3).
    (2) For m = 7 and k = 1, we should return None.
"""

__author__ = 'Hwasung Lee'


import itertools


def min_sum(ints, k, m):
    """Return the solution to the question."""
    candidates = [x for x in itertools.combinations_with_replacement(ints, k) if sum(x) % m == 0]
    return min(candidates, key=sum) if candidates else None
