#!/usr/bin/env python3
"""
Returns transpose of a 2D matrix
"""


def matrix_transpose(matrix):
    """
    Returns transpose of a 2D matrix
    """
    trans = []

    for row in range(len(matrix[0])):
        trans.append([])
        for col in range(len(matrix)):
            trans[row].append(matrix[col][row])

    return trans
