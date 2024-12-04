import numpy as np
import tensorflow as tf
import misc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

def run():
    # Neural net
    model = Sequential([
        Conv2D(64, (3, 3), activation='relu', input_shape=(8, 8, 12)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(1, activation='linear')
    ])
    
    # Compile
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    
    def encode_board(board):
        encoded_board = np.zeros((8, 8, 12))
        piece_to_index = {
            'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5,
            'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11
        }
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != '0':
                    encoded_board[i, j, piece_to_index[piece]] = 1
        return encoded_board
    
    def generate_chess_data():
        fens = ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
                "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR",
                "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR",
                "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R",
                "rnbqkbnr/ppp2ppp/3p4/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R",
                "rnbqkbnr/ppp2ppp/3p4/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R",
                "rn1qkbnr/ppp2ppp/3p4/4p3/3PP1b1/5N2/PPP2PPP/RNBQKB1R",
                "rn1qkbnr/ppp2ppp/3p4/4P3/4P1b1/5N2/PPP2PPP/RNBQKB1R",
                "rn1qkbnr/ppp2ppp/3p4/4P3/4P3/5b2/PPP2PPP/RNBQKB1R",
                "rn1qkbnr/ppp2ppp/3p4/4P3/4P3/5Q2/PPP2PPP/RNB1KB1R",
                "rn1qkbnr/ppp2ppp/8/4p3/4P3/5Q2/PPP2PPP/RNB1KB1R",
                "rn1qkbnr/ppp2ppp/8/4p3/2B1P3/5Q2/PPP2PPP/RNB1K2R",
                "rn1qkb1r/ppp2ppp/5n2/4p3/2B1P3/5Q2/PPP2PPP/RNB1K2R",
                "rn1qkb1r/ppp2ppp/5n2/4p3/2B1P3/1Q6/PPP2PPP/RNB1K2R",
                "rn2kb1r/ppp1qppp/5n2/4p3/2B1P3/1Q6/PPP2PPP/RNB1K2R",
                "rn2kb1r/ppp1qppp/5n2/4p3/2B1P3/1QN5/PPP2PPP/R1B1K2R",
                "rn2kb1r/pp2qppp/2p2n2/4p3/2B1P3/1QN5/PPP2PPP/R1B1K2R",
                "rn2kb1r/pp2qppp/2p2n2/4p1B1/2B1P3/1QN5/PPP2PPP/R3K2R",
                "rn2kb1r/p3qppp/2p2n2/1p2p1B1/2B1P3/1QN5/PPP2PPP/R3K2R",
                "rn2kb1r/p3qppp/2p2n2/1N2p1B1/2B1P3/1Q6/PPP2PPP/R3K2R",
                "rn2kb1r/p3qppp/5n2/1p2p1B1/2B1P3/1Q6/PPP2PPP/R3K2R",
                "rn2kb1r/p3qppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/R3K2R",
                "r3kb1r/p2nqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/R3K2R",
                "r3kb1r/p2nqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/2KR3R",
                "3rkb1r/p2nqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/2KR3R",
                "3rkb1r/p2Rqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/2K4R",
                "4kb1r/p2rqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/2K4R",
                "4kb1r/p2rqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/2KR4",
                "4kb1r/p2r1ppp/4qn2/1B2p1B1/4P3/1Q6/PPP2PPP/2KR4",
                "4kb1r/p2B1ppp/4qn2/4p1B1/4P3/1Q6/PPP2PPP/2KR4",
                "4kb1r/p2n1ppp/4q3/4p1B1/4P3/1Q6/PPP2PPP/2KR4",
                "1Q2kb1r/p2n1ppp/4q3/4p1B1/4P3/8/PPP2PPP/2KR4",
                "1n2kb1r/p4ppp/4q3/4p1B1/4P3/8/PPP2PPP/2KR4",
                "1n1Rkb1r/p4ppp/4q3/4p1B1/4P3/8/PPP2PPP/2K5"]
        scores = [0.2, 0.2, 0.2, 0.1, 0.5, 0.6, 1.0, 0.9, 1.4, 1.3, 1.5, 1.7,
                  2.0, 2.3, 2.3, 1.9, 1.9, 1.9, 3.3, 3.4, 5.3, 5.5, 5.5, 5.7,
                  5.8, 5.8, 6.0, 5.8, 9.3, 10.4, 100, 100, 100, 999]
        boards = [encode_board(misc.FENtoArr(fen)) for fen in fens]
        return np.array(boards), np.array(scores)
    
    X_train, Y_train = generate_chess_data()
    model.fit(X_train, Y_train, epochs=10, batch_size=32)
    
    # Save weights
    model.save_weights('chess_model.weights.h5')
