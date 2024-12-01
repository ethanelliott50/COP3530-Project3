import copy
from pieces import PieceSets


class Board:
    legal_positions = []
    current_position = []

    def __init__(self, current_position):
        self.legal_positions = []
        self.current_position = current_position

    def generatePosition(self, start_row, start_col, end_row, end_col, promotion=""):
        new_position = []
        for row in self.current_position:
            new_position.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
        if promotion == "":
            new_position[end_row][end_col] = self.current_position[start_row][start_col]
        else:
            new_position[end_row][end_col] = promotion
        new_position[start_row][start_col] = "0"
        return new_position

    def printBoard(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                print(f"{board[i][j]}", end=" ")
            print()
        print()

    def printLegalPositions(self):
        for position in self.legal_positions:
            self.printBoard(position)
            print()

    def inCheck(self, position, white_turn):    # e.g. white_turn == True looks for white king in check
        for row in range(0, 8):
            for col in range(0, 8):
                if position[row][col] != "0":
                    if white_turn != position[row][col].isupper():
                        new_coordinates = self.attacking(position, row, col)
                        for square in new_coordinates:
                            if white_turn:
                                if position[square[0]][square[1]] == "K":
                                    return True
                            if not white_turn:
                                if position[square[0]][square[1]] == "k":
                                    return True
        return False

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

    # returns a list of positions that a piece can move to (to capture)
    # each position is a list: ordered pair (row, col)
    def attacking(self, position, row, col):
        if position[row][col] == "0":
            return []
        attacking = []
        path = [[row, col], [row, col], [row, col], [row, col], [row, col], [row, col], [row, col], [row, col]]
        move = [True, True, True, True, True, True, True, True]
        if position[row][col] == "P" or position[row][col] == "p":
            if position[row][col].islower():
                pawn_direction = 1
            else:
                pawn_direction = -1
            if col > 0:
                if self.canMove(row, col, row + pawn_direction, col - 1, True):
                    attacking.append([row + pawn_direction, col - 1])
            if col < 7:
                if self.canMove(row, col, row + pawn_direction, col + 1, True):
                    attacking.append([row + pawn_direction, col + 1])

        if position[row][col] == "R" or position[row][col] == "r":
            while move[0] or move[1] or move[2] or move[3]:
                path[0][0] += 1
                path[1][0] -= 1
                path[2][1] += 1
                path[3][1] -= 1
                for i in range(0, 4):
                    if move[i]:
                        if self.canMove(row, col, path[i][0], path[i][1]):
                            attacking.append([path[i][0], path[i][1]])
                            if not position[path[i][0]][path[i][1]] == "0":
                                move[i] = False
                        else:
                            move[i] = False

        if position[row][col] == "B" or position[row][col] == "b":
            while move[4] or move[5] or move[6] or move[7]:
                path[4][0] += 1
                path[4][1] += 1
                path[5][0] -= 1
                path[5][1] -= 1
                path[6][0] += 1
                path[6][1] -= 1
                path[7][0] -= 1
                path[7][1] += 1
                for i in range(4, 8):
                    if move[i]:
                        if self.canMove(row, col, path[i][0], path[i][1]):
                            attacking.append([path[i][0], path[i][1]])
                            if not position[path[i][0]][path[i][1]] == "0":
                                move[i] = False
                        else:
                            move[i] = False

        if position[row][col] == "Q" or position[row][col] == "q":
            while move[0] or move[1] or move[2] or move[3] or move[4] or move[5] or move[6] or move[7]:
                path[0][0] += 1
                path[1][0] -= 1
                path[2][1] += 1
                path[3][1] -= 1
                path[4][0] += 1
                path[4][1] += 1
                path[5][0] -= 1
                path[5][1] -= 1
                path[6][0] += 1
                path[6][1] -= 1
                path[7][0] -= 1
                path[7][1] += 1
                for i in range(0, 8):
                    if move[i]:
                        if self.canMove(row, col, path[i][0], path[i][1]):
                            attacking.append([path[i][0], path[i][1]])
                            if not position[path[i][0]][path[i][1]] == "0":
                                move[i] = False
                        else:
                            move[i] = False

        if position[row][col] == "N" or position[row][col] == "n":
            path[0][0] += 1
            path[0][1] += 2
            path[1][0] += 1
            path[1][1] -= 2
            path[2][0] -= 1
            path[2][1] += 2
            path[3][0] -= 1
            path[3][1] -= 2
            path[4][0] += 2
            path[4][1] += 1
            path[5][0] += 2
            path[5][1] -= 1
            path[6][0] -= 2
            path[6][1] += 1
            path[7][0] -= 2
            path[7][1] -= 1

            for i in range(0, 8):
                if self.canMove(row, col, path[i][0], path[i][1]):
                    attacking.append([path[i][0], path[i][1]])

        if position[row][col] == "K" or position[row][col] == "k":
            path[0][0] += 1
            path[1][0] -= 1
            path[2][1] += 1
            path[3][1] -= 1
            path[4][0] += 1
            path[4][1] += 1
            path[5][0] -= 1
            path[5][1] -= 1
            path[6][0] += 1
            path[6][1] -= 1
            path[7][0] -= 1
            path[7][1] += 1

            for i in range(0, 8):
                if self.canMove(row, col, path[i][0], path[i][1]):
                    attacking.append([path[i][0], path[i][1]])
        return attacking

    def findLegalPositions(self, position, white_turn=True, castle_W_Q=True, castle_W=True, castle_B_Q=True, castle_B=True):
        for row in range(0, 8):
            for col in range(0, 8):
                if white_turn:  # white's turn
                    if position[row][col] == "P":
                        if row > 0:
                            if position[row - 1][col] == "0":
                                if row != 1:
                                    new_position = self.generatePosition(row, col, row - 1, col)
                                    if not self.inCheck(new_position, white_turn):
                                        self.legal_positions.append(new_position)
                                if row == 1:
                                    for piece in PieceSets.white_promotions:
                                        new_position = self.generatePosition(row, col, row - 1, col, piece)
                                        if not self.inCheck(new_position, white_turn):
                                            self.legal_positions.append(new_position)
                            if row == 6:  # pawn can move two squares here
                                if position[row - 1][col] == "0" and position[row - 2][col] == "0":
                                    new_position = self.generatePosition(row, col, row - 2, col)
                                    if not self.inCheck(new_position, white_turn):
                                        self.legal_positions.append(new_position)
                if white_turn == position[row][col].isupper():
                    new_coordinates = self.attacking(position, row, col)
                    for square in new_coordinates:
                        new_position = self.generatePosition(row, col, square[0], square[1])
                        if not self.inCheck(new_position, white_turn):
                            self.legal_positions.append(new_position)


