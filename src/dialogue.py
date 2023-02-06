def get_next_move(current_player) -> str:
    next_move = input(f"{current_player}, please enter your move\n")
    return next_move


def get_character() -> str:
    first_character = input("Please enter player one's character: X or O\n")
    first_character_cleaned = first_character.strip()
    return first_character_cleaned
