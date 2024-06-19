# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 12.17
# Date:         11/28/2022

import numpy as np
import matplotlib.pyplot as plt

#define m and v, arrays and variables
m = np.array([[1.01, 0.09], [-0.09, 1.01]])
v = np.array([0, 1])
plt.figure(0)

#label x and y axis, create title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Golden-Ratio Spiral")
#for loop w/ 200 iterations
for i in range(200):
    v = v @ m
    plt.plot(v[0], v[1], marker = ".", color = "black")
print(v)