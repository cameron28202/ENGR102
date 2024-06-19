# By submitting this assignment, I }}}}}}}}agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 4.18
# Date:         9/18/2022

day = int(input("Please enter a positive value for day:"))

if day > 0:

    if day <= 10:
        #There are 5 gadgets produced per day
        #Slope is the area under the curve, which is a square
        gadgets_produced = day * 5
    elif day > 10 and day <= 60:
        #There are now 50 gadgets produced per day
        #Slope is area under the curve, which is still a square, starting at 1 again
        #Y intercept is 100 because for the first 10 days, 100 gadgets are produced.
        gadgets_produced = ((day-10) * 50) + 50
    elif day > 61 and day < 100:
        gadgets_produced = (2550 + (1/2) * (49 + (50-(day-60))) * (day-60))
    else:
        gadgets_produced = 3730
    
        
    print(f'The total number of gadgets produced on day {day} is {gadgets_produced:.0f}')
else:
    print("You entered an invalid number!")
    