import math
from constraints import Board


class GameTree:
    def __init__(self, start_position, depth):
        self.root_position = Board(start_position, 1)
        self.root_position.addLegalPositions()
        self.depth = depth

    def make_move(self, new_position):

        self.root_position = new_position
        board_object = Board(new_position)
        board_object.findLegalPositions()

    def find_best_move(self):
        candidate_moves = []
        best_move = self.root_position.legal_positions[0]
        best_eval = self.minimax(best_move, self.root_position.half_move + 1, self.depth - 1)
        if self.root_position.half_move % 2 == 1:
            for move in self.root_position.legal_positions:
                new_eval = self.minimax(move, self.root_position.half_move + 1, self.depth - 1)
                if new_eval > best_eval:
                    best_move = move
                    best_eval = new_eval
        else:
            for move in self.root_position.legal_positions:
                new_eval = self.minimax(move, self.root_position.half_move + 1, self.depth - 1)
                if new_eval < best_eval:
                    best_move = move
                    best_eval = new_eval
        best_move.printBoard()
        return best_move

def minimax(self, position, half_move, depth, alpha=-math.inf, beta=math.inf):    # Alpha-Beta Pruning Included for Faster Performance. See below for previous minimax.
    if depth == 0:
        return position.evaluate()
    position.addLegalPositions()
    candidate_moves = position.legal_positions

    if half_move % 2 == 1:
        max_eval = -math.inf
        for move in candidate_moves:
            eval = self.minimax(move, half_move + 1, depth - 1, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in candidate_moves:
            eval = self.minimax(move, half_move + 1, depth - 1, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

    # def minimax(self, position, half_move, depth):
    #     if depth == 0:
    #         return position.evaluate()            This stays the same with the alpha-beta update.
    #     position.addLegalPositions()
    #     candidate_moves = position.legal_positions

    #     evals = []                                New minimax uses recursion to find the maximum value instead of finding the max in an array of evals.
    #     for move in candidate_moves:
    #         evals.append(self.minimax(move, half_move + 1, depth - 1)) 

    #     if half_move % 2 == 1:                    New minimax uses pruning to eliminate paths that would not be optimal immediately.
    #         if evals:
    #             return max(evals)
    #         else:
    #             return -1000
    #     else:
    #         if evals:
    #             return min(evals)
    #         else:
    #             return 1000


