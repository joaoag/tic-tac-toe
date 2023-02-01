from board import Board


class BoardFullException(Exception):
    pass


MAXIMUM_MOVES = 9


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

    def _get_moves(self) -> list:
        return self.moves

    def count_moves(self) -> int:
        return len(self._get_moves())
