#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Test the array summing logic."""

__author__ = 'Hwasung Lee'


import sum_array

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_sum_array_basic(self):
        """When there is no carry over, it should just sum them."""
        expected = [5, 7, 9]
        result = sum_array.sum_array([1, 2, 3], [4, 5, 6])
        self.assertEqual(expected, result)

    def test_sum_array_carry_over(self):
        """When there is a carry over we should count that."""
        expected = [4, 6, 9, 0]
        result = sum_array.sum_array([1, 2, 3], [4, 5, 6, 7])
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
