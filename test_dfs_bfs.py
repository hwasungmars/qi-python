#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Describe what this package does."""

__author__ = 'Hwasung Lee'


import unittest

from dfs_bfs import Node
from dfs_bfs import bfs
from dfs_bfs import dfs
from dfs_bfs import dfs_recur


class TestBFSDFS(unittest.TestCase):
    """Standard test class inheriting from unittest.TestCase"""

    def test_bfs(self):
        """Run bfs on a simple graph."""
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')

        a.children = [b, c]
        b.children = [c]
        c.children = [d]

        expected = {a: 1, b: 1, c: 2, d: 1}
        result = bfs(a)
        self.assertEqual(expected, result)

    def test_dfs(self):
        """Run dfs on a simple graph."""
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')

        a.children = [b, c]
        b.children = [c]
        c.children = [d]

        expected = {a: 1, b: 1, c: 2, d: 1}
        result = dfs(a)
        self.assertEqual(expected, result)

    def test_dfs_recur(self):
        """Run dfs recur on a simple graph."""
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')

        a.children = [b, c]
        b.children = [c]
        c.children = [d]

        expected = {a: 1, b: 1, c: 2, d: 1}
        result = dfs_recur(a)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
