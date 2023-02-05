from io import StringIO

from src.play import Play
from src.game import Game
from src.board import Board


def test_play_allows_game_to_be_won(monkeypatch):
    x_o_moves_with_x_win = ["1", "9", "2", "8", "3"]
    first_player_chooses_x = "X\n"
    player_input_for_x_win = "\n".join(x_o_moves_with_x_win)
    players_input = StringIO(f"{first_player_chooses_x}{player_input_for_x_win}")
    monkeypatch.setattr("sys.stdin", players_input)

    board = Board()
    game = Game(board)
    play = Play(game)
    play.play()

    expected_winner = "X"
    actual_winner = play.game.get_winner()
    assert expected_winner == actual_winner
