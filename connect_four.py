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
# Date:         11/14/2022
#


import numpy as np
import turtle

#turn var to determine whos turn it is
turn = 1
#ope ngame details file, a file that keeps track of all moves 
game_details = open('game_details.txt', 'w')

#draw smiley method to draw smiley face when the game ends yay
def draw_smiley(player):
    '''
    
    Parameters
    ----------
    player : integer
        1 or 2.

    Returns
    -------
    no return.

    '''
    pen = turtle.Turtle()
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(150)
    pen.end_fill()
    pen.up()
    
    
    pen.goto(-40,120)
    pen.down()
    pen.fillcolor('black')
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    pen.up()
    
    pen.goto(40, 120)
    pen.down()
    pen.fillcolor('black')
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    pen.up()
    
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()
    
    pen.goto(0, -100)
    pen.write(f'Player {player} wins!!!',  font = ('Arial', 75, 'normal'), align = 'center')
    
    pen.end_fill()
    pen.hideturtle()
    
    turtle.exitonclick()#new thing
    
#is winner function, loops through the board and checks to see if a certain player has won the game
def is_winner(board, player):
    '''

    Parameters
    ----------
    board : 2d Numpy Array
        7 column 6 row vertically suspended grid.
    player : Integer
        Either 1 or 2, to determine which player to check to see has won..

    Returns
    -------
    bool
        Returns whether the player has won (4 in a row)

    '''
    for x in range(5):
        for y in range(6):
          try:
            if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player and board[y][x+3] == player:
                return True
            elif board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                return True
            elif board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True
          except IndexError:
            next
    return False

    
#find row function, loops through the column to see which row the piece should be placed on
def find_row(col, board):
    '''

    Parameters
    ----------
    col : Integer
        The column the user wants to play.
    board : 2d Numpy Array
        7 column 6 row vertically suspended grid.

    Returns
    -------
    Integer
        Returns the row that corresponds with the desired column.

    '''
    if board[5][col] == 0:
        return 6
    if board[0][col] != 0:
        return -1
    for x in range(6):
        try:
            if board[x][col] == 0 and board[x+1][col] != 0:
                return x+1
        except IndexError:
            next
    
#print intructions method
#call when user enters a certain number

def print_instructions():
    print("--------- Connect Four ---------\n")
    print("Instructions: Players choose a number and then\ntake turns dropping colored tokens into a \nseven-column, six-row vertically suspended grid.\n")
    print("Each player will enter their desired column (1-7). To view instructions again, type -1. To end the game early, type -2.")
    
print_instructions()
#define board, a 6 by 7 empty board
board = np.zeros(42).reshape(6, 7)
print(board)

prev_turn = -1
num_turns = 0
#loop through to play game, game ends when is winner is true
while is_winner(board, prev_turn) == False:
    prev_turn = turn
    col = int(input(f'Enter your desired col, player {turn}...\n')) -1
    if col == -2:
        print_instructions()
        print(board)
        col = int(input(f'Enter your desired col, player {turn}...\n')) -1
        
    elif col == -3:
        prev_turn = -1
        break
    
    row = find_row(col, board) - 1
    if row != -1:
        board[row][col] = turn
        game_details.write(f'Player {turn} put a piece at row {row} in column {col}.\n')
        num_turns += 1
        if turn == 1:
            turn = 2
        else:
            turn = 1
    else:
        print("Bad input, try again...")
    print(board)
    
#print who won to the user, close file draw smiley face
if prev_turn == 1:
    print("Player 1 wins. Game concluded.")
    game_details.write(f'Player 1 won the game in {num_turns} turns.')
    game_details.close()
    draw_smiley(prev_turn)
elif prev_turn == 2:
    print("Player 2 wins. Game concluded.")
    game_details.write(f'Player 2 won the game in {num_turns} turns.')
    game_details.close()
    draw_smiley(prev_turn)
else:
    print("No winner:(")
    game_details.write(f'Game concluded.')
    game_details.close()

