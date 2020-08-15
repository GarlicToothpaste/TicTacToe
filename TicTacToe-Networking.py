def display_board():
    clear_output()
    print(f"-------")
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"-------")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"-------")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print(f"-------\n")

def player_input():
    marker = input("Player 2, do you want to be X or O? ")

    while not (marker == "X" or marker == "O"):
        print()
        marker = input("Player 2, do you want to be X or O? ")

    return ("X", "O") if marker == "X" else ("O", "X")

def place_marker(marker, position):
    board[position] = marker

    return board

def win_check(mark):
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

def space_check(position):
    return True if board[position] == " " else False

def full_board_check():
    return False if " " in board else True

from IPython.display import clear_output
import socket
import sys
import time
import re

# setting up sockets
init_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = None
connection = None

ip_address_mask = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

print(f"Setting up connection...\n")

host = input(f"Please input the host connection: ")

# setting up server address, can now input custom IP addresses and custom ports
while not (re.search(ip_address_mask, host) or host == "localhost"):
    host = input(f"\nInvalid IP Address. Please input a valid host IP Address: ")
# host = "localhost"

print()

port = input("Please input a port from 0 to 65535: ")
# port = 8080

while not (port.isnumeric() and int(port) >= 0 and int(port) <= 65535):
    port = input("\nCannot have an alpha character in the port or invalid port. Please input a port from 0 to 65535: ")

port = int(port)
print()

# check existing connection/s
check_connection = init_sock.connect_ex((host, port))

currentPlayer = 0

if (check_connection == 0): # there is a socket connection already
    print(f"Connecting...\n")
    currentPlayer = 2
    sock = init_sock
else: # no socket was opened, thus first player who opened the file becomes the server
    print(f"Establishing connection...\n")
    currentPlayer = 1
    init_sock.close()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

board = [" "," "," "," "," "," "," "," "," "]
print(f"Welcome to TicTacToe!\n")
gameState = True

currentInput = ""

if (currentPlayer == 1):
    # initialize the server
    sock.bind((host, port))
    sock.listen(0)

    print(f"Waiting for an opponent...\n")

    connection, client = sock.accept()

    print(f"Someone has finally challenged you to a game of TicTacToe!\n")

    # receive what input you will have based on Player 2's input
    input_bytes = connection.recv(1)
    p1_input = input_bytes.decode("utf-8")
    print(f"You will use {p1_input} for this game!\n")

    p2_input = "X" if p1_input == "O" else "O"

    currentInput = p1_input # set current input for Player 1
    firstInstance = True # on the first instance [turn], the server won't receive anything first        

else:
    print(f"You have finally connected to the server! Are you ready for a game of TicTacToe?\n")

    # ask Player 2 what mark he/she wants
    set_tuple = player_input()
    print()

    # setting inputs for both players occur on the client side
    p2_input = set_tuple[0]
    print(f"You will use {p2_input} for this game!\n")
    sock.sendall(set_tuple[1].encode("utf-8")) # give player one his/her input

    p1_input = "X" if p2_input == "O" else "O"
    
    currentInput = p2_input # set current input for Player 2

while(gameState):
    if (currentPlayer == 1):
        # get last input from Player 2, if it's at least Player 1's second turn
        if(not firstInstance):
            p2_last_input = connection.recv(1)

            if p2_last_input:
                p2_last_position = p2_last_input.decode("utf-8")
                # place Player 1's input
                board = place_marker(p2_input, int(p2_last_position)-1)
                # display Player 1's input
                print(f"Player 2\'s last input:")
                display_board()

            # check if Player 2 has won already
            if (win_check(p2_input)):
                print(f"Player 2 has won the game. Good luck next time!")
                break
    else:
        # get last input from Player 1
        p1_last_input = sock.recv(1)

        if p1_last_input:
            p1_last_position = p1_last_input.decode("utf-8")
            # place Player 1's input
            board = place_marker(p1_input, int(p1_last_position)-1)
            # display Player 1's input
            print(f"Player 1\'s last input:")
            display_board()

            # check if Player 1 has won already
            if (win_check(p1_input)):
                print(f"Player 1 has won the game. Good luck next time!")
                break

    draw_game_string = f"The board is already full! Nobody wins or loses, thus it is considered a draw."

    # check if the board is full before proceeding; this block is mainly for if the player is receiving/waiting
    if(full_board_check()):
        print(draw_game_string)
        break
    
    # this happens if it's the player's turn
    inputting = True

    while(inputting):
        input_string = f"Player {currentPlayer}, give a position from 1-9 on where to put {currentInput}: "

        position = input(input_string)

        # input validation for choosing a position
        while not (position.isnumeric() and int(position) >= 1 and int(position) <= 9):
            print()
            position = input(input_string)

        # the logic happening in this block will happen if it's the player's turn
        # check first if the player can put a mark on that specific position player inputted
        # if player inputs a valid position, it will then update the status of the game
        # else, the player is asked to give another position instead
        if (space_check(int(position)-1)):
            board = place_marker(currentInput, int(position)-1)
            print(f"\nCurrent Status of the Board:")
            display_board()

            send_position = position.encode("utf-8")

            # check if you have won locally
            if(win_check(currentInput)):
                print(f"Congratulations Player {currentPlayer} for winning the game!")
                connection.sendall(send_position) if currentPlayer == 1 else sock.sendall(send_position)
                gameState = False
                break

            # check if game is a draw locally; if not switch turns
            if(full_board_check()):
                print(draw_game_string)
                connection.sendall(send_position) if currentPlayer == 1 else sock.sendall(send_position)
                gameState = False
                break
            else:
                if (currentPlayer == 1):
                    firstInstance = False
                connection.sendall(send_position) if currentPlayer == 1 else sock.sendall(send_position)
                print(f"Now waiting for other player\'s input...\n")
                inputting = False
        else:
            print(f"\nPosition has been already taken with element: {board[int(position)-1]}\n")
            inputting = inputting #restart the loop

# put quick timeout after winning the game
time.sleep(2)

# close socket when game is over
connection.close() if currentPlayer == 1 else sock.close()