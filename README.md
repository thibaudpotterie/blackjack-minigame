# High-Low Blackjack Minigame

A stand-alone Python project for a "High-Low" card game, where players guess if the next card dealt will be higher or lower than the current one.

## Project Scope
This project is a minimalist implementation of a High-Low card game. It demonstrates best practices in Python development, including:
- Functional decomposition (2-4 core functions).
- Unit testing with `pytest`.
- Linting and code quality with `ruff`.
- Automated CI/CD using GitHub Actions.

## Functions Overview
- `get_card()`: Generates a random card value between 1 and 11.
- `play_turn(current_card)`: Handles user input and the comparison logic for a single game turn.
- `main()`: Manages the overall game state, scoring, and the option to restart after a loss.

## AI Contribution & Workflow
This project was developed in collaboration with **Antigravity (Google DeepMind)**, an agentic AI coding assistant.
- **Workflow**: The AI was used for initial logic generation, refactoring for PEP8 compliance (using the `black` formatter), implementing unit tests with mocks, and configuring the GitHub Actions CI workflow. All code was reviewed and validated by the user.

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run the game: `python high_low.py`
3. Run tests: `pytest`