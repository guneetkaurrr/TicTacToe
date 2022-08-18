# list of all values on the board
board = ["1", "2", "3",
          "4", "5", "6",
          "7", "8", "9"]

player = "X"
winner = None
gameOn = True

# prints the game board
def printGame(board):

    i = 0
    while i < 8:
        print((board[i] + " | " + board[i + 1] + " | " + board[i + 2]))
        i = i + 3

# takes the players' input
def userInput(board):

    global player
    playerInput = int(input("Please enter any available number from 1-9: "))
    if playerInput < 1  or playerInput > 9:
        print("That spot does not exist on the board! Please try again. ")
    elif board[playerInput - 1] != str(playerInput):
        print("That spot is already taken! Please try again. ")
        switch()
    else:
        board[playerInput - 1] = player

# check if any player won horizontally
def checkHor(board):

    global winner
    i = 0
    while i < 7:
        if board[i] == board[i + 1] == board[i + 2] and ((board[i] == "X") or (board[i] == "O")):
            winner = board[i]
            return True
        i = i + 3

# check if any player won vertically
def checkVer(board):

    global winner
    i = 0
    while i < 3:
        if board[i] == board[i + 3] == board[i + 6] and ((board[i] == "X") or (board[i] == "O")):
            winner = board[i]
            return True
        i = i + 1

# check if any player won diagonally
def checkDiag(board):

    global winner
    if board[0] == board[4] == board[8] and (board[0] == "X" or (board[0] == "O")):
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and ((board[2] == "X") or (board[2] == "O")):
        winner = board[2]
        return True

# checks for a tie
def checkTie(board):

    global gameOn
    allSlots = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]
    equal = [x for x in board if x in allSlots]
    if len(equal) == 0:
        printGame(board)
        print("This round is a tie. ")
        gameOn = False
        return True

# checks for a winner or tie
def checkWin():

    global gameOn
    if checkHor(board) or checkVer(board) or checkDiag(board):
        print("Congratulations, " + winner + " is the winner")
        printGame(board)
        gameOn = False
    elif checkTie(board):
        checkTie(board)

# switches the player
def switch():

    global player
    if player == "X":
        player = "0"
    else:
        player = "X"

# loop that calls all game functions until someone wins or there's a tie
while gameOn:
    printGame(board)
    userInput(board)
    checkWin()
    switch()