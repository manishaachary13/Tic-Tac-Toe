#TIC-TAC-TOE
#Algorithm:
'''
1. Create a board(3*3)
2. Players should be ready(X or O)
3. Either X or O should start the game
4. Swap the Players (or) Flip the Players
5. Calculate '''

#Code For The Game
board=['-','-','-',
       '-','-','-',
       '-','-','-'] #Creating a board

player="X"  #Initializing the player
game_is_going=True
count=0
def display_board():        #Printing the board pattern
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | " +board[7]+" | "+board[8])

def handle_turn(): #input the position
    global count,game_is_going
    if count==9:
        game_is_going=False
    else:
        position=int(input("Enter the position from 0 to 8: "))
        if board[position] == '-':
            board[position] = player
            count+=1

        elif board[position] != '-':
            print("This position is already filled. Choose another one:")
            handle_turn()



def swap_player():  #swap the player after each input
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

def row():
    global game_is_going
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        game_is_going=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    else:
        return board[6]
def col():
    global game_is_going
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    if col1 or col2 or col3:
        game_is_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    else:
        return board[2]
def diagonal():
    global game_is_going
    dia1 = board[0] == board[4] == board[8] != '-'
    dia2 = board[2] == board[4] == board[6] != '-'
    if dia1 or dia2:
        game_is_going=False
    if dia1:
        return board[0]
    else:
        return board[2]


def check_winner():
    global winner
    row_winner = row()
    col_winner = col()
    dia_winner = diagonal()
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif dia_winner:
        winner=dia_winner

def play_game():
    while game_is_going:
        display_board()
        handle_turn()
        swap_player()
        check_winner()

    if winner == "X":
        print("X is the winner")
    elif winner == "O":
        print("O is the winner")
    else:
        print("Game is tie")

play_game()