#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

figure = plt.figure()
figure.suptitle("All in One")

# FIRST GRAPH

# Creates a subplot at a specific location inside a regular grid.
graph1 = plt.subplot2grid(shape=(3, 2), loc=(0, 0))

# Set the limit on the x axis
graph1.set_xlim(0, 10)

# Set at which interval the numbers show up on the x and y axis
graph1.set_xticks(range(0, 11, 2))
graph1.set_yticks(range(0, 1010, 500))

# Draws our graph with the correct color
graph1.plot(y0, color="red")

# SECOND GRAPH

# Creates a subplot at a specific location inside a regular grid.
graph2 = plt.subplot2grid(shape=(3, 2), loc=(0, 1))

# Set labels and titles along with correct font size
graph2.set_xlabel("Height (in)", fontsize="x-small")
graph2.set_ylabel("Weight (lbs)", fontsize="x-small")
graph2.set_title("Men's Height vs Weight", fontsize="x-small")

# Set the limits of the x and y axises
graph2.set_xlim(54, 83)
graph2.set_ylim(165, 194)

# Set at which intervals the numbers show up on the x and y axis
graph2.set_xticks(range(60, 90, 10))
graph2.set_yticks(range(170, 200, 10))

# Draws our graph with the correct color, parameter s stands for size
# of the dots
graph2.scatter(x1, y1, color="magenta", s=10)

# THIRD GRAPH

# Creates a subplot at a specific location inside a regular grid.
graph3 = plt.subplot2grid(shape=(3, 2), loc=(1, 0))

# Makes our graph a logarythm based on y
graph3.semilogy()

# Set the limits of the x axis
graph3.set_xlim(0, 28650)

# Set labels and titles along with correct font size
graph3.set_xlabel("Time (years)", fontsize="x-small")
graph3.set_ylabel("Fraction Remaining", fontsize="x-small")
graph3.set_title("Exponential Decay of C-14", fontsize="x-small")

# Set at which intervals the numbers show up on the x axis
graph3.set_xticks(range(0, 28650, 10000))

# Draws our graph
graph3.plot(x2, y2)

# FOURTH GRAPH

# Creates a subplot at a specific location inside a regular grid.
graph4 = plt.subplot2grid(shape=(3, 2), loc=(1, 1))

# Set the limits of the x and y axises
graph4.set_xlim(0, 20000)
graph4.set_ylim(0, 1)

# Set labels and titles along with correct font size
graph4.set_xlabel("Time (years)", fontsize="x-small")
graph4.set_ylabel("Fraction Remaining", fontsize="x-small")
graph4.set_title("Exponential Decay of Radioactive Elements",
                 fontsize="x-small")

# Draws both our graphs
graph4.plot(x3, y31, color="red", linestyle="dashed", label="C-14")
graph4.plot(x3, y32, color="green", label="Ra-226")

# Makes our legend show up and makes it small
graph4.legend(prop={'size': 'x-small'})

# FIFTH GRAPH

# Creates a subplot at a specific location inside a regular grid,
# and makes it take up 2 spots.
graph5 = plt.subplot2grid(shape=(3, 2), loc=(2, 0), colspan=2)

# Set the limits of the x and y axises
graph5.set_xlim(0, 100)
graph5.set_ylim(0, 30)

# Set at which intervals the numbers show up on the x axis
graph5.set_xticks(range(0, 110, 10))

# Set labels and titles along with correct font size
graph5.set_xlabel("Grades", fontsize="x-small")
graph5.set_ylabel("Number of Students", fontsize="x-small")
graph5.set_title("Project A", fontsize="x-small")

# Draws our histogram, setting the range of the bins at the correct intervals,
# and adding black borders
graph5.hist(student_grades, bins=range(0, 110, 10), edgecolor="black")

# Makes it so our text doesn't overlap in an ugly way
figure.tight_layout()

# Prints the whole thing
plt.show()
