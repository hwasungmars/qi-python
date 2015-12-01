#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Describe what this package does."""

__author__ = 'Hwasung Lee'


import comb

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_choose(self):
        """Choose should give the desired outcome."""
        iterable = [1, 2, 3]
        n = 2
        expected = [(1, 2), (1, 3), (2, 3)]
        self.assertEqual(expected, comb.choose(iterable, 2))


if __name__ == '__main__':
    unittest.main()
