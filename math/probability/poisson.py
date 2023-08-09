#!/usr/bin/env python3
"""
Module representing a poisson distribution
"""


class Poisson:
    """
    Class representing a poisson distribution
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

            # Lambtha can be defined as simply the mean of the available data
            # in this context
            # The mean is calculated by doing the sum of the data divided
            # by the number of data points
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Instance method that calculates the value
        of the PMF(probability mass function)
        for a given number of “successes”.
        """
        if type(k) is not int:
            k = int(k)

        if k < 0:
            return 0

        euler = 2.7182818285

        # The probability mass function (PMF) for a Poisson distribution
        # is given by:
        # P(x; λ) = (λ^x / x!) *e^(-λ)

        # Where x is the observed number of successes,
        # λ is the expected mean number of successes,
        # and e is the euler constant (approximately 2.7182818285 here).

        # To calculate the PMF value for a given number of successes,
        # simply substitute the observed number of successes (x)
        # and the expected mean number of successes (λ) into the formula.

        # The checker doesn't seem to want to let
        # me make a factorial function, so
        # I'm putting this here.
        factor = 1

        for ite in range(1, k + 1):
            factor *= ite

        pmf = (self.lambtha ** k / factor) * euler ** (-self.lambtha)

        return pmf

    def cdf(self, k):
        """
        Instance method that calculates the value
        of the CDF(cumulative distribution function)
        for a given number of “successes”.
        """
        if type(k) is not int:
            k = int(k)

        if k < 0:
            return 0

        # The CDF (or cumulative distribution function) for a poisson
        # distribution is calculated by adding up the probabilities
        # of all the success values that are less than or equal to the
        # given number of successes. This is done using the formula:

        # CDF = Σ (x = 0 to x = number of successes) (λ^x / x!) *e^(-λ)
        # (λ^x / x!) *e^(-λ) being how you calculate the PMF

        # where X is the random variable of the poisson distribution and
        # x is the given number of successes.
        cdf = 0

        # This loop represents our Sigma
        for ite in range(k + 1):
            # In which we do the sum of all our PMFs
            cdf += self.pmf(ite)

        return cdf
