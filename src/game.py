from board import Board


class BoardFullException(Exception):
    pass


MAXIMUM_MOVES = 9
WINNING_SEQUENCES = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
]


class Game:
    def __init__(self, board: Board):
        self.moves = []
        self.board = board
        self.play_order = {1: "", 2: ""}
        self._current_player = ""
        self._winner = ""

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

    def _is_space_on_board(self):
        moves_so_far = self._count_moves()
        self._validate_count(moves_so_far)

    def _validate_count(self, count: int):
        if count == MAXIMUM_MOVES:
            raise BoardFullException("Sorry, the board is full so the game is over")

    # def _is_winning_sequence(self, sequence: tuple):
    #     is_winning_sequence = all(entry == sequence[0] for entry in sequence)
    #     return is_winning_sequence

    def _is_won(self) -> bool:
        for sequence in WINNING_SEQUENCES:
            cell_entries = self.board.get_cells(sequence)
            if cell_entries == {"X"} or cell_entries == {"O"}:
                self._winner = cell_entries.pop()
                return True

    def add_move(self, position):
        self._is_space_on_board()
        self.moves.append(position)
        self.board.update_board(self._current_player, position)

        if self._is_won():
            return f"{self._winner} has won the game!"

        post_turn_move_count = self._get_current_move()
        self._switch_players(post_turn_move_count)

    def _switch_players(self, current_move):
        if current_move % 2 == 0:
            self._set_current_player(self.play_order[2])
        else:
            self._set_current_player(self.play_order[1])

    def _set_current_player(self, player):
        self._current_player = player

    def _get_current_player(self):
        return self._current_player

    def _get_moves(self) -> list:
        return self.moves

    def _count_moves(self) -> int:
        return len(self._get_moves())

    def _get_current_move(self) -> int:
        return len(self._get_moves()) + 1
