# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      501
# Assignment:   Lab 3.15
# Date:         9/7/2022
#

#input
num = float(input("Please enter the quantity to be converted:\n"))

#conversions
newtons = num * 4.44822
feet = num * 3.28084
kilopascals = num * 101.325
btu_per_hour = num * 3.412142
gallons_per_min = num * 15.850323141489
fahrenheit = (num * 9/5) + 32


s = "is equivalent to"
print(f'{num:.2f} pounds force {s} {newtons:.2f} Newtons')
print(f'{num:.2f} meters {s} {feet:.2f} feet')
print(f'{num:.2f} atmospheres {s} {kilopascals:.2f} kilopascals')
print(f'{num:.2f} watts {s} {btu_per_hour:.2f} BTU per hour')
print(f'{num:.2f} liters per second {s} {gallons_per_min:.2f} US gallons per minute')
print(f'{num:.2f} degrees Celsius {s} {fahrenheit:.2f} degrees Fahrenheit')


