# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 8.10.1
# Date:         10/5/2022
#

inp = input("Enter the time: \n")

# Create inp_list, a list that holds all the numbers of the time
# that the user entered.
inp_list = []
for i in inp:
    if i in nums:
        inp_list.append(i)