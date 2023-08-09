#!/usr/bin/env python3
"""
Module representing a binomial distribution
"""


class Binomial:
    """
    Class representing a normal distribution
    """
    def __init__(self, data=None, n=1, p=0.5):
        """
        Class constructor
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            elif p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")

            self.n = int(n)
            self.p = float(p)

        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")

            # To calculate n and p from a list of data,
            # we need to first calculate the variance.

            # To do that, we:
            # 1. Calculate the mean of the data
            # (the sum of the data divided by the number of data points).
            # 2. Calculate the difference between each data point and the mean.
            # 3. Square each of the differences.
            # 4. Add the squared differences together.
            # 5. Divide the sum of the squared differences
            # by the number of data points (minus one).

            # The result is the variance of the data.

            # The mean is calculated by doing the sum of the data divided
            # by the number of data points
            mean = sum(data) / len(data)

            # Expression used to do steps 2 to step 4
            steps_2_to_4 = sum([(values - mean) ** 2 for values in data])

            # Then we just do step 5
            variance = steps_2_to_4 / len(data)

            # Then calculate the probablity of failure
            # (as in, the probablity of the outcome we want not occuring)
            # using this formula:
            q = 1 - variance / mean

            # We then easily get n (the number of trials)
            # by dividing the mean by the probability of failure
            # (We also round it to nearest integer because of requirement)
            self.n = round(mean / q)

            # And finally, we get the probability of success
            # by dividing the mean by the number of trials
            self.p = mean / self.n

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

        # The probability mass function (PMF) of a binomial distribution
        # is given by the formula:

        # PMF = (n!/(x!(n-x)!) * p^x * (1-p)^(n-x)

        # Where n is the number of trials,
        # p is the probability of success,
        # and x is the number of successes

        # The checker doesn't seem to want to let
        # me make a factorial function, so
        # I'm doing it this way...
        n_factorial = 1
        for ite in range(1, self.n + 1):
            n_factorial *= ite

        x_factorial = 1
        for ite in range(1, k + 1):
            x_factorial *= ite

        n_minus_x_factorial = 1
        for ite in range(1, (self.n - k) + 1):
            n_minus_x_factorial *= ite

        # Here we do the first part of our operation
        first_part = (n_factorial) / (x_factorial * n_minus_x_factorial)

        # And here we do the second part of our operation
        pmf = first_part * (self.p ** k) * (1 - self.p) ** (self.n - k)

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

        # The CDF (or cumulative distribution function) for a binomial
        # distribution is calculated by adding up the probabilities
        # of all the success values that are less than or equal to the
        # given number of successes. This is done using the formula:

        # CDF = Σ (x = 0 to x = number of successes) (λ^x / x!) *e^(-λ)

        # ( (λ^x / x!) *e^(-λ) being how you calculate the PMF)

        # where X is the random variable of the poisson distribution and
        # x is the given number of successes.
        cdf = 0

        # This loop represents our Sigma
        for ite in range(k + 1):
            # In which we do the sum of all our PMFs
            cdf += self.pmf(ite)

        return cdf
