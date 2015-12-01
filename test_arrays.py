#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Tests for array related questions."""

__author__ = 'Hwasung Lee'

import arrays

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_zero_rows_columns(self):
        """We should be able to zero the rows and columns."""
        matrix = [[0, 1, 2], [0, 3, 4], [5, 6, 7]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 6, 7]]
        result = arrays.zero_rows_columns(matrix)
        self.assertEqual(expected, result)

    def test_another_function(self):
        """Describe this test too."""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

