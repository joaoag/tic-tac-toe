from collections import namedtuple

Announcements = namedtuple(
    "Announcements",
    [
        "invalid_character_selection",
        "invalid_move_selection",
        "unavailable_move",
        "characters_selection",
        "winner",
        "draw",
    ],
)

announcements = Announcements(
    lambda invalid_character: print(
        f"You selected '{invalid_character}', which is not a valid option. Valid characters are 'X' and 'O'"
    ),
    lambda invalid_move: print(
        f"Your move needs to be a number from 1-9, e.g. '5' but you selected '{invalid_move}'"
    ),
    lambda unavailable_move: print(
        f"Your move needs to be one of the empty cells, but you selected '{unavailable_move}'"
    ),
    lambda first_player, second_player: print(
        f"Player 1 has chosen {first_player}\nPlayer 2 will be {second_player}"
    ),
    lambda winner: print(f"{winner} has won the game!"),
    lambda: print("It's a draw!"),
)
