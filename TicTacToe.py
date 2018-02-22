from IPython.display import clear_output

def main():
    board = [" "," "," "," "," "," "," "," "," "]
    print("Welcome to TicTacToe!")
    gameState = True

    while(gameState):
        

    tup = player_input()
    #display_board(board)

    board = place_marker(board, "$", 1)
    display_board(board)
def display_board(board):
    clear_output()
    print("-------")
    print("|"+ board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------")
    print("|"+ board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------")
    print("|"+ board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-------")

def player_input():
    marker = " "
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1 do you want to be X or O? ")
    if(marker == "X"):
        return ("X" , "O")
    else:
        return( "O", "X")

def place_marker(board, marker, position):
    board[position] = marker

    return board

def win_check(board, mark):

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
def player_choice(board):

def replay():

main()