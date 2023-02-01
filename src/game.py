from board import Board


class BoardFullException(Exception):
    pass


MAXIMUM_MOVES = 9


class Game:
    def __init__(self, board: Board):
        self.moves = []
        self.board = board
        self.play_order = dict()
        self._current_player = ""

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
        self._set_current_player(first_character)

    def _set_play_order(self, first_character):
        second_character = "0" if first_character == "X" else "X"
        self.play_order = {1: first_character, 2: second_character}

    def _get_play_order(self) -> dict:
        return self.play_order

    def add_move(self, position):
        pre_turn_move_count = self._get_current_move()
        if pre_turn_move_count == MAXIMUM_MOVES:
            raise BoardFullException("Sorry, the board is full so the game is over")

        self.moves.append(position)
        post_turn_move_count = self._get_current_move()

        if post_turn_move_count % 2 == 0:
            self._set_current_player(self.play_order[2])

    def _set_current_player(self, player):
        self._current_player = player

    def _get_current_player(self):
        return self._current_player

    def _get_moves(self) -> list:
        return self.moves

    def count_moves(self) -> int:
        return len(self._get_moves())

    def _get_current_move(self) -> int:
        return len(self._get_moves()) + 1
