board= ['-', '-','-', '-','-', '-','-', '-','-', '-']

def display_board(board):

    print(board[7] + "|" + board[8] + "|" + board[9])
    print('--------------')
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('--------------')
    print(board[1] + "|" + board[2] + "|" + board[3])


def user_choices():
    marker= ''
    while not (marker == 'X' or marker == 'O'):
        choice_xoro = input("Enter select (X , O): ").upper()
        if choice_xoro not in ('X', 'O'):
            return False
        else:
            if choice_xoro == 'X':
                return 'X'
            else:
                return 'O'
        #break


def input_user():
    input_number= int(input("enter the number (1-9): "))
    return input_number


def update_list(board, position, updatel):
    if position in range(1,10):
        board[position] = updatel
    else:
        return False



def win_check(board, mark):
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

print("Welcome to Tic Tac Toe game")
display_board(board)
while gameon:
    count +=1
    user_choice= user_choices()
    if not user_choice:
        print("Please enter only X or O")
        count -=1
    elif user_choice == 'X':
        print("X's Start")
        user_input= input_user()

        my_update_validate= update_list(board, user_input, user_choice)
        if not my_update_validate:
            print("This is not numbers, should be range between (1 to 9)")
            count -=1
        display_board(board)
        val= win_check(board, user_choice)
        if not val:
            gameon= True
        else:
            print("Congratulations! X have won the game!")
            gameon= False
    else:
        print("O's Start")
        input_num= input_user()
        my_update_validate= update_list(board, input_num, user_choice)

        if not my_update_validate:
            print("This is not numbers, should be range between (1 to 9)")
            break
        display_board(board)
        val= win_check(board, user_choice)
        if not val:
            gameon= True
        else:
            print("Congratulations! O have won the game!")
            gameon= False
    if count >= 8:
        print("The game is a draw!")
        gameon= False
    
