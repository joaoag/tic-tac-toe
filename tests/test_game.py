from io import StringIO
from unittest.mock import patch
import pytest

from src.game import Game, BoardFullException


@patch("src.board.Board")
def test_game_allows_no_more_than_nine_moves(mock_board):
    game = Game(mock_board)

    for n in range(1, 10):
        game._move_and_switch_players(n)

    with pytest.raises(
        BoardFullException, match="Sorry, the board is full so the game is over"
    ):
        game._move_and_switch_players(4)


@patch("src.board.Board")
def test_game_gets_and_saves_players_characters(mock_board, monkeypatch):
    first_player_choice = StringIO("O\n")
    monkeypatch.setattr("sys.stdin", first_player_choice)
    game = Game(mock_board)
    game.request_first_character()
    expected_order = {1: "O", 2: "X"}
    actual_order = game._get_play_order()
    assert expected_order == actual_order


@patch("src.board.Board")
def test_game_only_allows_player_to_choose_x_or_o(mock_board, monkeypatch):
    first_player_choice = StringIO("A\n")
    monkeypatch.setattr("sys.stdin", first_player_choice)
    game = Game(mock_board)

    expected_state = {1: "", 2: ""}
    expected_return_value = False

    actual_return_value = game.request_first_character()
    actual_state = game._get_play_order()

    assert expected_state == actual_state
    assert expected_return_value == actual_return_value


@patch("src.board.Board")
def test_game_alternates_players(mock_board, monkeypatch):
    players_input = StringIO("X\n9\n3\n")
    monkeypatch.setattr("sys.stdin", players_input)
    game = Game(mock_board)
    game.request_first_character()  # player chooses X

    expected_first_turn = "X"
    expected_second_turn = "O"
    expected_third_turn = "X"

    actual_first_turn = game._get_current_player()
    game.handle_move()
    actual_second_turn = game._get_current_player()
    game.handle_move()
    actual_third_turn = game._get_current_player()

    assert expected_first_turn == actual_first_turn
    assert expected_second_turn == actual_second_turn
    assert expected_third_turn == actual_third_turn


@patch("src.board.Board")
def test_game_identifies_win(mock_board, monkeypatch):
    mock_board.get_cells.return_value = {"X"}
    players_input = StringIO("X")
    monkeypatch.setattr("sys.stdin", players_input)
    x_o_moves_with_x_win = [1, 9, 2, 8]

    game = Game(mock_board)
    game.request_first_character()
    for move in x_o_moves_with_x_win:
        game._move_and_switch_players(move)

    expected = "X"
    game._move_and_switch_players(3)  # winning move for X
    actual = game.get_winner()
    assert expected == actual


@patch("src.board.Board")
def test_game_identifies_draw(mock_board, monkeypatch):
    players_input = StringIO("X")
    monkeypatch.setattr("sys.stdin", players_input)
    x_o_moves_with_draw = [1, 2, 3, 4, 6, 5, 7, 9, 8]

    game = Game(mock_board)
    game.request_first_character()
    for move in x_o_moves_with_draw:
        game._move_and_switch_players(move)

    expected = True
    actual = game.is_draw()

    assert expected == actual


@pytest.mark.parametrize("valid_input", [1, 2, 3, 4, 5, 6, 7, 8, 9])
@patch("src.board.Board")
def test_game_accepts_valid_cells(mock_board, valid_input):
    expected = True
    game = Game(mock_board)
    actual = game._is_valid_cell(valid_input)
    assert expected == actual


@pytest.mark.parametrize("invalid_input", ["A", "?", "22", "four", "O", "", "-", "0"])
@patch("src.board.Board")
def test_game_rejects_invalid_cells(mock_board, invalid_input):
    expected = False
    game = Game(mock_board)
    actual = game._is_valid_cell(invalid_input)
    assert expected == actual


@patch("src.board.Board")
def test_game_rejects_moves_onto_populated_cells(mock_board, monkeypatch):
    players_input = StringIO("X")
    monkeypatch.setattr("sys.stdin", players_input)
    first_player_first_move = 1
    game = Game(mock_board)

    game.request_first_character()
    game._move_and_switch_players(first_player_first_move)

    expected = False
    actual = game._is_available_cell(first_player_first_move)
    assert expected == actual
