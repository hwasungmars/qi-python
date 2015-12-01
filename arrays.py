#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Array related questions."""

__author__ = 'Hwasung Lee'


import logging


def zero_rows_columns(matrix):
    """Given an m x n matrix zero the rows and columns that have a 0 in it."""
    rows = []
    columns = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in columns:
                matrix[i][j] = 0

    return matrix


def rotate_counter_clockwise(matrix):
    """Rotate a matrix 90* counter clockwise."""


