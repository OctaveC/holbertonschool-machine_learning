#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Draws our graphs
plt.plot(x, y)

# Makes our graph a logarythm based on y
plt.semilogy()

# Set the limits of the x axis
plt.xlim(0, 28650)

plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.title("Exponential Decay of C-14")
plt.show()
