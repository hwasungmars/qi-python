#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Test minimum diff solution."""

__author__ = 'Hwasung Lee'


import minimum_diff_sum

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_brute_min(self):
        """brute_min should return the minimum using brute force search."""
        a1 = [1, 2]
        a2 = [1, 3]
        a3 = [1, 4]
        expected = (1, 1, 1)
        result = minimum_diff_sum.brute_min(a1, a2, a3)
        self.assertEqual(expected, result)

    def test_optimised_min(self):
        """brute_min should return the minimum using brute force search."""
        a1 = [1, 2]
        a2 = [3, 4]
        a3 = [5, 3]
        expected = (2, 3, 3)
        result = minimum_diff_sum.optimised_min(a1, a2, a3)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
