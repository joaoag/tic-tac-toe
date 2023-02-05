from dialogue import announce_winner, announce_draw
from src.game import Game


class Play:
    def __init__(self, game: Game):
        self.game = game
        self.is_playing = True

    def win(self, win_announcement):
        win_announcement(self.game.get_winner())
        self.is_playing = False

    def draw(self, draw_announcement):
        draw_announcement()
        self.is_playing = False

    def get_player_characters(self):
        while not self.game.request_first_character():
            self.game.request_first_character()

    def get_player_moves(self):
        while self.is_playing:
            self.game.get_move() #should a game get a move?...
            print(self.game.get_board())
            if self.game.is_won():
                self.win(announce_winner)
            if self.game.is_draw():
                self.draw(announce_draw)

    def play(self):
        self.get_player_characters()
        self.get_player_moves()
