# By submitting this assignment, I }}}}}}}}agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 4.19
# Date:         9/20/2022

from math import *

a = int(input("Please enter the coefficient A: \n"))
b = int(input("Please enter the coefficient B: \n"))
c = int(input("Please enter the coefficient C: \n"))

#Quadratic Formula: -b +- root(b**2 - 4 * a * c)/(2 * a)

r1 = 0
r2 = 0


if a == 0 and b == 0:
    #both a and b are 0, invalid input. Produce error
    print("You entered an invalid combination of coefficients!")
elif a == 0:
    #If a is 0, we have a linear equation. 
    #Divide by coefficient of negative c 
    r1 = -c / b
    print(f'The root is x = {r1}')
elif a != 0:
    
    
    # If the disc. is greater than 0, there are 2 real solutions
    #If the disc. is equal to zero, there is 1 real solution
    #If the disc is less than zero, there are 2 imaginary solutions.
    
    disc = b**2 - 4 * a * c
    
    if disc > 0:
        #because disc > 0, there are 2 real roots
        #use quadratic formula to calculate both roots
        r1 = (-b + sqrt(disc)) / (2 * a)
        r2 = (-b - sqrt(disc)) / (2 * a)
        
        #make bigger root listed first
        if r2 > r1:
            temp = r1
            r1 = r2
            r2 = temp
        
        print(f'The roots are x = {r1:.1f} and x = {r2:.1f}')
    
    elif disc == 0:
        #because disc = 0, there is 1 real root
        #use quadratic formula to calculate the root
        r1 = (-b + sqrt(disc)) / (2 * a)
        
        print(f'The root is x = {r1:.1f}')
        
    elif disc < 0:
        
        #because disc < 0, there are 2 imaginary solutions
        #take absolute value of the discriminate to use it to simplify 
        #divide this number and -b by a, use string formatting to add i
        new_b = -b / (2*a)
        new_disc = sqrt(abs(disc)) / (2*a)
        print(f'The roots are x = {new_b:.1f} + {new_disc:.1f}i and x = {new_b:.1f} - {new_disc:.1f}i')
        
        
        
        
        
        