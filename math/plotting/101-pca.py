#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)


# Creating our Axes3D object using the "projection=‘3d’ keyword"
# Like outlined at:
# https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html
figure = plt.figure()
graph = figure.add_subplot(111, projection='3d')

# The data we want to represent is the 3 dimensional data present in pca_data
# So we're putting each of the columns of our pca_data array into variables
U1 = pca_data[:, 0]
U2 = pca_data[:, 1]
U3 = pca_data[:, 2]

# Scatters our data in our graph thanks to our U1, U2 an U3 coordinates
# The argument c stands for color and we can pass it the whole labels array
# directly thanks to the cmap argument
graph.scatter(U1, U2, U3, cmap="plasma", c=labels, s=20)

# Set labels and titles
graph.set_xlabel("U1")
graph.set_ylabel("U2")
graph.set_zlabel("U3")
graph.set_title("PCA of Iris Dataset")

# Prints our graph
plt.show()
