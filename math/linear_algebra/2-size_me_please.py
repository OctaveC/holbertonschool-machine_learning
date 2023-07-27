#!/usr/bin/env python3
"""
calculates the shape of a matrix
"""


def matrix_shape(matrix):
    """
    Takes Matrix as Input
    Returns list of integers
    """
    if type(matrix[0]) is list:
        return [len(matrix)] + matrix_shape(matrix[0])
    else:
        return [len(matrix)]
