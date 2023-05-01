from src.constants import Constants
from src.dialogue import request_character, request_next_move
from src.announcements import Announcements, announce
from src.game import Game


class Play:
    def __init__(self, game: Game):
        self.game: Game = game
        self._is_playing: bool = True
        self._is_selecting_character: bool = True

    def _win(self):
        announce(Announcements.WINNER, self.game.get_winner())
        self._is_playing = False

    def _draw(self):
        announce(Announcements.DRAW)
        self._is_playing = False

    def _select_characters(self):
        selected_character = request_character()
        is_valid_selection = self.game.handle_character_selection(selected_character)
        if not is_valid_selection:
            announce(Announcements.INVALID_CHARACTER, selected_character)

    def get_player_characters(self):
        while self._is_selecting_character:
            self._select_characters()
            is_selecting = self.game.is_selecting_characters()
            if not is_selecting:
                play_order = self.game.get_play_order()
                announce(Announcements.CHARACTER_SELECTION, play_order[1], play_order[2])
                self._is_selecting_character = is_selecting

    def _announce_invalid_move(self, move: str, move_status: str):
        if move_status == Constants.INVALID_MOVE_TYPE:
            announce(Announcements.INVALID_MOVE, move)

        if move_status == Constants.UNAVAILABLE_MOVE:
            announce(Announcements.UNAVAILABLE_MOVE, move)

    def _move(self):
        current_player = self.game.get_current_player()
        move = request_next_move(current_player)
        move_status = self.game.handle_move(move)
        if move_status in Constants.INVALID_MOVE_STATUSES:
            self._announce_invalid_move(move, move_status)

    def get_player_moves(self):
        while self._is_playing:
            self._move()
            print(self.game.get_board())

            if self.game.is_won():
                self._win()
            if self.game.is_draw():
                self._draw()

    def play(self):
        self.get_player_characters()
        self.get_player_moves()
