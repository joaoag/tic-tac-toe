from src.board import Board
from src.dialogue import (
    get_character,
    get_next_move,
    announce_winner,
    announce_character_selection,
    announce_invalid_character_selection,
    announce_invalid_move_selection,
    announce_draw,
)
from src.constants import GameConstants


class BoardFullException(Exception):
    pass


class Game:
    def __init__(self, board: Board):
        self._taken_moves = set()
        self._board = board
        self._play_order = {1: "", 2: ""}
        self._current_player = ""
        self._winner = None
        self._draw = False

    def _get_remaining_moves(
        self, all_moves: set[str] = GameConstants.ALL_CELLS
    ) -> set:
        remaining_moves = all_moves - self._taken_moves
        return remaining_moves

    def _is_available_cell(self, move) -> bool:
        remaining_moves = self._get_remaining_moves()
        is_available = move in remaining_moves
        return is_available

    def _is_valid_cell(self, move: str) -> bool:
        is_valid_cell = move.isdigit() and move in GameConstants.ALL_CELLS
        if is_valid_cell:
            return is_valid_cell
        else:
            announce_invalid_move_selection(move)
            return is_valid_cell

    def _is_move_playable(self, move: str) -> bool:
        is_playable = self._is_valid_cell(move) and self._is_available_cell(move)
        return is_playable

    def _get_move(self):
        move = get_next_move(self._current_player)
        if self._is_move_playable(move):
            self._move_and_switch_players(int(move))

    def move_selection(self):
        is_being_played = True
        while is_being_played:
            self._get_move()
            print(self._board.get_board())
            if self._is_won():
                announce_winner(self._winner)
                is_being_played = False
            if self._is_draw():
                announce_draw()
                is_being_played = False

    def character_selection(self):
        while not self._request_first_character():
            self._request_first_character()

    def _implement_play_order(self, first_character: str):
        self._set_play_order(first_character)
        self._set_current_player(first_character)
        announce_character_selection(
            first_player=self._play_order[1], second_player=self._play_order[2]
        )

    def _request_first_character(self) -> bool:
        first_character = get_character()
        is_valid_selection = first_character in GameConstants.VALID_CHARACTERS

        if is_valid_selection:
            self._implement_play_order(first_character)
            return is_valid_selection
        else:
            announce_invalid_character_selection(first_character)
            return is_valid_selection

    def _set_play_order(self, first_character: str):
        second_character = (
            GameConstants.NOUGHT
            if first_character == GameConstants.CROSS
            else GameConstants.CROSS
        )
        self._play_order = {1: first_character, 2: second_character}

    def _get_play_order(self) -> dict:
        return self._play_order

    def _is_space_on_board(self):
        moves_so_far = self._count_moves()
        self._validate_count(moves_so_far)

    def _validate_count(self, count: int):
        if count == GameConstants.MAXIMUM_MOVES:
            raise BoardFullException("Sorry, the board is full so the game is over")

    def _get_winner(self) -> str | None:
        return self._winner

    def _set_winner(self, winner: str):
        self._winner = winner

    def _is_won(self) -> bool:
        return bool(self._get_winner())

    def _is_draw(self) -> bool:
        return self._draw

    def _cells_contain_win(self, cell_entries: set[str]) -> bool:
        winning_sequence_for_x = cell_entries == {GameConstants.CROSS}
        winning_sequence_for_o = cell_entries == {GameConstants.NOUGHT}
        return winning_sequence_for_x or winning_sequence_for_o

    def _check_for_winner(self, move_count: int):
        if move_count >= GameConstants.EARLIEST_WINNING_MOVE:
            for sequence in GameConstants.WINNING_SEQUENCES:
                cell_entries = self._board.get_cells(sequence)
                if self._cells_contain_win(cell_entries):
                    winner = cell_entries.pop()
                    self._set_winner(winner)

    def _apply_move(self, position: int):
        self._is_space_on_board()  # TODO unsure if this is needed any more
        self._taken_moves.add(position)
        self._board.update_board(self._current_player, position)

    def _move_and_switch_players(self, position: int):
        self._apply_move(position)

        move_count = self._count_moves()
        self._check_for_winner(move_count)
        if self._is_won():
            return  # TODO do we need this early return? Could we bundle two into check_win_or_draw()

        if self._count_moves() >= GameConstants.MAXIMUM_MOVES and not self._is_won():
            self._set_is_draw(True)

        self._switch_players(move_count)

    def _set_is_draw(self, is_draw: bool):
        self._draw = is_draw

    def _switch_players(self, current_move: int):
        end_of_first_player_turn = current_move % 2 != 0
        if end_of_first_player_turn:
            self._set_current_player(self._play_order[2])
        else:
            self._set_current_player(self._play_order[1])

    def _set_current_player(self, player):
        self._current_player = player

    def _get_current_player(self):
        return self._current_player

    def _get_moves(self) -> set[int]:
        return self._taken_moves

    def _count_moves(self) -> int:
        return len(self._get_moves())
