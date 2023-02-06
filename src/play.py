from typing import Callable

from src.constants import Constants
from src.dialogue import get_character, get_next_move
from src.announcements import announcements
from src.game import Game


class Play:
    def __init__(self, game: Game):
        self.game = game
        self._is_playing = True
        self._is_selecting_character = True

    def _get_is_playing(self) -> bool:
        return self._is_playing

    def _set_is_playing(self, is_playing: bool):
        self._is_playing = is_playing

    def _get_is_selecting_character(self) -> bool:
        return self._is_selecting_character

    def _set_is_selecting_character(self, is_selecting: bool):
        self._is_selecting_character = is_selecting

    def _win(self, win_announcement: Callable):
        win_announcement(self.game.get_winner())
        self._set_is_playing(False)

    def _draw(self, draw_announcement: Callable):
        draw_announcement()
        self._set_is_playing(False)

    def get_player_characters(self):
        while self._get_is_selecting_character():
            selected_character = get_character()
            is_valid_selection = self.game.handle_character_selection(
                selected_character
            )
            if not is_valid_selection:
                announcements.invalid_character_selection(selected_character)
            else:
                is_selecting = self.game.is_selecting_characters()
                play_order = self.game.get_play_order()
                announcements.characters_selection(
                    first_player=play_order[1], second_player=play_order[2]
                )
                self._set_is_selecting_character(is_selecting)

    def get_player_moves(self):
        while self._get_is_playing():
            current_player = self.game.get_current_player()
            move = get_next_move(current_player)
            move_status = self.game.handle_move(move)
            if move_status == Constants.INVALID_MOVE_TYPE:
                announcements.invalid_move_selection(move)

            if move_status == Constants.UNAVAILABLE_MOVE:
                announcements.unavailable_move(move)

            print(self.game.get_board())
            if self.game.is_won():
                self._win(announcements.winner)
            if self.game.is_draw():
                self._draw(announcements.draw)

    def play(self):
        self.get_player_characters()
        self.get_player_moves()
