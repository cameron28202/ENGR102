# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 4.14
# Date:         9/12/2022
#

from math import *

    
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

ans = ""



#a
if a < 0:
    ans += "- "
if a == 1 or a == -1:
    ans += "x^2"
elif a != 0:
    ans += str(abs(a)) + "x^2"

#b
if b < 0:
    ans += " - "
elif b > 0 and a != 0:
    ans += " + "
if b == 1 or b == -1:
    ans += "x"
elif b != 0:
    ans += str(abs(b)) + "x"


#c
if c != 0:
    if c < 0:
        ans += " - " + str(abs(c))
    if c > 0 and b != 0:
        ans += " + " + str(abs(c))
        
    
        

print("The quadratic equation is", ans, "= 0")
