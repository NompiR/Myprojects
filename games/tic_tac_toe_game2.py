import random
board= ['-', '-','-', '-','-', '-','-', '-','-', '-']

def display_board(board):

    print(board[7] + "|" + board[8] + "|" + board[9])
    print('--------------')
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('--------------')
    print(board[1] + "|" + board[2] + "|" + board[3])


def userchoice():
    marker= ''
    while not ( marker == 'X' or marker == 'O'):
        ip = input("Enter select (X , O): ").upper()
        if ip == 'X':
            return 'X'
        else:
            return 'O'
        break


def inputuser():
    inpt= int(input("enter the number (1-9): "))
    return inpt

def randmod():
    rands= random.randint(1, 2)
    if rands == 1:
        return 'P1'
    else:
        return 'P2'

def updatelist(board, position, updatel):
    board[position] = updatel



def validate(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

gameon = True
count= 0
while gameon:
    count+=1
    display_board(board)
    playersXorO= userchoice()
    if playersXorO == 'X':
        players= randmod()
        if players == 'P1':
            print("Player 2, Start the game: ")
            inpnum= inputuser()
            updatelist(board, inpnum, playersXorO)
            val= validate(board, playersXorO)
            if val == False:
                gameon= True
            else:
                display_board(board)
                print("Player 2 won")
                gameon= False
                

        else:
            print("player 1, start the game: ")
            inpnum= inputuser()
            updatelist(board, inpnum, playersXorO)
            val= validate(board, playersXorO)
            #display_board(board)
            if val == False:
                gameon= True
                
            else:
                display_board(board)
                print("Player 1 Won")
                gameon= False
               
    else:
        players= randmod()
        if players == 'P2':
            print("Player 1, Start the game: ")
            inpnum= inputuser()
            updatelist(board, inpnum, playersXorO)
            val= validate(board, playersXorO)
            #display_board(board)
            if val == False:
                gameon= True
                pass
            else:
                display_board(board)
                print("Won")
                gameon= False

        else:
            print("player 2, start the game: ")
            inpnum= inputuser()
            updatelist(board, inpnum, playersXorO)
            val= validate(board, playersXorO)
            #display_board(board)
            if val == False:
                gameon= True
                pass
            else:
                display_board(board)
                print("Won")
                gameon= False
    #print(count)
    if count >= 8:
        print("Tie")
        gameon= False
