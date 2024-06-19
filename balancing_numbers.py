# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 6.15
# Date:         9/28/2022

from math import *

#Take user input for the number:
num = int(input("Enter a value for n: \n"))

#Use the quadratic equation to calculate r value
disc = 8 * num**2 + 1

r = ((-2 * num - 1) + sqrt(disc))/2


#Num is a balancing number if the discriminant is a perfect square.
if sqrt(disc) == int(sqrt(disc)):
    print(f'{num} is a balancing number with r={r:.0f}') 
else:
    print(f'{num} is not a balancing number')
    