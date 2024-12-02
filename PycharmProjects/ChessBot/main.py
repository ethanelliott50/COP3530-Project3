# The sequence "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" describes the piece placement
# field of the starting position of a game of chess.
# this function determines all legal positions possible from a given postion
# it must take in the current position, whose turn it is as well as
    #1. whether white/black can still castle kingside/queenside
    #2. whether en passant is available for a given pair of pawns in the right spots\

# white_turn bool used to keep track of turn (false for balck's turn)

# TODO list:
# 1. make function that looks for checks (this function can be made more efficient; it need not check every square in
# the position but only what has changed in the last move)
# 2. en passant
# 3. castling
# 4. eval. function
# 5. Minimax

from constraints import Board
import constraints
import time
from datetime import timedelta


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


if __name__ == '__main__':
    fen = input()
    start_position = FENtoArr(fen)

    starttime = time.perf_counter()

    board_object = Board(start_position)
    print("START POSITION: ")
    board_object.printBoard(start_position)

    board_object.findLegalPositions(start_position, False)
    board_object.printLegalPositions()

    print(f"EVAL: {board_object.evaluate(start_position)}")
    duration = timedelta(seconds=time.perf_counter() - starttime)
    print('Job took: ', duration)
