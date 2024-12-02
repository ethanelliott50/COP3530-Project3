class PieceSets:
    white_pieces = ["P", "N", "B", "Q", "R", "K"]
    white_promotions = ["N", "B", "Q", "R"]
    black_pieces = ["p", "n", "b", "q", "r", "k"]
    black_promotions = ["n", "b", "q", "r"]

    # note that the empty piece has a value of zero, as well as the king (king is calculated seperately)
    piece_values = {"P": 1, "N": 3, "B": 3.25, "Q": 9, "K": 0, "R": 5, "p": -1, "n": -3, "b": -3.25, "q": -9, "k": 0,
                    "r": -5, "0": 0}

    # e.g. a white knight on a3 is worth 0.7 of its piece value.
    N_W_values = [[0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70],
                  [0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80],
                  [0.75, 0.80, 0.90, 0.90, 0.90, 0.90, 0.80, 0.70],
                  [0.70, 0.80, 0.90, 1.00, 1.00, 0.90, 0.80, 0.70],
                  [0.70, 0.80, 0.90, 1.00, 1.00, 0.90, 0.80, 0.70],
                  [0.70, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.70],
                  [0.65, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
                  [0.60, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.60]]