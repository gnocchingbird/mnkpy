from game import Game
from player import Player

class Session(object):
    def __init__(self, p1: Player, p2: Player, p1_first: bool, m: int = 3, n: int = 3, k: int = 3, drop_pieces: bool = False, headless: bool = True):
        self.p1 = p1
        self.p2 = p2
        self.turn = 1 if p1_first else 2
        self.game = Game(m, n, k)
        self.move_num = 1
        self.drop_pieces = drop_pieces
        self.headless = headless

    def __repr__(self):
        return f"Game between {self.p1} and {self.p2}:\n{self.game}"

    def new_game(self, p1_first: bool, m: int = 3, n: int = 3, k: int = 3, drop_pieces: bool = False):
        self.game = Game(m, n, k)
        self.turn = 1 if p1_first else 2
        self.move_num = 1
        self.drop_pieces = drop_pieces

    def parse_move(self, inp: str) -> tuple:
        if self.drop_pieces:
            return int(inp.split(",")[0].strip(" ")) - 1
        x, y = inp.split(",")
        x = int(x.strip(" ")) - 1
        y = int(y.strip(" ")) - 1
        return (x, y)
    
    def prompt_move_(self):
        if self.headless:
            if self.drop_pieces:
                match self.turn:
                    case 1:
                        return self.parse_move(input(f"{self.move_num}:\t{self.p1}'s move (x):\n"))
                    case 2:
                        return self.parse_move(input(f"{self.move_num}:\t{self.p2}'s move (x):\n"))
            match self.turn:
                case 1:
                    return self.parse_move(input(f"{self.move_num}:\t{self.p1}'s move (x,y):\n"))
                case 2:
                    return self.parse_move(input(f"{self.move_num}:\t{self.p2}'s move (x,y):\n"))
        # else call for corresponding player's ip
    
    def prompt_move(self):
        illegal = True
        while illegal:
            if self.drop_pieces:
                x, y = self.prompt_move_(), -1
            else:
                x, y = self.prompt_move_()
            try:
                if self.drop_pieces:
                    y_ = self.game.m - 1
                    while y_ >= 0:
                        if self.game.board[y_, x] == 0:
                            y = y_
                            break
                        y_ -= 1
                self.game.place(x, y, self.turn)
                illegal = False
            except IndexError:
                pass

        self.turn = 1 if self.turn == 2 else 2
        self.move_num += 1
    
    def loop(self, print_board: bool = True):
        print(f"Starting game...")
        if print_board:
            print(self.game)

        while not self.game.is_over():
            self.prompt_move()
            if print_board:
                print(self.game)

        if self.game.winner == -1:
            print("Game over! It's a draw...")
        else:
            print(f"Game over! {self.p1 if self.game.winner == 1 else self.p2} wins!")

        if input("New game (y/n)? ").strip(" ") == "y":
            self.new_game(False)
            self.loop()
                
            


    
if __name__ == "__main__":
    s = Session(Player("nick"), Player("george"), True, 3, 5, 3, True)
    print(s)
    s.loop()