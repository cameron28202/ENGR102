# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 6.13
# Date:         9/28/2022


#Take user input for 2 integers:
num = int(input("Enter an integer: \n"))
another_num = int(input("Enter another integer: \n"))

#Set i equal to 1 because numbers go 1 to 100
i = 1

#Loop while i is less than or equal to 100
while i <= 100:
    #Print the number if it's not divisble by both user input numbers
    if i % num != 0 and i % another_num != 0:
        print(i)
    #Print howdy if it's divisible by the first num
    if i % num == 0:
        print("Howdy")
    #Print whoop if it's divisble by the second num
    if i % another_num == 0:
        print("Whoop")
        
    #Add 1 to i each iteration
    i+=1