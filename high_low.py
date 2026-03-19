import random


def get_card() -> int:
    """Returns a random card value between 1 and 11."""
    return random.randint(1, 11)


def play_turn(current: int) -> tuple[bool, int]:
    """
    Prompts the user for a guess and compares the current card with the next.
    Returns a tuple of (bool: is_correct, int: next_card).
    """
    print(f"\nCurrent card: {current}")
    guess = input("Next card higher(h) or lower(l)? ").strip().lower()
    nxt = get_card()
    print(f"Next card: {nxt}")
    is_correct = (guess == "h" and nxt > current) or (guess == "l" and nxt < current)
    return is_correct, nxt


def main() -> None:
    """Orchestrates the High-Low game rounds and score tracking."""
    print("Welcome to High-Low Blackjack!")
    while True:
        score, current = 0, get_card()
        while True:
            won, current = play_turn(current)
            if not won:
                break
            score += 1
            print(f"Correct! Score: {score}")
        print(f"Game Over! Final Score: {score}")
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
