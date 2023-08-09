#!/usr/bin/env python3
"""
Function for integral of a polynomial
"""


def integer_checker(number):
    """Checks if the given number is a whole number
    and we therefore need to return an integer"""
    if int(number) == number:
        return int(number)
    else:
        return number


def poly_integral(poly, C=0):
    """Function that calculates the integral of a polynomial,

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

    C is an integer representing the integration constant

    Returns a new list of coefficients representing the integral
    of the polynomial, in the same format mentionned earlier.
    """
    if type(poly) is not list or not isinstance(C, (float, int)):
        return None
    elif len(poly) == 0:
        return None
    elif poly == [0]:
        return [C]

    # Initializing our array with our constant
    integral = [C]

    for index in range(len(poly)):

        # Have to check each individual number for impostors
        if not isinstance(poly[index], (int, float)):
            return None

        # Calculating our integral
        number = poly[index] / (index + 1)

        # Checking if our number should have a decimal
        number = integer_checker(number)

        # Adding our number to our list
        integral.append(number)

    return integral
