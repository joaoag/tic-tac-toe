def get_next_move(current_player) -> int:
    next_move = int(input(f"{current_player}, please enter your move\n"))
    return next_move


def get_character() -> str:
    first_character = input("Please enter player one's character: X or O\n")
    first_character_cleaned = first_character.strip().upper()
    return first_character_cleaned


def announce_invalid_character_selection(invalid_selection):
    print(f"You selected '{invalid_selection}', which is not a valid option")


def announce_character_selection(first_player, second_player):
    print(f"Player 1 has chosen {first_player}")
    print(f"Player 2 will be {second_player}")


def announce_winner(winner):
    print(f"{winner} has won the game!")
