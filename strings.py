#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Collection of answers to string questions."""

__author__ = 'Hwasung Lee'


def is_unique(string):
    """Check whether a string has unique characters."""
    return len(string) == len(set(string))

def is_unique_without_extra(string):
    """Check whether a string has unique chars without an additional data structure."""
    sorted_string = sorted(string)
    for i in range(len(sorted_string), -1):
        if sorted_string[i] == sorted_string[i+1]:
            return False

    return True

def reverse_c_string(string, result_so_far):
    """Reverse a C-style null terminating string."""
    if string == '\0':
        return result_so_far + '\0'
    else:
        return reverse_c_string(string[1:], string[0] + result_so_far)

def is_permutation(first, second):
    """Given two strings decide if they are permutations."""
    return sorted(first) == sorted(second)

def replace_whitespace(string):
    """Replace whitespace with %20."""
    return string.replace(' ', "%20")

def basic_string_compression_recur(string):
    """Given string do basic compression."""
    def impl(current, count, remaining):
        if not remaining:
            return "%s%s" % (current, count)
        elif current == remaining[0]:
            return impl(current, count + 1, remaining[1:])
        else:
            return "%s%s" % (current, count) + impl(remaining[0], 1, remaining[1:])

    return impl(string[0], 1, string[1:])

def basic_string_compression_for(string):
    """Given a string do basic compression using a for loop."""
    current = string[0]
    counter = 1

    so_far = []
    for i in string[1:]:
        if i == current:
            counter += 1
        else:
            so_far.append("%s%s" % (current, counter))
            current = i
            counter = 1

    so_far.append("%s%s" % (current, counter))

    return ''.join(so_far)

