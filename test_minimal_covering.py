#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Test the minimal convering quiz."""

__author__ = 'Hwasung Lee'


import minimal_covering

import unittest


class TestMinimalCovering(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_function(self):
        """Describe this test."""
        first = [1, 3, 5, 2, 3, 1, 4, 5]
        second = [1, 2, 3]

        expected = (3, 6)
        result = minimal_covering.find_minimum_cover(first, second)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
