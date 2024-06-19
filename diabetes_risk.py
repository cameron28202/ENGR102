# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 4.15
# Date:         9/14/2022
#


from math import *

######### PART A: User Input ##########
# Define variables:
# string variable for sex called sex, stores M or F 
sex = str(input("Enter your sex (M/F): \n"))
# float variable for age called age, stores number of years
age = float(input("Enter your age (years): \n"))
# float variable for BMI called BMI
BMI = float(input("Enter your BMI: \n"))
# str for whether the user is on medication for hypertension called hypertension
hypertension = str(input("Are you on medication for hypertension (Y/N)? \n"))
# boolean for whether the user is on steriods called steriods
steroids = str(input("Are you on steroids (Y/N)? \n"))
# boolean for whether the user smokes cigarettes called smoker
smoker = str(input("Do you smoke cigarettes (Y/N)? \n"))
# boolean for whether the user used to smoke cigarettes previous_smoker
previous_smoker = ""
if smoker == "N" or smoker == "n":
    previous_smoker = str(input("Did you used to smoke (Y/N)? \n"))
# boolean for whether they have a family history of diabetes called history
history = str(input("Do you have a family history of diabetes (Y/N)? \n"))
both = ""
if history == "Y" or history == "y":
    both = str(input("Both parent and sibling (Y/N)? \n"))

######### PART B: Calculations #######6###


# Sex is either 0.879 for female or 0 for male

if sex == "F" or sex == "f":
    sex = 0.879
else:
    sex = 0

# BMI is 0 for under 25
if BMI < 25:
    BMI = 0
# BMI is 0.699 for 25-27.49
elif BMI >= 25 and BMI <= 27.49:
    BMI = 0.699
# BMI is 1.97 for 27.5 to 29.99
elif BMI >= 27.5 and BMI <= 29.99:
    BMI = 1.97
# BMI is 2.518 for over 30
elif BMI >= 30:
    BMI = 2.518

# hypertension is 1.222 if True but 0 if False
if hypertension == "Y" or hypertension == "y":
    hypertension = 1.222
else:
    hypertension = 0

# steroids is 2.191 if True but 0 if false
if steroids == "Y" or steroids == "y":
    steroids = 2.191
else:
    steroids = 0

# smoker is 0 if smoker is False, -0.218 if used to smoke, 0.855 if smoker
if smoker == "Y" or smoker == "y":
    smoker = 0.855
elif previous_smoker == "Y" or previous_smoker == "y":
    smoker = -0.218
else:
    smoker = 0

# family history is 0 if none, 0.728 if parent or sibling, 0.753 if parent and sibling
if history == "Y" or history == "y":
    if both == "Y" or both == "y":
        history = 0.753
    else:
        history = 0.728
else:
    history = 0


n = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history

risk = 100 / (1 + e**n)



############PART C: Printing output to user###########


print(f'Your risk of developing type-2 diabetes is {risk:.1f} %')



 





