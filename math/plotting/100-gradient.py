#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))


# Set labels and titles
plt.xlabel("x coordinate (m)")
plt.ylabel("y coordinate (m)")
plt.title("Mountain Elevation")

# Draws our graph, the c stands for color,
# and we pass it the z argument so that the color depends on height
plt.scatter(x, y, c=z)

# Adds a side bar called a colorbar to our graph.
# (we don't need to pass it a graph as an argument,
# as it default to the current image)
plt.colorbar(label="elevation (m)")

# Prints our graph
plt.show()
