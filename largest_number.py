# By submitting this assignment, I }}}}}}}}agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 4.16
# Date:         9/18/2022

a = float(input("Enter number 1:"))
largest_num = a

b = float(input("Enter number 2:"))
if b > largest_num:
    largest_num = b
    
c = float(input("Enter number 3:"))
if c > largest_num:
    largest_num = c

print(f'The largest number is {largest_num:.1f}')
#hello