from dialogue import get_character, get_next_move
from src.announcements import announcements
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
        character_selection_complete = False
        while not character_selection_complete:
            selected_character = get_character()
            self.game.request_first_character(selected_character)
            character_selection_complete = self.game.is_valid_characters_selected()

    def get_player_moves(self):
        while self.is_playing:
            current_player = self.game.get_current_player()
            move = get_next_move(current_player)
            self.game.handle_move(move)
            print(self.game.get_board())
            if self.game.is_won():
                self.win(announcements.winner)
            if self.game.is_draw():
                self.draw(announcements.draw)

    def play(self):
        self.get_player_characters()
        self.get_player_moves()
