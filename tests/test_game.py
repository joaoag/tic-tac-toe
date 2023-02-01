from io import StringIO
from unittest.mock import MagicMock
import pytest

from src.game import Game, BoardFullException


def test_game_only_allows_nine_moves():
    game = Game(MagicMock)
    game.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with pytest.raises(
        BoardFullException, match="Sorry, the board is full so the game is over"
    ):
        game.add_move(10)


def test_game_gets_and_saves_players_characters(monkeypatch):
    first_player_choice = StringIO("O\n")
    monkeypatch.setattr("sys.stdin", first_player_choice)
    game = Game(MagicMock)
    game.request_first_character()
    expected_order = {1: "O", 2: "X"}
    actual_order = game._get_play_order()
    assert expected_order == actual_order


def test_game_only_allows_player_to_choose_x_or_o(monkeypatch):
    first_player_choice = StringIO("A\n")
    monkeypatch.setattr("sys.stdin", first_player_choice)
    game = Game(MagicMock)

    expected_state = dict()
    expected_message = "Sorry, that's not a valid character, you must pick X or O"

    actual_message = game.request_first_character()
    actual_state = game._get_play_order()

    assert expected_state == actual_state
    assert expected_message == actual_message


def test_game_alternates_players(monkeypatch):
    first_move = StringIO("X\n9")
    monkeypatch.setattr("sys.stdin", first_move)
    game = Game(MagicMock)
    game.request_first_character()  # player chooses X

    expected_first_player = "X"
    expected_second_player = "0"

    actual_first_player = game._get_current_player()
    game.get_move()
    actual_second_player = game._get_current_player()

    assert expected_first_player == actual_first_player
    assert expected_second_player == actual_second_player
