# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 10.14
# Date:         11/2/22


#check num method, where my try except statement is.
#use recursion to keep asking user for input after they enter bad input
def check_num(num):
    try:
        num = int(num)
        high_or_low(num)
    except:
        num = input("Bad input! Try again:")
        check_num(num)
        
# high or low method, check if the number is below or above 26
def high_or_low(num):
    global iterate 
    if num < 26:
        print("Too low!")
    elif num > 26:
        print("Too high!")
    else:
        print("You guessed it!", end = " ")
        iterate = False

#print first statement to user
print("Guess the secret number! Hint: it's an integer between 1 and 100...")

#count var, to track the number of guesses
count = 0
#iterate var, to determine whether the while loop should iterate. this will
#be false when the user guesses the correct number.
iterate = True

#while loop, increment iterate by 1 each time
while iterate:
    count += 1
    print("What is your guess?")
    #call check_num
    check_num(input())
    
#print number of guesses using count variable
print(f'It took you {count} guesses.')
    