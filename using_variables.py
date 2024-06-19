# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 1.11
# Date:         8/24/2022

from math import *

#Calculating force (F = ma)
mass = 3
acceleration = 5.5
force = mass * acceleration
print("Force is", force, "N")


#Calculating wavelength (braggs law)
distance = 0.025
angle = 25
print("Wavelength is", 2 * sin(radians(angle)) * distance, "nm")


#Calculating Radon-222 left (N(t) = N2^-t/t1/2)
initial_amount = 5
half_life = 3.8
time = 3
print("Radon-222 left is", initial_amount*2**(-time/half_life), "g")

#Calculating Pressure (ideal gas law)
const = 8.314
num_moles = 5
temp = 415
vol = .25
print("Pressure is", ((num_moles*const*temp)/vol)/1000 , "kPa")