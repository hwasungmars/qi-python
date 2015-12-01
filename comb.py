#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Implement combinations function"""

__author__ = 'Hwasung Lee'


def choose(iterable, n):
    """Create a n-tuple that gives all the combinations from iterable."""
    if len(iterable) < n:
        return []
    elif n == 1:
        return [(item,) for item in iterable]

    results = []
    for i in range(len(iterable)):
        results += [(iterable[i],) + choice for choice in choose(iterable[i+1:], n-1)]

    return results
