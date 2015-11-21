#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Test highest number concatenation answer."""

__author__ = 'Hwasung Lee'


import unittest
from highest_value_string_concate import concate


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_concate(self):
        """Concate the list of integers to obtain the highest value."""
        integers = [9, 918, 917]
        expected = 9918917
        self.assertEqual(expected, concate(integers))

        integers = [1, 112, 113]
        expected = 1131121
        self.assertEqual(expected, concate(integers))

        integers = [9, 1, 99]
        expected = 9991
        self.assertEqual(expected, concate(integers))


if __name__ == '__main__':
    unittest.main()
