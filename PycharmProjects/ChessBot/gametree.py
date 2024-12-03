
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

    def minimax(self, position, half_move, depth):
        if depth == 0:
            return position.evaluate()
        position.addLegalPositions()
        candidate_moves = position.legal_positions

        evals = []
        for move in candidate_moves:
            evals.append(self.minimax(move, half_move + 1, depth - 1))

        if half_move % 2 == 1:
            if evals:
                return max(evals)
            else:
                return -1000
        else:
            if evals:
                return min(evals)
            else:
                return 1000


