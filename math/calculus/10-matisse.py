#!/usr/bin/env python3
"""
Function for derivative of a polynomial
"""


def poly_derivative(poly):
    """Function that calculates the derivative of a polynomial,
    poly is a list of coefficients representing a polynomial
    each index of the list represents the power of x that the coefficient
    belongs to.
    By that I mean that each emplacement in the list itself represent a
    given power of x,
    like, in a list with 4 indexes [0, 0, 0, 0], the first represent x^0
    (so any constant, like, if the number 4 is part of your polynomial,
    that's where it'll go),
    the second x^1 (so that's where something like the 3 in 3x will go),
    the third x^2 (where something like the 5 in 5x^2),
    and the fourth x^3 (where something like the 3 in 3x^3 would go)
    so, if you have a polynome that is 3x^3,
    the list would look like [0, 0, 0, 3].

    Return a new list of coefficients with same format explained earlier
    representing the derivative of the polynomial.
    """
    if type(poly) is not list:
        return None
    elif len(poly) == 0:
        return None
    elif len(poly) == 1:
        return [0]

    derivative = []

    # We do not care about the number at the first index
    # as it does not influence the result of our derivative,
    # so we can slice it with poly[1:]
    # we use enumerate to both iterate over our list and get our numbers
    # from it
    for index, number in enumerate(poly[1:]):

        # We then multiply our index by our number to obtain the correct result
        # (exemple: derivative of 3x is 3, so index=1 and number=3, 1x3=3)
        # (exemple2: derivative 3x^3 is 9x^2, so index=3 and number=3, 3x3=9)
        # We also need to add +1 to our index to rectify our previous slicing
        # We then append it at the end of our list
        derivative.append((index+1)*number)

    return derivative
