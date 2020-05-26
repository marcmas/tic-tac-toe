board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

game_stil_work = True

current_player = 'X'

winner = None

def game():
    display_board()
    while game_stil_work:

        choose_place(current_player)

        check_game_over()

        change_player()

    if winner == 'X' or winner == '0':
        print(winner + ' won')
    elif winner == None:
        print("Draw")

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "     1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "     4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "     7 | 8 | 9")

def choose_place(player):
    print(player + 'turn.')
    position = input("Choose a position from 1-9: ")
    choose = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valid = False
    while not valid:
        while position not in choose:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == '-':
            valid= True
        else:
            print("This position is not available")
            
    board[position] = current_player

    display_board()

def check_winner():
    global winner
    winner_row = check_rows()
    winner_columns = check_columns()
    winner_digional = check_diagonals()

    if winner_row:
        winner = winner_row
    elif winner_columns:
        winner = winner_columns
    elif winner_digional:
        winner = winner_digional
    else:
        winner = None

def change_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    elif current_player == '0':
        current_player = 'X'

def check_rows():
    global game_stil_work
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_stil_work = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_stil_work
    coulumn_1 = board[0] == board[3] == board[6] != '-'
    coulumn_2 = board[1] == board[4] == board[7] != '-'
    coulumn_3 = board[2] == board[5] == board[8] != '-'

    if coulumn_1 or coulumn_2 or coulumn_3:
        game_stil_work = False
    
    if coulumn_1:
        return board[0]
    elif coulumn_2:
        return board[1]
    elif coulumn_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_stil_work
    digional_1 = board[0] == board[4] == board[8] != '-'
    digional_2 = board[2] == board[4] == board[6] != '-'

    if digional_1 or digional_2:
        game_stil_work = False
    
    if digional_1:
        return board[0]
    elif digional_2:
        return board[2]
    else:
        return None

def check_end_game():
    global game_stil_work
    if "-" not in board:
        game_stil_work = False
        return True
    else:
        return False

def check_game_over():
    check_winner()
    check_end_game()


if __name__ == "__main__":
    game()
