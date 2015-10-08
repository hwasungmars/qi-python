#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Tests for string related questions."""

__author__ = 'Hwasung Lee'


import unittest
import strings


class TestPackage(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_is_unique(self):
        """Test whether we have uniq chars."""
        self.assertFalse(strings.is_unique("hello"))
        self.assertTrue(strings.is_unique("abc"))

    def test_is_unique_without_extra(self):
        """Test whether we have uniq chars without additional structure."""
        self.assertFalse(strings.is_unique("hello"))
        self.assertTrue(strings.is_unique("abc"))

    def test_reverse_c_string(self):
        """Test whether we reverse a C-style string correctly."""
        self.assertEqual("abc\0", strings.reverse_c_string("cba\0", ""))

    def test_permutation(self):
        """Given two strings are they permutations?"""
        self.assertTrue(strings.is_permutation("abc", "cba"))
        self.assertFalse(strings.is_permutation("abc", "aba"))

    def test_replace_whitespace(self):
        """HTML style whitespace."""
        self.assertEqual("hello%20world!", strings.replace_whitespace("hello world!"))

    def test_basic_string_compression(self):
        """Compress the string."""
        self.assertEqual("a1b2a1", strings.basic_string_compression_recur("abba"))
        self.assertEqual("a1b2a1", strings.basic_string_compression_for("abba"))


if __name__ == '__main__':
    unittest.main()

