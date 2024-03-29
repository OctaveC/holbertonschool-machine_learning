#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Draws our histogram, setting the range of the bins at the correct intervals,
# and adding black borders
plt.hist(student_grades, bins=range(0, 110, 10), edgecolor="black")
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.xticks(range(0, 110, 10))
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")
plt.show()
