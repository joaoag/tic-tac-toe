from board import Board


class BoardFullException(Exception):
    pass


MAXIMUM_MOVES = 9


class Game:
    def __init__(self, board: Board):
        self.moves = []
        self.board = board
        self.play_order = dict()

    def get_move(self):
        move = self.prompt()
        self.add_move(move)

    def prompt(self) -> int:
        next_move = int(input("Please enter your move"))
        return next_move

    def request_first_character(self) -> str | None:
        first_character = input("Please enter player one's character: X or O")
        first_character = first_character.strip().upper()
        if first_character not in ["X", "O"]:
            return "Sorry, that's not a valid character, you must pick X or O"

        self._set_play_order(first_character)

    def _set_play_order(self, first_character):
        second_character = "0" if first_character == "X" else "X"
        self.play_order = {1: first_character, 2: second_character}

    def _get_play_order(self) -> dict:
        return self.play_order

    def add_move(self, position):
        if self.count_moves() < MAXIMUM_MOVES:
            self.moves.append(position)
        else:
            raise BoardFullException("Sorry, the board is full so the game is over")

    def _get_moves(self) -> list:
        return self.moves

    def count_moves(self) -> int:
        return len(self._get_moves())
