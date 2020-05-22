import numpy as np
import random
# --------------


def create_board():
    board = np.zeros((3, 3), dtype=int)
    print(f'board 1: \n {board}')
    return board


def place(board, player, position):
    x = board[position]
    if x == 0:
        board[position] = player
    else:
        print("This place is not empty. Try a new position!")
    print(f'board 2: \n {board}')
    return board


def possibilities(board):
    positions = np.array(np.where(board == 0))
    positions_list = list(zip(positions[0], positions[1]))
    print(f'positions_list 2: \n {positions_list}')
    return positions_list


def random_place(board, player):
    positions_list = possibilities(board)
    random_selection = np.random.choice(len(positions_list))
    print(f'random_selection: \n {random_selection}')
    board[positions_list[random_selection]] = player
    print(f'board 3: \n {board}')
    return board


board = create_board()
place(board, 1, (0, 0))
possibilities(board)
random_place(board, 2)
