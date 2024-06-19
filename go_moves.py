# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 
# Date:         10/5/2022
#



# Define turn variable to keep track of whether it is white or black's
# turn. Start with W, or white
turn = "W"

# Define num_moves variable to know when the users can no longer make
# a move (when the board is full)
num_moves = 0

# Define print_board function, which loops through the columns then rows
# of any board and prints it in order.
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], sep = ' ', end = " ")
            if j == 8:
                print("\n")



# Define 9 by 9 2d array filled with empty spaces, which would be
# dots.
board = [["." for x in range(9)] for y in range(9)]


# Create a loop that loops will continue to loop while there are still
# places left to move on the board. Alternate turns between white and 
# black each time an iteration of the loop is concluded. 
# Ask the user for a row and column then if there is a "." at that location,
# fulfill the user's move.

while num_moves != 81:
    invalid_move = True
    if num_moves != 0:
        stop = input("Do you want to stop the game? (Y/N)")
        if stop == "Y" or stop == "y":
            break
    
    # While loop to check if the move the player wants to make is valid
    # A valid move is when the desired position has a ".", which means the
    # position is empty. loop through and asks the user for a new position
    # if the move is invalid.
    
    while invalid_move == True:
        
        
        row = int(input("Enter row of desired position (1-9):\n")) -1 
        col = int(input("Enter column of desired position (1-9):\n")) -1
        
        
        if board[row][col] != ".":
            invalid_move = True
            print("Invalid move.")
        else:
            invalid_move = False
    
    #Alternate turns, place white or black dots
    if turn == "W":
        board[row][col] = chr(9675)
        turn = "B"
    else:
        board[row][col] = chr(9679)
        turn = "W"
        
    num_moves += 1
    print_board(board)
    
print("Game concluded.")
        
        



