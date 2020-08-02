from IPython.display import clear_output

def main():
    board = [" "," "," "," "," "," "," "," "," "]
    print(f"Welcome to TicTacToe!\n")
    gameState = True

    tup = player_input()
    print()

    while (gameState):
        currentPlayer = 1

        while (currentPlayer == 1 or currentPlayer == 2):
            if(full_board_check(board)):
                print(f'The board is already full! Nobody wins or loses, thus it is considered a draw.')
                gameState = False
                break
            else:
                position = input(f"Player {currentPlayer}, give a position from 1-9 on where to put {tup[currentPlayer-1]}: ")
                if (space_check(board, int(position)-1)):
                    board = place_marker(board, tup[currentPlayer-1], int(position)-1)
                    print()
                    print(f'Current Status of the Board:')
                    display_board(board)
                    print()
                    if(win_check(board, tup[currentPlayer-1])):
                        print(f'Congratulations Player {currentPlayer} for winning the game!')
                        gameState = False
                        break
                    else:
                        if (currentPlayer == 1):
                            currentPlayer = 2
                        else:
                            currentPlayer = 1
                else:
                    print(f"\nPosition has been already taken with element: {board[int(position)-1]}\n")
                    currentPlayer = currentPlayer #restart the loop

    #display_board(board)

def display_board(board):
    clear_output()
    print(f"-------")
    print(f'|{board[0]}|{board[1]}|{board[2]}|')
    print(f"-------")
    print(f'|{board[3]}|{board[4]}|{board[5]}|')
    print(f"-------")
    print(f'|{board[6]}|{board[7]}|{board[8]}|')
    print(f"-------")

def player_input():
    marker = " "
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1 do you want to be X or O? ")
    if(marker == "X"):
        return ("X", "O")
    else:
        return ("O", "X")

def place_marker(board, marker, position):
    board[position] = marker

    return board

def win_check(board, mark):
    condition_one = board[0] == mark and board[1] == mark and board[2] == mark # top row completed
    condition_two = board[3] == mark and board[4] == mark and board[5] == mark # middle row completed
    condition_three = board[6] == mark and board[7] == mark and board[8] == mark # bottom row completed

    condition_four = board[0] == mark and board[3] == mark and board[6] == mark # left column completed
    condition_five = board[1] == mark and board[4] == mark and board[7] == mark # middle column completed
    condition_six = board[2] == mark and board[5] == mark and board[8] == mark # right column completed

    condition_seven = board[0] == mark and board[4] == mark and board[8] == mark # upper-left corner to lower-right corner completed
    condition_eight = board[2] == mark and board[4] == mark and board[6] == mark # upper-right corner to lower-left corner completed

    conditions = [condition_one, condition_two, condition_three, condition_four, condition_five, condition_six, condition_seven, condition_eight]
    
    return any(conditions)

def space_check(board,position):
    if(board[position]== " "):
        return True
    else:
        return False

def full_board_check(board):
    if(" " in board):
        return False
    else:
        return True

# def player_choice(board):

# def replay():

main()