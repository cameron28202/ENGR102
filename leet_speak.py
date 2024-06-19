# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.26
# Date:         10/14/2022

#Take user input
inp = input("Enter some text: \n")


#Create dictonary for leet speak letters
leet_speak = {
        'a' : '4',
        'e' : '3',
        'o' : '0',
        's' : '5',
        't' : '7'
    }

#Define answer variable to add each letter of string to, converted or not converted to leet speak
ans = ""
for x in inp:
    if x in leet_speak:
        ans += leet_speak[x]
    else:
        ans += x
        
        
#Print to user
print(f'In leet speak, "{inp}" is:\n{ans}')