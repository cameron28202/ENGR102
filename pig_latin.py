# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.25
# Date:         10/14/2022

#List of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#String to contain all converted words
ans = ""
#Take user input for words
inp = input("Enter word(s) to convert to Pig Latin: \n")

#Use string split to divide string into words splitting every space
split = inp.split(" ")

#Loop through words, check if starts with vowel or not, follow pig latin rules
for x in split:
    if x[0] in vowels:
        ans += x + "yay "
    else:
        i = 0
        while x[i] not in vowels:
            i+=1
        ans += x[i:] + x[:i] + "ay "
    
    
#Print converted into pig latin
print(f'In Pig Latin, "{inp}" is: {ans}')