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
    
    return [[(mat1[ite1][ite2] + mat2[ite1][ite2]) for ite2 in range(len(mat1[0]))]
        for ite1 in range(len(mat1))]
