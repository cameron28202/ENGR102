# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 4.13
# Date:         9/12/2022
#

from math import *

paid = float(input("How much did you pay?\n"))
cost = float(input("How much did it cost?\n"))

change = round(paid - cost, 2)

num_quarters = 0
num_dimes = 0
num_nickels = 0
num_pennies = 0

print(f'You received ${change:.2f} in change. That is...')
if change % .25 != change:
    num = round(change % .25, 2)
    num_quarters = round((change - num) / .25, 2)
    change = num
    
if change % .10 != change:
    num = round(change % .10, 2)
    num_dimes = round((change - num) / .10, 2)
    change = num
    
if change % .05 != change:
    num = round(change % .05, 2)
    num_nickels = round((change - num) / .05, 2)
    change = num

#add remaining change to pennies
num_pennies += change * 100

if(num_quarters > 0):
    if num_quarters == 1:
        print(f'{num_quarters:.0f} quarter')
    else:
        print(f'{num_quarters:.0f} quarters')

if(num_dimes > 0):
    if num_dimes == 1:
        print(f'{num_dimes:.0f} dime')
    else:
        print(f'{num_dimes:.0f} dimes')
        
if(num_nickels > 0):
    if num_nickels == 1:
        print(f'{num_nickels:.0f} nickel')
    else:
        print(f'{num_nickels:.0f} nickels')
        
if(num_pennies > 0):
    if num_pennies == 1:
        print(f'{num_pennies:.0f} penny')
    else:
        print(f'{num_pennies:.0f} pennies')
    


    