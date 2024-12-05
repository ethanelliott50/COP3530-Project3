
from gametree import GameTree
from constraints import Board
import time
from datetime import timedelta
import ml
import train

def FENtoArr(fen_string):
    board = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            row.append("0")
        board.append(row)
    curr_row = 0
    curr_col = 0
    for char in fen_string:
        if not char.isdigit() and char != "/":
            board[curr_row][curr_col] = char
            curr_col += 1
        if char.isdigit():
            curr_col += int(char)
        if char == "/":
            curr_col = 0
            curr_row += 1
    return board


def playComputer(board, computer_type, depth, white):
    if computer_type == "1":
        game_tree = GameTree(board.current_position, depth, white)
        best_pos = game_tree.find_best_move()
        board.current_position = best_pos.current_position
        best_pos.printBoard
    elif computer_type == "2":
        best_pos = ml.get_best_pos(board.current_position)
        board.current_position = best_pos
        board.printBoard()

def move(input, board):
    if ord(input[0]) > 96 and ord(input[0]) < 105 and input[0] != 98:
        board.current_position = board.generatePosition(8 - int(input[1]), ord(input[0]) - 97, 8 - int(input[3]), ord(input[2]) - 97, "")
    else:
        board.current_position = board.generatePosition(8 - int(input[2]), ord(input[1]) - 97, 8 - int(input[5]), ord(input[4]) - 97, "")
