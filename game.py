import numpy as np

class Game(object):
    def __init__(self, m: int, n: int, k: int):
        self.board = np.zeros((m, n), dtype = np.byte)
        self.m, self.n = m, n
        self.k = k
        self.slices = [] # contains lists of lists of coordinate pairs corresponding to the board sliced vertically, horizontally and diagonally (twice).
        self.slice(m, n, k)
        self.winner = -1

    def __repr__(self):
        return self.board.__repr__()

    def is_over(self) -> bool:
        return self.is_full() or self.is_won()
    
    def is_full(self) -> bool:
        shape = self.board.shape
        return len(np.flatnonzero(self.board)) == shape[0] * shape[1] # as many nonzero fields as existing fields

    def is_won(self) -> bool:
        for slice in self.slices:
            pieces = [0 for _ in range(self.k)]
            p1 = 0
            p2 = 0
            i = 0
            for x, y in slice:
                if pieces[i] == 1:
                    p1 -= 1
                if pieces[i] == 2:
                    p2 -= 1
                match self.board[y, x]:
                    case 1:
                        p1 += 1
                        pieces[i] = 1
                    case 2:
                        p2 += 1
                        pieces[i] = 2
                    case 0:
                        pieces[i] = 0
                if p1 == self.k:
                    self.winner = 1
                    return True
                if p2 == self.k:
                    self.winner = 2
                    return True
                
                i = (i + 1) % self.k
        
        return False

    def place(self, x: int, y: int, player: int) -> bool:
        if self.board[y, x] != 0:
            raise IndexError(f"Illegal move! ({x},{y}) is already occupied by player {self.board[y, x]}!")
            return False
        elif x < 0 or x >= self.n or y < 0 or y >= self.m:
            raise IndexError(f"Illegal move! ({x},{y}) is out of bounds for the board of shape {self.board.shape}!")
        else:
            self.board[y, x] = player

    def slice(self, m: int, n: int, k: int) -> None:
        slices = []

        v = []
        if n >= k:
            for y in range(m):
                col = []
                for x in range(n):
                    col.append((x, y))
                v.append(col)
        
        h = []
        if m >= k:
            for x in range(n):
                row = []
                for y in range(m):
                    row.append((x, y))
                h.append(row)
        
        d1 = [] # top left to bottom right
        #if m >= k and n >= k:
        #    for i in range(-(m - k), 0):
        if m >= k and n >= k:
            x, y = 0, m - k
            while y > 0:
                x_, y_ = x, y
                dia = []
                while x_ < n and y_ < m:
                    dia.append((x_, y_))
                    x_ += 1
                    y_ += 1
                d1.append(dia)
                y -= 1
            while x <= n - k:
                x_, y_ = x, y
                dia = []
                while x_ < n and y_ < m:
                    dia.append((x_, y_))
                    x_ += 1
                    y_ += 1
                d1.append(dia)
                x += 1

        d2 = [] # bottom left to top right
        if m >= k and n >= k:
            x, y = 0, k - 1
            while y < m - 1:
                x_, y_ = x, y
                dia = []
                while x_ < n and y_ >= 0:
                    dia.append((x_, y_))
                    x_ += 1
                    y_ -= 1
                d2.append(dia)
                y += 1
            while x <= n - k:
                x_, y_ = x, y
                dia = []
                while x_ < n and y_ >= 0:
                    dia.append((x_, y_))
                    x_ += 1
                    y_ -= 1
                d2.append(dia)
                x += 1
        
        self.slices.extend(v)
        self.slices.extend(h)
        self.slices.extend(d1)
        self.slices.extend(d2)

    

if __name__ == "__main__":
    pass