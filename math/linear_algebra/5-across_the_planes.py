#!/usr/bin/env python3
"""
Sum of two matrices
"""


def add_matrices2D(mat1, mat2):
    """
    sum of two matrices as a list
    """
    if len(mat1[0]) != len(mat2[0]):
        return None
    if len(mat1) == 0 or len(mat2) == 0:
        return None

    return [[(mat1[it1][it2] + mat2[it1][it2]) for it2 in range(len(mat1[0]))]
            for it1 in range(len(mat1))]
