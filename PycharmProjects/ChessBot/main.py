# The sequence "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" describes the piece placement
# field of the starting position of a game of chess.

# this function determines all legal positions possible from a given postion
# it must take in the current position, whose turn it is as well as
    #1. whether white/black can still castle kingside/queenside
    #2. whether en passant is available for a given pair of pawns in the right spots\

from constraints import Board

def inCheck(poition, turn):
    #TODO should return true if given player is in check
    return False


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

    board_object = Board(start_position)
    print("START POSITION: ")
    board_object.printBoard(start_position)
    print()
    board_object.findLegalPositions(board_object.current_position, 1)
    board_object.printLegalPositions()
