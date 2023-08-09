#!/usr/bin/env python3
"""
Module representing a normal distribution
"""


class Normal:
    """
    Class representing a normal distribution
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Class constructor
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")

            # The mean is calculated by doing the sum of the data divided
            # by the number of data points
            self.mean = float(sum(data) / len(data))

            # The standard deviation of a normal distribution
            # can be calculated using the formula:

            # stddev = √ [ ( ∑ (x - μ)^2 ) / N ]

            # where x is the value of each data point,
            # μ is the mean of the data,
            # and N is the total number of data points.
            pre_sqrt = sum([pow(x - self.mean, 2) for x in data]) / len(data)

            # We can put a number to the power of 0,5
            # to simulate a square root
            self.stddev = pow(pre_sqrt, 0.5)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value
        """

        # The z-score of a given x-value in a normal distribution
        # is calculated using:
        # z-score = (x - mean) / standard deviation.
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score

        """

        # The x-value of a given z-score in a normal distribution
        # is calculated using:
        # x-value = mean + (z-score × standard deviation)
        return self.mean + (z * self.stddev)

    def pdf(self, x):
        """
        Instance method that calculates the value
        of the PDF(Probability Density Function)
        for a given x-value.
        """
        euler = 2.7182818285
        pi = 3.1415926536

        # To calculate the value of the PDF
        # for a given x-value in a normal distribution,
        # we use the formula:

        # PDF(x) = e^(-(z-score(x)/2)^2 / (σ * √(2π))

        # Where µ is the mean,
        # σ is the standard deviation,
        # e is euler,
        # and x is the x-value for which you are looking for the PDF.

        # Splitting our formula in two part for the sake of
        # readibility:
        first_part = euler ** (-0.5 * self.z_score(x) ** 2)
        second_part = (self.stddev * (2 * pi) ** 0.5)

        return first_part / second_part

    def cdf(self, x):
        """
        Instance method that calculates the value
        of the CDF(cumulative distribution function)
        for a given x-value.
        """

        euler = 2.7182818285
        pi = 3.1415926536

        # The value of the CDF for a given x-value
        # in a normal distribution is calculated using:

        # CDF(x) = 1/2 * (1 + erf((x - μ)/(σ * (2^1/2)))

        # Where μ is the mean of the distribution
        # and σ is the standard deviation.

        # Because this is kind of a long operation we'll
        # need to split it in parts

        # This is the part of the calculation that goes
        # inside the erf formula
        inside = (x - self.mean) / (self.stddev * pow(2, 0.5))

        # This is my ERF formula bcause I can't make
        # functions because of the checker...
        erf = 2 / pow(pi, 0.5) * (inside - pow(inside, 3)/3 + pow(inside, 5)/10
                                  - pow(inside, 7)/42 + pow(inside, 9)/216)

        cdf = 0.5 * (1 + erf)

        return cdf
