import copy
from pieces import PieceSets


class Board:
    legal_positions = []

    def __init__(self, current_position):
        self.legal_positions = []
        self.current_position = current_position

    def generatePosition(self, current_position, start_row, start_col, end_row, end_col, promotion=""):
        new_position = copy.deepcopy(current_position)
        if promotion == "":
            new_position[end_row][end_col] = current_position[start_row][start_col]
        else:
            new_position[end_row][end_col] = promotion
        new_position[start_row][start_col] = "0"
        return new_position

    def printBoard(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                print(f"{board[i][j]}", end=" ")
            print()

    def printLegalPositions(self):
        for position in self.legal_positions:
            self.printBoard(position)
            print()
            print()

    def canMove(self, start_row, start_col, end_row, end_col, capture=False):  # capture=True used for pawn capture
        if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
            return False
        taker = self.current_position[start_row][start_col]
        takee = self.current_position[end_row][end_col]
        required_upper = True
        if taker.isupper():
            required_upper = False
        if takee == "0":
            if not capture:
                return True
        else:
            if takee.isupper() == required_upper:
                return True
        return False


    def attacking(self, position, row, col):  # returns a list of positions that a piece can move to (to capture)
        attacking = []
        path = [[row, col], [row, col], [row, col], [row, col], [row, col], [row, col], [row, col], [row, col]]
        move = [True, True, True, True, True, True, True, True]
        if position[row][col] == "R":
            while move[0] or move[1] or move[2] or move[3]:
                path[0][0] += 1
                path[1][0] -= 1
                path[2][1] += 1
                path[3][1] -= 1
                for i in range(0, 4):
                    if move[i]:
                        if self.canMove(row, col, path[i][0], path[i][1]):
                            attacking.append(path[i][0], path[i][1])
                            if not position[path[i][0]][path[i][1]] == "0":
                                move[i] = False
                        else:
                            move[i] = False


    def findLegalPositions(self, position, turn, castle_W_Q=True, castle_W=True, castle_B_Q=True, castle_B=True):
        for row in range(0, 8):
            for col in range(0, 8):
                if turn == 1:  # white's turn
                    if position[row][col] == "P":
                        if row > 0:
                            if position[row - 1][col] == "0":
                                if row != 1:
                                    new_position = self.generatePosition(position, row, col, row - 1, col)
                                    self.legal_positions.append(new_position)
                                if row == 1:
                                    for piece in PieceSets.white_promotions:
                                        new_position = self.generatePosition(position, row, col, row - 1, col, piece)
                                        self.legal_positions.append(new_position)
                            if row == 6:  # pawn can move two squares here
                                if position[row - 1][col] == "0" and position[row - 2][col] == "0":
                                    new_position = self.generatePosition(position, row, col, row - 2, col)
                                    self.legal_positions.append(new_position)
                            if col > 0:
                                if self.canMove(row, col, row - 1, col - 1, True):
                                    if row != 1:
                                        new_position = self.generatePosition(position, row, col, row - 1, col - 1)
                                        self.legal_positions.append(new_position)
                                    if row == 1:
                                        for piece in PieceSets.white_promotions:
                                            new_position = self.generatePosition(position, row, col, row - 1, col - 1,
                                                                                 piece)
                                            self.legal_positions.append(new_position)

                            if col < 7:
                                if self.canMove(row, col, row - 1, col + 1, True):
                                    if row != 1:
                                        new_position = self.generatePosition(position, row, col, row - 1, col - 1)
                                        self.legal_positions.append(new_position)
                                    if row == 1:
                                        for piece in PieceSets.white_promotions:
                                            new_position = self.generatePosition(position, row, col, row - 1, col + 1,
                                                                                 piece)
                                            self.legal_positions.append(new_position)

                    if position[row][col] == "R":
                        path = [[row, col], [row, col], [row, col], [row, col]]
                        move = [True, True, True, True]
                        while move[0] or move[1] or move[2] or move[3]:
                            path[0][0] += 1
                            path[1][0] -= 1
                            path[2][1] += 1
                            path[3][1] -= 1
                            for i in range(0, 4):
                                if move[i]:
                                    if self.canMove(row, col, path[i][0], path[i][1]):
                                        new_position = self.generatePosition(position, row, col, path[i][0], path[i][1])
                                        self.legal_positions.append(new_position)
                                        if not position[path[i][0]][path[i][1]] == "0":
                                            move[i] = False
                                    else:
                                        move[i] = False

                        # TODO rook movement

                    if position[row][col] == "N":
                        return
                        # TODO knight movement

                    if position[row][col] == "B":
                        return
                        # TODO bishop movement

                    if position[row][col] == "Q":
                        return
                        # TODO queen movement

                    if position[row][col] == "K":
                        return
                        # TODO king movement
                if turn == 0:  # black's turn
                    if position[row][col] == "p":
                        return
                        # TODO pawn movement

                    if position[row][col] == "r":
                        return
                        # TODO rook movement

                    if position[row][col] == "n":
                        return
                        # TODO knight movement

                    if position[row][col] == "b":
                        return
                        # TODO bishop movement

                    if position[row][col] == "q":
                        return
                        # TODO queen movement

                    if position[row][col] == "k":
                        return
                        # TODO king movement
