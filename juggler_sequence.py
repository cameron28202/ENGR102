# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 6.14
# Date:         9/28/2022

from math import *

#Take user input for a positive number
num = int(input("Enter a positive integer: \n"))

#Define variable count to add to each time the loop
#is iterated, used to determine how many iterations it took
count = 0

#Loop until num is 1
print(f'The Juggler sequence starting at {num} is:')
while(num != 1):
    print(num, end = ", ")
    #If num is even, floor of sqrt of num
    if num % 2 == 0:
        num = int(sqrt(num))
    #If num is odd, floor of num to power of 3/2
    else:
        num = int(sqrt(num**3))
    #Add to count variable each iteration
    count += 1

print(1)
print(f'It took {count} iterations to reach 1')