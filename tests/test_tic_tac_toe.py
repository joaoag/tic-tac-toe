from io import StringIO

from tic_tac_toe import Game


def test_tic_tac_toe_stores_user_input(monkeypatch):
    first_move = StringIO("1\n")
    monkeypatch.setattr("sys.stdin", first_move)
    game = Game()
    game.begin_game()
    expected = [1]
    actual = game.get_moves()
    assert expected == actual
