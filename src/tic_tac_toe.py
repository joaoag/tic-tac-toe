class BoardFullException(Exception):
    pass


MAXIMUM_MOVES = 9


class Board:
    boundary = "\n"
    y_dividers = "     |     |     \n"
    xy_dividers = "-----|-----|-----\n"

    def __init__(self):
        self.board_rows = [
            self.boundary,
            self.y_dividers,
            self.xy_dividers,
            self.y_dividers,
            self.xy_dividers,
            self.y_dividers,
            self.boundary,
        ]

    def get_board_rows(self):
        return self.board_rows

    def get_board(self):
        board = "".join(self.get_board_rows())
        return board


class Game:
    def __init__(self, board: Board):
        self.moves = []
        self.board = board

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
