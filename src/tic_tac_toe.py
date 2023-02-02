from src.game import Game
from src.board import Board


def main():
    board = Board()
    game = Game(board)

    game.character_selection()
    game.move_selection()


if __name__ == "__main__":
    main()
