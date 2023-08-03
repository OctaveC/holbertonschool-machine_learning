#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Putting all of our data into arrays
people = ["Farrah", "Fred", "Felicia"]
produce = ["apples", "bananas", "orange", "peaches"]
colors = ["red", "yellow", "#ff8000", "#ffe5b4"]

# Sets labels and titles
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")

# For every one of our fruits, we make a three bar graphs labelled
# with the name of our people, (these serve as our x coordinates)
# each of the bars represent a fruit, and its height represents
# how many each person has (we iterate on our fruit matrice,
# and we pass each row as an argument to plt.bar).
# the "bottom" parameter lets us essentially draw our bars on top
# of each other, instead of replacing the previous ones,
# we sum the previously placed fruits to know at which height to
# put the next bar.
# "label" is used for the legend, and "width" determine how wide our bars are
for ite in range(len(fruit)):
    plt.bar(people, fruit[ite], bottom=np.sum(fruit[:ite], axis=0),
            label=produce[ite], color=colors[ite], width=0.5)

# Sets at which intervals the numbers show up on the y axis
plt.yticks(range(0, 81, 10))

# Makes our legend show up
plt.legend()

# Prints the whole thing
plt.show()
