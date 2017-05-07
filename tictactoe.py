# create board
board = [[0,0,0], [0,0,0], [0,0,0]]

# who is winner
def whoIsWinner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] > 0:
            return row[0]

    for i in [0,1,2]:
        if board[0][i] == board [1][i] == board[2][i] and board[0][i] > 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board [2][2] and board[0][0] > 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board [2][0] and board[0][2] > 0:
        return board[0][2]


# tie
def isTie():
    if whoIsWinner() == None and isFinished() == True:
        return True
    else:
        return False







def isFinished():
    zer_lst = []
    for row in board:
        for el in row:
            if el == 0:
                zer_lst.append('O')
    if len(zer_lst) != 0:
        return False
    else:
        return True








#printBoard(board)

def printBoard():
    # Iterating over rows

    for row in board:
        l = []
        # row is for example: [0,0,1]
        for el in row:

            # el is either 0, 1 or 2
            if el == 1:
                l.append('X')
            elif el == 2:
                l.append('O')
            else:
                l.append(" ")
        print "-----"
        print "|".join(l)

round_no = 0
while isFinished() == False:
    printBoard()
    print 'Round:', round_no
    row_loc = int(raw_input('Which row?'))
    col_loc = int(raw_input('Which column?'))
    if board[row_loc][col_loc] != 0:
        print 'Please choose another cell'
        continue
    if round_no %2 == 0:
        board[row_loc][col_loc] = 1
    else:
        board[row_loc][col_loc] = 2
    round_no += 1
    if whoIsWinner() != None:
        printBoard()
        print 'The winner is player no.', whoIsWinner()
        break
    if isTie() == True:
        printBoard()
        print 'There is a tie'
        break










# interaction with a user