import numpy as np
import random
# --------------

"""
In the following exercises, we will create a tic-tac-toe board, place markers on the board, 
evaluate if either player has won, and use this to simulate two basic strategies.
"""


def create_board():
    """Write a function that creates a board with the value of
        each cell set to the integer 0."""

    board = np.zeros((3, 3), dtype=int)
    return board


def place(board, player, position):
    """Create a function where player is the current player (an integer 1 or 2).
        Position is a tuple of length 2 specifying a desired location to place their marker."""

    x = board[position]
    if x == 0:
        board[position] = player
    else:
        print("This place is not empty.")
    return board


def possibilities(board):
    """Create a function that returns a list of all positions (tuples)
        on the board that are not occupied (0). """

    positions = np.array(np.where(board == 0))
    # print(positions)
    positions_list = list(zip(positions[0], positions[1]))
    return positions_list


def random_place(board, player):
    """Write a function that places a marker for the current
        player at random among all the available positions"""
    random.seed(1)
    positions_list = possibilities(board)
    if len(positions_list) > 0:
        random_selection = np.random.choice(len(positions_list))
        position = positions_list[random_selection-1]
        place(board, player, position)
    return board


# def row_win(board, player):



board = create_board()
print(f"board: {board}")
# place(board, 1, (0, 0))
possibilities(board)
x = 0
while x <3:
    random_place(board, 2)
    random_place(board, 1)
    x +=1
print(f"board: {board}")


"""TODO:
   
"""