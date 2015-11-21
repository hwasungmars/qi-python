#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Given a list of integers, return the highest value obtained by concatenating them together.

For example,
[9, 918, 917] => 9918917
"""

__author__ = 'Hwasung Lee'


import functools


def gt(first, second):
    """A comparator that returns comparison between first ++ second, second ++ first comparison."""
    first_second = int(str(first) + str(second))
    second_first = int(str(second) + str(first))
    return first_second - second_first


def concate(integers):
    """Concate the list of integers and return the largest one."""
    sorted_integers = sorted(integers, key=functools.cmp_to_key(gt), reverse=True)
    return int(''.join(map(str, sorted_integers)))
