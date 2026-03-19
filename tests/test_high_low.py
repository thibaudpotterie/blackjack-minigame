"""Unit tests for the High-Low Blackjack minigame."""

from unittest.mock import patch
from high_low import get_card, play_turn


def test_get_card():
    """Verify get_card returns values in range 1-11."""
    for _ in range(100):
        card = get_card()
        assert 1 <= card <= 11


@patch("high_low.input", return_value="h")
@patch("high_low.get_card", return_value=10)
def test_play_turn_win_higher(_mock_get_card, _mock_input):
    """Verify play_turn logic for a correct 'higher' guess."""
    won, next_card = play_turn(5)
    assert won is True
    assert next_card == 10


@patch("high_low.input", return_value="l")
@patch("high_low.get_card", return_value=2)
def test_play_turn_win_lower(_mock_get_card, _mock_input):
    """Verify play_turn logic for a correct 'lower' guess."""
    won, next_card = play_turn(5)
    assert won is True
    assert next_card == 2


@patch("high_low.input", return_value="h")
@patch("high_low.get_card", return_value=3)
def test_play_turn_lose_higher(_mock_get_card, _mock_input):
    """Verify play_turn logic for an incorrect 'higher' guess."""
    won, next_card = play_turn(5)
    assert won is False
    assert next_card == 3


@patch("high_low.input", return_value="l")
@patch("high_low.get_card", return_value=8)
def test_play_turn_lose_lower(_mock_get_card, _mock_input):
    """Verify play_turn logic for an incorrect 'lower' guess."""
    won, next_card = play_turn(5)
    assert won is False
    assert next_card == 8
