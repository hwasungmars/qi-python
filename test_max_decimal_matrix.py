#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Describe what this package does."""

__author__ = 'Hwasung Lee'


import max_decimal_matrix

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_max_decimal(self):
        """Given a matrix find the max decimal row."""
        array = [[0, 1, 0], [1, 1, 0], [1, 0, 1]]
        expected = 1
        self.assertEqual(expected, max_decimal_matrix.max_decimal(array))


if __name__ == '__main__':
    unittest.main()
