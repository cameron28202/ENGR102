# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 2.9.1
# Date:         8/31/2022

from math import *

t1 = 10
t2 = 55
y1 = 2026
y2 = 23026


slope = (y2-y1)/(t2-t1)

t = 25
pos = slope * (t-t1) + y1

print("Part 1:")
print("For t = 25 minutes, the position p =", pos, "kilometers") 

radius = 6745
circumference = 2 * pi * radius
t = 300
pos = slope * (t-t1) + y1
dist_houston = pos % circumference

print()
print("Part 2:")
print("For t = 300 minutes, the position p =", dist_houston, "kilometers")
