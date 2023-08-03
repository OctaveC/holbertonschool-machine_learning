#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Draws our graph with the correct color
plt.plot(y, color='red')

# Sets the limits of the x axis
plt.xlim(0, 10)

# Prints our graph
plt.show()
