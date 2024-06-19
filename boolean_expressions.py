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

a = str(input("Enter True or False for a:\n"))
b = str(input("Enter True or False for b:\n"))
c = str(input("Enter True or False for c:\n"))

############ Part A ############
count = 0
if a == "True" or a == "T" or a == "t":
    a = True
    count += 1
elif a == "False" or a == "F" or a == "f":
    a = False

if b == "True" or b == "T" or b == "t":
    b = True
    count += 1
elif b == "False" or b == "F" or b == "f":
    b = False

if c == "True" or c == "T" or c == "t":
    c = True
    count += 1
elif c == "False" or c == "F" or c == "f":
    c = False
    
    
#print statements
############ Part B ############
print("a and b and c:", a and b and c)
print("a or b or c:", a or b or c)

############ Part C ############
print("XOR:", (a == True and b == False) or (a == False and b == True))

print("Odd number:", count == 1 or count == 3)

