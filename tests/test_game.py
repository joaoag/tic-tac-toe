from io import StringIO
from unittest.mock import MagicMock
import pytest

from src.game import Game, BoardFullException


def test_game_allows_no_more_than_nine_moves():
    game = Game(MagicMock)

    for n in range(1, 10):
        game.add_move(n)

    with pytest.raises(
        BoardFullException, match="Sorry, the board is full so the game is over"
    ):
        game.add_move(4)


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

    expected_state = {1: '', 2: ''}
    expected_message = "Sorry, that's not a valid character, you must pick X or O"

    actual_message = game.request_first_character()
    actual_state = game._get_play_order()

    assert expected_state == actual_state
    assert expected_message == actual_message


def test_game_alternates_players(monkeypatch):
    players_input = StringIO("X\n9\n3\n")
    monkeypatch.setattr("sys.stdin", players_input)
    game = Game(MagicMock)
    game.request_first_character()  # player chooses X

    expected_first_turn = "X"
    expected_second_turn = "0"
    expected_third_turn = "X"

    actual_first_turn = game._get_current_player()
    game.get_move()
    actual_second_turn = game._get_current_player()
    game.get_move()
    actual_third_turn = game._get_current_player()

    assert expected_first_turn == actual_first_turn
    assert expected_second_turn == actual_second_turn
    assert expected_third_turn == actual_third_turn
