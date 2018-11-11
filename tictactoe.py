#CMPT 120 Intro to Programming
#Lab #6 - Lists and Error Handling
#Author: Ian Miller
#Created: 2018-11-08
#must complete "A Simple Implementation of Tic-Tac-Toe" (through step #6)

symbol = [ " ", "x", "o"]

def printRow(row):
    #initialize output to the left border
    output = "|"
    #for each square in the row...
    for cell in row:
        #add to output the symbol for this square followed by a border
        output += " " + symbol[cell] + "|"
    #print the completed output for this row
    print(output)

def printBoard(board):
    #print the top border
    print("+--------+") 
    #for each row in the board...
    for row in board:
        #print the row
        printRow(row)
        #print the next border
        print("+--------+")
    print(board)

def markBoard(board, row, col, player):
    #check to see whether the desired square is blank
    if board[row][col] == 0:
        #if so, set it to the player number
        board[row][col] = player
        return True
    else:
        print("\nThat cell is not blank. Please choose another cell.\n")
        return False
    

def getPlayerMove():
    #prompt the user separately for the row and column numbers
    row = int(input("\nEnter the row of the space you would like to mark: "))
    col = int(input("\nEnter the column of the space you would like to mark: "))
    #then return that row and colum instead of (0,0)
    return (row,col)

def hasBlanks(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return True
    #if no square is blank, return False
    return False

def main():
    board = [ [0,0,0],
              [0,0,0],
              [0,0,0] ]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        marked = markBoard(board, row, col, player)
        #switch player for next turn
        if marked == False:
            continue
        player = player % 2 + 1
            
main()
    
