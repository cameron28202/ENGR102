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


# Create dictonary nums that has keys that are number values 0-9 and
# values which are lists of each line of the number in ascii.
nums = {
        
        "0" : ["000", "0 0", "0 0", "0 0", "000"],
        "1" : [" 1 ", "11 ", " 1 ", " 1 ", "111"],
        "2" : ["222", "  2", "222", "2  ", "222"],
        "3" : ["333", "  3", "333", "  3", "333"],
        "4" : ["4 4", "4 4", "444", "  4", "  4"],
        "5" : ["555", "5  ", "555", "  5", "555" ],
        "6" : ["666", "6  ", "666", "6 6", "666"],
        "7" : ["777", "  7", "  7", "  7", "  7"],
        "8" : ["888", "8 8", "888", "8 8", "888"],
        "9" : ["999", "9 9", "999", "  9", "999"]
        }


# Create inp, variable for user input of the time
inp = input("Enter the time: \n")

# Create inp_list, a list that holds all the numbers of the time
# that the user entered.
inp_list = []
for i in inp:
    if i in nums:
        inp_list.append(i)

# Loop through list 5 times to print each line of each number. Create a second for loop
# inside the 
for i in range(5):
    

    for x in range(len(inp_list)):
        print(nums[inp_list[x]][i], end = " ")
        
        if x == len(inp_list) // 2 - 1:
            if i == 1 or i == 3:
                print(":", end = " ")
            else:
                print(" ", end = " ")
        if x == len(inp_list) - 1:
            print("")