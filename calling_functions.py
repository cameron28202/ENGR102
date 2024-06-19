# By submitting this assignment, I }}}}}}}}agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 3.18
# Date:         8/24/2022

from math import *

def printresult(shape, side, area):
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

#printresult(name of shape, value of side length, area of shape)
len = float(input("Please enter the side length:\n"))
printresult("triangle", len, (sqrt(3)/4) * len**2)
printresult("square", len, len**2)
printresult("pentagon", len, (1/4 * sqrt(5 * (5+ (2 * sqrt(5)))) * len**2))
printresult("dodecagon", len, (3 * (2 + sqrt(3)) * len**2))
