from board import Board


def test_board_shows_player_the_board():
    board = Board()

    expected = """
     |     |     
-----|-----|-----
     |     |     
-----|-----|-----
     |     |     
"""
    actual = board.get_board()
    assert expected == actual


def test_board_can_be_updated():
    expected = """
     |     |     
-----|-----|-----
     |  X  |     
-----|-----|-----
     |     |     
"""
    board = Board()
    board.update_board("X", 5)
    actual = board.get_board()
    assert expected == actual
