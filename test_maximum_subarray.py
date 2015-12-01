#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Describe what this package does."""

__author__ = 'Hwasung Lee'


from maximum_subarray import kadane

import unittest


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_kadane(self):
        """Find the maximum subarray."""
        array = [1, -3, 4, 5, -2, 3]
        expected = [4, 5, -2, 3]
        result = kadane(array)
        self.assertEqual(expected, result)

    def test_another_function(self):
        """Describe this test too."""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
