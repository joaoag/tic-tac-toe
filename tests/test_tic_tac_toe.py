from io import StringIO

import pytest

from tic_tac_toe import Game, BoardFullException


def test_game_stores_user_input(monkeypatch):
    first_move = StringIO("1\n")
    monkeypatch.setattr("sys.stdin", first_move)
    game = Game()
    game.begin_game()
    expected = [1]
    actual = game.get_moves()
    assert expected == actual


def test_game_only_allows_nine_moves():
    game = Game()
    game.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with pytest.raises(BoardFullException):
        game.add_move(10)
