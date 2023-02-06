from dataclasses import dataclass


@dataclass(frozen=True)
class Constants:
    EARLIEST_WINNING_MOVE = 5
    MAXIMUM_MOVES = 9
    WINNING_SEQUENCES = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    CROSS = "X"
    NOUGHT = "O"
    VALID_CHARACTERS = {CROSS, NOUGHT}
    ALL_MOVES = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    ALL_CELLS = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    VALID_MOVE = "valid"
    INVALID_MOVE_TYPE = "invalid"
    UNAVAILABLE_MOVE = "unavailable"
    INVALID_MOVE_STATUSES = [INVALID_MOVE_TYPE, UNAVAILABLE_MOVE]
