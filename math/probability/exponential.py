#!/usr/bin/env python3
"""
Module representing an exponential distribution
"""


class Exponential:
    """
    Class representing an exponential distribution
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")

            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")

        # The value of lambda in an exponential distribution is equal
        # to the reciprocal of the mean. This can be calculated by dividing 1
        # by the mean of the data set, or by simply doing the number
        # of data points divided by the sum of that data
            self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """
        Instance method that calculates the value
        of the PDF(Probability Density Function)
        for a given time period.
        """

        if x < 0:
            return 0

        euler = 2.7182818285

        # To calculate the value of the PDF for a given time period
        # in an exponential distribution, you need to use
        # the following formula:

        # PDF = (1/lambda) * e^(-lambda * x),

        # where lambda is the rate parameter and x is the given time period.

        # Not sure why we don't divide 1 by lambda here,
        # but the expected result is incorrect if we do?
        pmf = (self.lambtha) * euler ** (-self.lambtha * x)

        return pmf

    def cdf(self, x):
        """
        Instance method that calculates the value
        of the CDF(cumulative distribution function)
        for a given time period.
        """

        if x < 0:
            return 0

        euler = 2.7182818285

        # The CDF (or cumulative distribution function) for an exponential
        # distribution is calculated using the formula:

        # CDF(x) = 1 - e^(-λx)
        # Where x is the given time period.

        cdf = 1 - euler ** (-self.lambtha * x)

        return cdf
