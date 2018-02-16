from IPython.display import clear_output

def main():
    board = [" "," "," "," "," "," "," "," "," "]
    tup = player_input()

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

main()
