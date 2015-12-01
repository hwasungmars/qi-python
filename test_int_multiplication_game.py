#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Test the integer multiplication game."""

__author__ = 'Hwasung Lee'


import int_multiplication_game

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_min_sum_valid(self):
        """Find the solution that satisfies the constraints."""
        ints = [1, 2, 3, 4, 5]
        k = 3
        m = 3
        expected = (1, 1, 1)
        self.assertEqual(expected, int_multiplication_game.min_sum(ints, k, m))

    def test_min_sum_invalid(self):
        """If there is no solutions, we should return None."""
        ints = [1, 2, 3, 4, 5]
        k = 1
        m = 7
        self.assertIsNone(int_multiplication_game.min_sum(ints, k, m))


if __name__ == '__main__':
    unittest.main()
