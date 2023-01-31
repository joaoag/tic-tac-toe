class BoardFullException(Exception):
    pass


MAXIMUM_MOVES = 9


class Game:
    def __init__(self):
        self.moves = []

    def begin_game(self):
        move = self.prompt()
        self.add_move(move)

    def prompt(self) -> int:
        next_move = int(input("Please enter your move"))
        return next_move

    def add_move(self, position):
        if self.count_moves() < MAXIMUM_MOVES:
            self.moves.append(position)
        else:
            raise BoardFullException("Sorry, the board is full so the game is over")

    def get_moves(self):
        return self.moves

    def count_moves(self):
        return len(self.get_moves())


if __name__ == "__main__":
    game = Game()
    game.begin_game()
