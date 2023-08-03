#!/usr/bin/env python3
"""
Sigma function
"""


def canUnlockAll(boxes):
    """Function that calculates sigma,
    n is the stopping condition
    Returns the integer value of the sum
    """
    if type(n) != int or n < 1:
        return None

    # return n**2 + summation_i_squared(n-1)
    # Sadly does not work as a recursive function
    # due to checker requirement.

    return (n*(n + 1) * (2 * n + 1)) // 6
