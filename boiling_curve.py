# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 5.4
# Date:         9/27/2022


from math import *


########### Part A: Variables ###########

# Define y0, y1, x0 and x1 variables to calculate slope. 
y0 = 0 
y1 = 0
x0 = 0
x1 = 0

#Define m, the value of the slope.
m = 0

# Set all variables equal to 0 so they can be used in if statements.

# Define variable invalid, which will be set true if the user inputs a
# value that surface heat flux is not available for.
invalid = False


# Define excess_temp, user input variable for the value of x. Use to
# calculate the slope at the end.
excess_temp = float(input("Enter the excess temperature: \n"))


########### Part B: Conditions ###########

# if excess_temp is between certain values, the values of x and y
# will change. For example, if between 1.3 and 5, the slope has to 
# be log10(7000 / 1000) / log10(5 / 1.3). This will be calculated
# using x0, x1, y0 and y1 values.

if excess_temp >= 1.3 and excess_temp <= 5:
    y0 = 1000
    y1 = 7000
    x0 = 1.3
    x1 = 5
    
elif excess_temp > 5 and excess_temp <= 30:
    y0 = 7000
    y1 = 1.5e6
    x0 = 5
    x1 = 30
    
elif excess_temp > 30 and excess_temp <= 120:
    y0 = 1.5e6
    y1 = 2.5e4
    x0 = 30
    x1 = 120
    
elif excess_temp > 120 and excess_temp <= 1200:
    y0 = 2.5e4
    y1 = 1.5e6
    x0 = 120
    x1 = 1200

else:
    invalid = True
    

########### Part C: Calculations ###########

# Using these values set during our if statements based on the 
# excess temperature, the slope is calculated using the log-log plot
# slope formula. This is then plugged into the log-log y position 
# formula to give us our surface heat flux

if invalid == False:
    m = log10(y1 / y0) / log10(x1 / x0)
    y1 = y0 * (excess_temp / x0)**m


########### Part D: Print output ###########

if invalid == True:
    print("Surface heat flux is not available")
else:
    print(f'The surface heat flux is approximately {y1:.0f} W/m^2')





