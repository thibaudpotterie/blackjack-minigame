import random
import json
import pathlib


def get_cards() -> dict[int, str]:
    """
    Load card names from the metadata JSON file.
    Returns a dictionary mapping integer values to card names.
    """
    metadata_path = pathlib.Path(__file__).parent / "data" / "card_metadata.json"
    try:
        with open(metadata_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {card["value"]: card["name"] for card in data["cards"]}
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        # Fallback to string representation if file is missing or invalid
        return {i: str(i) for i in range(1, 14)}


CARD_NAMES = get_cards()


def get_card() -> int:
    """Returns a random card value between 1 and 13 (Ace to King)."""
    return random.randint(1, 13)


def play_turn(current_card: int) -> tuple[bool, int]:
    """
    Executes a single game turn: displays the current card, gets a user guess,
    and returns if the guess was correct along with the next card.
    """
    print(f"\nCurrent card: {CARD_NAMES.get(current_card, current_card)}")
    guess = input("Will the next card be higher(h) or lower(l)? ").strip().lower()

    next_card = get_card()
    print(f"Next card was: {CARD_NAMES.get(next_card, next_card)}")

    is_higher = guess == "h" and next_card > current_card
    is_lower = guess == "l" and next_card < current_card

    return is_higher or is_lower, next_card


def main() -> None:
    """Main game loop for the Higher or Lower Blackjack-style game."""
        print( "Welcome to Higher or Lower Blackjack!" )
    print("Cards from Ace to King will be displayed and you have to guess if "
          "the next card is higher or lower.")
    print("If you guess correctly, you get a point. Good luck!")

    while True:
        score = 0
        current_card = get_card()

        while True:
            won, next_card = play_turn(current_card)
            if won:
                score += 1
                print(f"Correct! Your current score: {score}")
                current_card = next_card
            else:
                print(f"Wrong! Game Over. Final Score: {score}")
                break

        if input("\nDo you want to play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing! See you next time.")
            break


if __name__ == "__main__":
    main()
