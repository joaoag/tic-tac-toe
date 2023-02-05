from dialogue import announce_winner, announce_draw
from src.game import Game


class Play:
    def __init__(self, game: Game):
        self.game = game

    def get_player_characters(self):
        while not self.game.request_first_character():
            self.game.request_first_character()

    def get_player_moves(self):
        is_being_played = True
        while is_being_played:
            self.game._get_move()
            print(self.game._board.get_board())
            if self.game._is_won():
                announce_winner(self.game._get_winner())
                is_being_played = False
            if self.game._is_draw():
                announce_draw()
                is_being_played = False

    def play(self):
        self.get_player_characters()
        self.get_player_moves()
