
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


def playComputer(computer_type,depth=4,play_as="white"):
    start_board = FENtoArr("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    game_tree = GameTree(start_board, depth)
    game_tree.root_position.printBoard()
    while True:
        if play_as == "white":
            start_row = int(input())
            start_col = int(input())
            end_row = int(input())
            end_col = int(input())

            starttime = time.perf_counter()
            new_board = game_tree.root_position.generatePosition(start_row, start_col, end_row, end_col)
            game_tree.root_position = Board(new_board, game_tree.root_position.half_move + 1)

            game_tree.root_position.addLegalPositions()
            if computer_type == "1":
                computer_move = game_tree.find_best_move()
            if computer_type == "2":
                computer_move = ml.get_best_pos(new_board)

            game_tree.root_position = computer_move
            computer_move.printBoard()
            duration = timedelta(seconds=time.perf_counter() - starttime)
            print("Thought for", duration, "seconds")
