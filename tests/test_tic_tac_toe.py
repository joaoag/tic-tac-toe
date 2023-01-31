from io import StringIO


def test_tic_tac_toe_stores_user_input(monkeypatch):
    first_move = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', first_move)
    assert game.get_first_move == 1