from src.play import Play
from src.game import Game
from src.board import Board


def main():
    board = Board()
    game = Game(board)
    play = Play(game)
    play.play()
