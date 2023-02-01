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


def test_board_can_be_filled_with_noughts_and_crosses():
    expected = """
  X  |  X  |  X  
-----|-----|-----
  X  |  O  |  O  
-----|-----|-----
  O  |  O  |  O  
"""
    board = Board()
    for n in range(1, 5):
        board.update_board("X", n)
    for n in range(5, 10):
        board.update_board("O", n)

    actual = board.get_board()
    assert expected == actual
