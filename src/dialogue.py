def get_next_move(current_player) -> str:
    next_move = input(f"{current_player}, please enter your move\n")
    return next_move


def get_character() -> str:
    first_character = input("Please enter player one's character: X or O\n")
    first_character_cleaned = first_character.strip().upper()
    return first_character_cleaned


def announce_invalid_character_selection(invalid_selection: str):
    print(f"You selected '{invalid_selection}', which is not a valid option")


def announce_character_selection(first_player: str, second_player:str):
    print(f"Player 1 has chosen {first_player}")
    print(f"Player 2 will be {second_player}")


def announce_winner(winner: str):
    print(f"{winner} has won the game!")


def announce_draw():
    print("It's a draw!")


def announce_invalid_move_selection(invalid_selection: str):
    print(
        f"Your move needs to be a number from 1-9, e.g. '5' but you selected '{invalid_selection}'"
    )


def announce_unavailable_move(unavailable_selection: int):

    print(
        f"Your move needs to be one of the empty cells, but you selected '{unavailable_selection}'"
    )
