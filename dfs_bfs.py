#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""BFS and DFS."""

__author__ = 'Hwasung Lee'


from queue import Queue


class Node:
    """A node in the graph."""
    def __init__(self, name):
        self.name = name
        self.children = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return '%s -> %s' % (self.name, self.children)


def bfs(root):
    """Breadth first search."""
    todo = Queue()
    todo.put(root)
    refs = {root: 1}
    while not todo.empty():
        current = todo.get()
        for child in current.children:
            if child in refs:
                refs[child] += 1
            else:
                refs[child] = 1
                todo.put(child)

    return refs


def dfs(root):
    """Depth first search."""
    todo = []
    todo.append(root)
    refs = {root: 1}
    while not len(todo) == 0:
        current = todo.pop()
        for child in current.children:
            if child in refs:
                refs[child] += 1
            else:
                refs[child] = 1
                todo.append(child)

    return refs


def dfs_recur(root):
    """Depth first search recursive version."""
    def inner(current, refs):
        """Inner loop of dfs_recur."""
        for child in current.children:
            if child in refs:
                refs[child] += 1
            else:
                refs[child] = 1
                inner(child, refs)

    refs = {root: 1}
    inner(root, refs)
    return refs
