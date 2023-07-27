#!/usr/bin/env python3
"""
Adds two arrays together
"""


def add_arrays(arr1, arr2):
    """
    Returns the sum of two arrays as a list
    """

    if len(arr1) != len(arr2):
        return None

    returnal = arr1.copy()
    for row in range(len(arr1)):
        returnal[row] = arr1[row] + arr2[row]

    return returnal
