# Tic Tac Toe Game
# Author: Laura Fry      Date: Dec 1, 2022

# Imports
import random
from gameFunctions import print_game_board, check_board, check_for_winner, player_make_placement, swap_player_turn


# Main Menu
def main():
    print()
    print("********************************")
    print("Welcome to the Tic Tac Toe Game!")
    print("********************************")
    print()
    firstPlayerName = input("Please enter the first player's name: ").title()
    print("First player will be X's")
    secondPlayerName = input("Please enter the second player's name: ").title()
    print("Second player will be O's")

    playerList = ["X", "O"]
    turn = random.choice(playerList)
    global firstPlayer
    global secondPlayer
    if turn == "X":
        firstPlayer = "X"
        secondPlayer = "O"
    elif turn == "O":
        firstPlayer = "O"
        secondPlayer = "X"

    print()
    print("We will randomly decide who goes first....", turn + "'s !")
    print()
    gameBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("Time to play:")

    for i in range(9):
        print_game_board(gameBoard)
        print()
        print(turn + "'s it is your turn:")
        print()
        userRowSelection = int(input("Enter the row number you would like to select: "))
        userColumnSelection = int(input("Enter the column number you would like to select: "))
        player_make_placement(userRowSelection, userColumnSelection, gameBoard, turn)

        if check_for_winner(gameBoard, turn) == True:
            print(turn + "'s Win!")
            print()
            break
        elif check_board(gameBoard) == True:
            print("Draw!!!")
            print()
            break
        else:
            print("Continue...")
            turn = swap_player_turn(turn)
            continue

    print_game_board(gameBoard)
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
