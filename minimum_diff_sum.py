#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Given three arrays a1, a2, a3, containing distinct positive numbers, find three numbers a, b, c
from a1, a2, a3 respectively such that the following is minimum:

abs(a-b) + abs(b-c) + abs(c-a)
"""

__author__ = 'Hwasung Lee'


import itertools


def abs_dist(a, b, c):
    """Given a, b, c find the abs distance."""
    return abs(a-b) + abs(b-c) + abs(c-a)


def brute_min(a1, a2, a3):
    """Given a1, a2, a3 find the minimum using brute force."""
    candidates = [(a, b, c) for a in a1 for b in a2 for c in a3]
    return min(candidates, key=lambda x: abs_dist(x[0], x[1], x[2]))


def optimised_min(a1, a2, a3):
    """Optimise the brute force search by sorting a3."""
    a3.sort()
    min_so_far = None
    for x, y in itertools.product(a1, a2):
        for i in range(len(a3)):
            dist = abs_dist(x, y, a3[i])
            if not min_so_far or dist < abs_dist(*min_so_far):
                min_so_far = (x, y, a3[i])
            elif i > 0 and abs_dist(x, y, a3[i-1]) < abs_dist(x, y, a3[i]):
                break

    return min_so_far
