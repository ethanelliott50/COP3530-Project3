import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from constraints import Board
import misc

# Neural Net
model = Sequential([
    Conv2D(64, (3, 3), activation='relu', input_shape=(8, 8, 12)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')
])

# Load  weights
model.load_weights('chess_model.weights.h5')

def encode_board(board_2d):
    encoded_board = np.zeros((8, 8, 12))
    piece_to_index = {
        'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5,
        'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11
    }
    for i in range(8):
        for j in range(8):
            piece = board_2d[i][j]
            if piece != '0':
                encoded_board[i, j, piece_to_index[piece]] = 1
    return encoded_board

def evaluate_position(board):
    encoded_board = encode_board(board)
    encoded_board = np.expand_dims(encoded_board, axis=0)
    score = model.predict(encoded_board)[0][0]
    return score

def get_best_pos(board):
    board_object = Board(board)
    board_object.addLegalPositions()
    best_pos = None
    best_score = -float('inf')

    for pos in board_object.legal_positions:
        score = evaluate_position(pos.current_position)
        if score > best_score:
            best_score = score
            best_pos = pos.current_position

    return best_pos
    
def printBoard(board):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                print(f"{board[i][j]}", end=" ")
            print()

def best_pos(board):
    best_pos = get_best_pos(board)
    print("Best Pos:")
    printBoard(best_pos)
    
