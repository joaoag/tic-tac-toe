class Game:

    def __init__(self):
        self.moves = []
        self.begin_game()

    def begin_game(self):
        move = self.prompt()
        self.add_move(move)

    def prompt(self) -> int:
        next_move = int(input("Please enter your move"))
        return next_move

    def add_move(self, position):
        self.moves.append(position)

    def get_moves(self):
        return self.moves



