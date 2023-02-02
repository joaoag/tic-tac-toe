from src.board import Board
from src.dialogue import (
    get_character,
    get_next_move,
    announce_winner,
    announce_character_selection,
    announce_invalid_character_selection,
)
from src.constants import (
    EARLIEST_WINNING_MOVE,
    MAXIMUM_MOVES,
    WINNING_SEQUENCES,
    VALID_CHARACTERS,
    NOUGHT,
    CROSS,
)


class BoardFullException(Exception):
    pass


class Game:
    def __init__(self, board: Board):
        self.moves = []
        self.board = board
        self.play_order = {1: "", 2: ""}
        self._current_player = ""
        self._winner = ""

    def get_move(self):
        move = get_next_move(self._current_player)
        self.move_and_switch_players(move)

    def move_selection(self):
        is_being_played = True
        while is_being_played:
            self.get_move()
            print(self.board.get_board())
            if self._winner:
                announce_winner(self._winner)
                is_being_played = False

    def character_selection(self):
        while not self.request_first_character():
            self.request_first_character()

    def _implement_play_order(self, first_character: str):
        self._set_play_order(first_character)
        self._set_current_player(first_character)
        announce_character_selection(
            first_player=self.play_order[1], second_player=self.play_order[2]
        )

    def request_first_character(self) -> bool:
        first_character = get_character()
        is_valid_selection = first_character in VALID_CHARACTERS

        if is_valid_selection:
            self._implement_play_order(first_character)
            return is_valid_selection
        else:
            announce_invalid_character_selection(first_character)
            return is_valid_selection

    def _set_play_order(self, first_character):
        second_character = NOUGHT if first_character == CROSS else CROSS
        self.play_order = {1: first_character, 2: second_character}

    def _get_play_order(self) -> dict:
        return self.play_order

    def _is_space_on_board(self):
        moves_so_far = self._count_moves()
        self._validate_count(moves_so_far)

    def _validate_count(self, count: int):
        if count == MAXIMUM_MOVES:
            raise BoardFullException("Sorry, the board is full so the game is over")

    def _get_winner(self) -> str | None:
        return self._winner

    def _set_winner(self, winner):
        self._winner = winner

    def _is_won(self) -> bool:
        return bool(self._get_winner())

    def _check_for_winner(self, move_count):
        if move_count >= EARLIEST_WINNING_MOVE:
            for sequence in WINNING_SEQUENCES:
                cell_entries = self.board.get_cells(sequence)
                if cell_entries == {CROSS} or cell_entries == {NOUGHT}:
                    winner = cell_entries.pop()
                    self._set_winner(winner)

    def _apply_move(self, position):
        self._is_space_on_board()
        self.moves.append(position)
        self.board.update_board(self._current_player, position)

    def move_and_switch_players(self, position):
        self._apply_move(position)

        move_count = self._count_moves()
        self._check_for_winner(move_count)
        if self._is_won():
            return

        self._switch_players(move_count)

    def _switch_players(self, current_move):
        end_of_first_player_turn = current_move % 2 != 0
        if end_of_first_player_turn:
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
