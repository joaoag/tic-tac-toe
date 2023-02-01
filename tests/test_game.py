from io import StringIO
from unittest.mock import MagicMock
import pytest

from src.game import Game, BoardFullException


def test_game_stores_user_input(monkeypatch):
    first_move = StringIO("1\n")
    monkeypatch.setattr("sys.stdin", first_move)
    game = Game(MagicMock)
    game.begin_game()
    expected = [1]
    actual = game._get_moves()
    assert expected == actual


def test_game_only_allows_nine_moves():
    game = Game(MagicMock)
    game.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with pytest.raises(
        BoardFullException, match="Sorry, the board is full so the game is over"
    ):
        game.add_move(10)


