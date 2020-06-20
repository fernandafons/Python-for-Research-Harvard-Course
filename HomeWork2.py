import numpy as np
import random
# --------------


def create_board():
    """Creates a board with the value of each cell set to the integer 0."""

    board = np.zeros((3, 3), dtype=int)
    return board


def place(board, player, position):
    """Player is the current player (an integer 1 or 2).
        Position is a tuple of length 2 specifying a desired location to place their marker."""

    if board[position] == 0:
        board[position] = player
        return board


def possibilities(board):
    """Returns a list of all positions (tuples) on the board that are not occupied (0). """

    return list(zip(*np.where(board == 0)))


def random_place(board, player):
    """Places a marker for the current player at random among all the available positions"""

    positions_list = possibilities(board)
    if len(positions_list) > 0:
        random_selection = random.choice(positions_list)
        place(board, player, random_selection)
    return board


def row_win(board, player):
    if np.any(np.all(board == player, axis=1)):
        return True
    else:
        return False


def col_win(board, player):
    if np.any(np.all(board == player, axis=0)):
        return True
    else:
        return False


def diag_win(board, player):
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    else:
        return False


def evaluate(board):
    """Checks if some of the players won the game."""
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    # print(f"Player {winner} has won the game!")
    return winner


def play_game():
    """Play the complete game"""
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


def play_strategic_game():
    """Player one will always start with the middle square """
    board, winner = create_board(), 0
    board[1, 1] = 1
    while winner == 0:
        for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


random.seed(1)
results = [play_strategic_game() for i in range(1000)]
print(results.count(1))