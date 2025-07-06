import numpy as np


class Game(object):
    def __init__(self, n: int, m: int, k: int):
        self.board = np.zeros((n, m), dtype = np.byte)
        self.k = k

    def __repr__(self):
        return self.board.__repr__()
    
    def is_full(self):
        shape = self.board.shape
        return len(np.flatnonzero(self.board)) == shape[0] * shape[1] # as many nonzero fields as existing fields

    

if __name__ == "__main__":
    game = Game(1, 1, 3)
    game.board[0, 0] = 1
    print(game.is_full())
    print(game)
