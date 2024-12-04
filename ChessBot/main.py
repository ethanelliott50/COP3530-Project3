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
import misc
from gametree import GameTree


if __name__ == '__main__':
    misc.playComputer()













    duration = timedelta(seconds=time.perf_counter() - starttime)
    print('Job took: ', duration)
