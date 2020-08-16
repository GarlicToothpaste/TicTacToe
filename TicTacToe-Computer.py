# displaying the current status of the board
def display_board():
    clear_output()
    print(f"-------")
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"-------")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"-------")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print(f"-------")

# used by the computer to get all possible positions available
def get_possible_positions():
    return [x for x, e in enumerate(board) if e == " "]

# used for the easy difficulty
def cpu_position():
    empty_spaces = get_possible_positions()
    
    get_position = random.randint(0, len(empty_spaces) - 1)

    return empty_spaces[get_position] + 1

# input on determining player's and/or computer's mark
def marker_input():
    ask_string = " "

    if ((not isPlayingComputer) or (isPlayingComputer and not computerDifficulty == "hard")):
        ask_string = "Player 1 do you want to be X or O? "
    else:
        ask_string = "Player 2 do you want to be X or O? "

    mark = input(ask_string)

    while not (mark == "X" or mark == "O"):
        print()
        mark = input(ask_string)
        
    if(mark == "X"):
        return ("X", "O")
    else:
        return ("O", "X")

# player or computer input on which position will they put their mark in
def player_input():
    g_vars["position"] = input(f"Player {currentPlayer}, give a position from 1-9 on where to put {marking}: ")

    # this input validation here will solve the first issue in the repository
    while not (g_vars["position"].isnumeric() and int(g_vars["position"]) >= 1 and int(g_vars["position"]) <= 9):
        print()
        position = input(f"Player {currentPlayer}, give a position from 1-9 on where to put {marking}: ")

    print()

# placing the mark in a specific position
def place_marker(marker, position, checking, printing):
    board[position] = marker

    if printing:
        print(f"Current Status of the Board:")
        display_board()
        print()

    if(win_check(marker)):
        if (isPlayingComputer and g_vars["currentPlayer"] == aiPlayer):
            if printing:
                print(f"The computer has won the game! Good luck next time!")
        else:
            if printing:
                print(f"Congratulations Player {currentPlayer} for winning the game!")
        if checking:
            g_vars["gameState"] = False

    change_turn()

# remove mark in a specific position, used in the minimax method
def remove_marker(position):
    board[position] = " "

    change_turn()

# changing turns
def change_turn():
    if (g_vars["currentPlayer"] == 1):
        g_vars["currentPlayer"] = 2
        if isPlayingComputer and computerDifficulty == "hard":
            g_vars["marking"] = tup[0]
        else:
            g_vars["marking"] = tup[1]
    else:
        g_vars["currentPlayer"] = 1
        if isPlayingComputer and computerDifficulty == "hard":
            g_vars["marking"] = tup[1]
        else:
            g_vars["marking"] = tup[0]    

# check if player or computer has won based on their mark
def win_check(marker):
    condition_one = board[0] == marker and board[1] == marker and board[2] == marker # top row completed
    condition_two = board[3] == marker and board[4] == marker and board[5] == marker # middle row completed
    condition_three = board[6] == marker and board[7] == marker and board[8] == marker # bottom row completed

    condition_four = board[0] == marker and board[3] == marker and board[6] == marker # left column completed
    condition_five = board[1] == marker and board[4] == marker and board[7] == marker # middle column completed
    condition_six = board[2] == marker and board[5] == marker and board[8] == marker # right column completed

    condition_seven = board[0] == marker and board[4] == marker and board[8] == marker # upper-left corner to lower-right corner completed
    condition_eight = board[2] == marker and board[4] == marker and board[6] == marker # upper-right corner to lower-left corner completed

    conditions = [condition_one, condition_two, condition_three, condition_four, condition_five, condition_six, condition_seven, condition_eight]
    
    return any(conditions)

# check if player or computer can put their mark in a specific position
def space_check(position):
    return True if board[position]== " " else False

# check if the board is full
def full_board_check():
    return False if " " in board else True

# used for medium or hard difficulties
def get_best_position():
    bestScore = -math.inf
    bestPosition = 0

    for move in get_possible_positions():
        place_marker(g_vars["marking"], move, False, False)
        score = minimax(False, g_vars["marking"])
        remove_marker(move)
        if (score > bestScore):
            bestScore = score
            bestPosition = move
    
    return bestPosition + 1

# brute-force method, but can be improved via alpha-beta pruning
def minimax(isMaxTurn, mark):
    if (full_board_check()):
        return 0
    elif (win_check(mark)):
        return 1 if mark == tup[1] else -1

    scores = []

    for move in get_possible_positions():
        place_marker(g_vars["marking"], move, False, False)
        scores.append(minimax(not isMaxTurn, g_vars["marking"]))
        remove_marker(move)
        if (isMaxTurn and max(scores) == 1) or (not isMaxTurn and min(scores) == -1):
            break
    
    return max(scores) if isMaxTurn else min(scores)

# main program starts here
from IPython.display import clear_output

import math # used for easy difficulty
import random # used for easy difficulty
import time # used for timeout once game is done
import getpass # used for inputting Enter to exit the program

board = [" "," "," "," "," "," "," "," "," "] # initializing board

# setting up global variables
g_vars = {
    "gameState" : True,
    "currentPlayer" : 0,
    "marking" : None,
    "position" : ''
}

print(f"\nWelcome to TicTacToe!\n")
g_vars["gameState"] = True # game is starting

print(f"If you are playing with someone, input 1. If you are alone, you can face the computer by inputting 2.")
mode = ""

# input validation when inputting the mode of the game
while not (mode == "1" or mode == "2"):
    mode = input(f"What mode are you going to choose? ")
    print()

isPlayingComputer = True if mode == "2" else False
computerDifficulty = ""
aiPlayer = 0

# accepted values for the easy difficulty
easy_difficulty_values = ["easy", "ez"]

if isPlayingComputer:
    print(f"What difficulty of the computer do you want to select? Choose between Easy, Medium or Hard.")
    # input validation when inputting the difficulty for the computer
    while not (computerDifficulty in easy_difficulty_values or computerDifficulty == "medium" or computerDifficulty == "hard"):
        computerDifficulty = input(f"Input difficulty here: ").lower()
        print()

if (isPlayingComputer and (computerDifficulty in easy_difficulty_values or computerDifficulty == "medium")):
    print(f"Alright cool, Player 2 will be the computer then.\n")
elif isPlayingComputer and computerDifficulty == "hard":
    print(f"Alright cool, Player 1 will be the computer then.\n")

# setting markers
tup = marker_input()
print()

g_vars["currentPlayer"] = 1

# getting marker for the computer and which player is the computer
if (isPlayingComputer and computerDifficulty == "hard"):
    g_vars["marking"] = tup[1]
    aiPlayer = 1
else:
    g_vars["marking"] = tup[0]
    aiPlayer = 2

while (g_vars["gameState"]):
    marking = g_vars["marking"]
    currentPlayer = g_vars["currentPlayer"]

    if(full_board_check()):
        print(f"The board is already full! Nobody wins or loses, thus it is considered a draw.")
        gameState = False
        break
    else:

        if currentPlayer == 1:
            if isPlayingComputer and aiPlayer == currentPlayer:
                g_vars["position"] = get_best_position()
                print(f"Computer marks {marking} in square {g_vars['position']}!\n")
            else:
                player_input()
        else:
            if isPlayingComputer and aiPlayer == currentPlayer:
                if (computerDifficulty in easy_difficulty_values):
                    g_vars["position"] = cpu_position()
                else:
                    g_vars["position"] = get_best_position()
                print(f"Computer marks {marking} in square {g_vars['position']}!\n")
            else:
                player_input()

        if (space_check(int(g_vars["position"])-1)):
            place_marker(g_vars["marking"], int(g_vars["position"])-1, True, True)
        else:
            print(f"Position has been already taken with element: {board[int(g_vars['position'])-1]}\n")
            currentPlayer = currentPlayer # restart the loop

time.sleep(2) # reflect your moves...

# program will only stop if player presses Enter; any other keyboard presses will not show in the console
exit_input = getpass.getpass(f"\nPress Enter to exit...")
exit(0)