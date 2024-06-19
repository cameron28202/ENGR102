# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 11.12
# Date:         11/13/2022

def find_num(str):
    for x in range(len(str)):
        if str[x] in "1234567890":
            return int(str[x:len(str)])


#game variable, to open the game.txt file with instructions
game = open("game.txt", "r")
#coins file, to output the number of coins gained or lost per turn
coins = open("coins.txt", "w")

lines = list(game)
x = 0
num_coins = 0
while x < len(lines):
    if "coin" in lines[x]:
        if "+" in lines[x]:
            num_coins += find_num(lines[x])
            coins.write(f'{find_num(lines[x])}\n')
        else:
            num_coins -= find_num(lines[x])
            coins.write(f'-{find_num(lines[x])}\n')
        x += 1
        
    elif "jump" in lines[x]:
        #what do i do if it jumps too far 
        if "+" in lines[x]:
            x += find_num(lines[x])
        else:
            x -= find_num(lines[x])
    else:
        x += 1
print(f'Total coins collected: {num_coins}')
game.close()
coins.close()




