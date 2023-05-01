from dataclasses import dataclass


def announce(announcement, *format_args):
    print(announcement.format(*format_args))


@dataclass(frozen=True)
class Announcements:
    WINNER = "{} has won the game!"
    DRAW = "It's a draw!"
    CHARACTER_SELECTION = "Player 1 has chosen {}\nPlayer 2 will be {}"
    UNAVAILABLE_MOVE = "Your move needs to be one of the empty cells, but you selected '{}'"
    INVALID_MOVE = "Your move needs to be a number from 1 to 9, but you selected '{}'"
    INVALID_CHARACTER = "Your character needs to be 'X' or 'O', but you selected '{}'."
