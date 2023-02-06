from src.board import Board


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


def test_board_updates_correctly_after_each_move():
    expected_board_after_first_go = """
  X  |     |     
-----|-----|-----
     |     |     
-----|-----|-----
     |     |     
"""
    board = Board()
    board.update_board("X", 1)

    actual_board_after_first_go = board.get_board()

    board.update_board("O", 6)
    expected_board_after_second_go = """
  X  |     |     
-----|-----|-----
     |     |  O  
-----|-----|-----
     |     |     
"""
    actual_board_after_second_go = board.get_board()

    assert expected_board_after_first_go == actual_board_after_first_go
    assert expected_board_after_second_go == actual_board_after_second_go
