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