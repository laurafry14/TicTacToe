# Game Functions:

# Print game board
def print_game_board(gameBoard):
    print("  " + gameBoard[0] + "  |  " + gameBoard[1] + "  |  " + gameBoard[2] + "  \n"
          "-----------------\n"
          "  " + gameBoard[3] + "  |  " + gameBoard[4] + "  |  " + gameBoard[5] + "  \n"
          "-----------------\n"
          "  " + gameBoard[6] + "  |  " + gameBoard[7] + "  |  " + gameBoard[8] + "  \n")


# Function to check whether or not the board is filled out.
def check_board(gameBoard):
    if gameBoard[0] == " ":
        return False
    elif gameBoard[1] == " ":
        return False
    elif gameBoard[2] == " ":
        return False
    elif gameBoard[3] == " ":
        return False
    elif gameBoard[4] == " ":
        return False
    elif gameBoard[5] == " ":
        return False
    elif gameBoard[6] == " ":
        return False
    elif gameBoard[7] == " ":
        return False
    elif gameBoard[8] == " ":
        return False
    else:
        return True


# Function to check whether a player has won or not.
def check_for_winner(gameBoard, turn):
    # Check for horizontal line.
    if gameBoard[0] == turn and gameBoard[1] == turn and gameBoard[2] == turn:
        return True
    elif gameBoard[3] == turn and gameBoard[4] == turn and gameBoard[5] == turn:
        return True
    elif gameBoard[6] == turn and gameBoard[7] == turn and gameBoard[8] == turn:
        return True

    # Check for vertical line.
    elif gameBoard[0] == turn and gameBoard[3] == turn and gameBoard[6] == turn:
        return True
    elif gameBoard[1] == turn and gameBoard[4] == turn and gameBoard[7] == turn:
        return True
    elif gameBoard[2] == turn and gameBoard[5] == turn and gameBoard[8] == turn:
        return True

    # Check for diagonal line.
    elif gameBoard[0] == turn and gameBoard[4] == turn and gameBoard[8] == turn:
        return True
    elif gameBoard[2] == turn and gameBoard[4] == turn and gameBoard[6] == turn:
        return True

    # If no winner found
    else:
        return False


def player_make_placement(userRowSelection, userColumnSelection, gameBoard, playerTurn):
    # Top left placement:
    if userRowSelection == 1 and userColumnSelection == 1:
        gameBoard[0] = playerTurn
        print_game_board(gameBoard)
    # Top middle placement:
    elif userRowSelection == 1 and userColumnSelection == 2:
        gameBoard[1] = playerTurn
        print_game_board(gameBoard)
    # Top left placement:
    elif userRowSelection == 1 and userColumnSelection == 3:
        gameBoard[2] = playerTurn
        print_game_board(gameBoard)
    # Middle left placement:
    elif userRowSelection == 2 and userColumnSelection == 1:
        gameBoard[3] = playerTurn
        print_game_board(gameBoard)
    # Middle placement:
    elif userRowSelection == 2 and userColumnSelection == 2:
        gameBoard[4] = playerTurn
        print_game_board(gameBoard)
    # Middle right placement:
    elif userRowSelection == 2 and userColumnSelection == 3:
        gameBoard[5] = playerTurn
        print_game_board(gameBoard)
    # Bottom left placement:
    elif userRowSelection == 3 and userColumnSelection == 1:
        gameBoard[6] = playerTurn
        print_game_board(gameBoard)
    # Bottom middle placement:
    elif userRowSelection == 3 and userColumnSelection == 2:
        gameBoard[7] = playerTurn
        print_game_board(gameBoard)
    # Bottom right placement:
    elif userRowSelection == 3 and userColumnSelection == 3:
        gameBoard[8] = playerTurn
        print_game_board(gameBoard)

def swap_player_turn(turn):
    if turn == "X":
        return "O"
    else:
        return "X"