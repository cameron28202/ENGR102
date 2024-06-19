# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 1.11
# Date:         9/8/2022


from math import *

#Calculating force (F = ma)
print("This program calculates the applied force given mass and acceleration\n")
mass = float(input("Please enter the mass (kg):\n"))
acceleration = float(input("Please enter the acceleration (m/s^2):\n"))
force = mass * acceleration
print(f'Force is {force:.1f} N')


#Calculating wavelength (braggs law)
print("This program calculates the wavelength given distance and angle\n")
distance = float(input("Please enter the distance (nm):\n"))
angle = float(input("Please enter the angle (degrees):\n"))
print(f'Wavelength is {2 * sin(radians(angle)) * distance:.4f} nm')


#Calculating Radon-222 left (N(t) = N2^-t/t1/2)
print("This program calculates how much Radon-222 is left given time and initial amount\n")
time = float(input("Please enter the time (days):\n"))
initial_amount = float(input("Please enter the initial amount (g):\n"))
half_life = 3.8
print(f'Radon-222 left is {initial_amount*2**(-time/half_life):.2f} g')

#Calculating Pressure (ideal gas law)
print("This program calculates the pressure given moles, volume, and temperature\n")
const = 8.314
num_moles = float(input("Please enter the number of moles:\n"))
vol = float(input("Please enter the volume (m^3):\n"))
temp = float(input("Please enter the temperature (K):\n"))
print(f'Pressure is {((num_moles*const*temp)/vol)/1000:.0f} kPa')