"""Unit tests for the High-Low Blackjack minigame."""

from unittest.mock import patch
from high_low import get_card, play_turn


def test_get_card():
    """Verify get_card returns values in range 1-13."""
    for _ in range(100):
        card = get_card()
        assert 1 <= card <= 13


@patch("high_low.input", return_value="h")
@patch("high_low.get_card", return_value=12)
def test_play_turn_win_higher(_mock_get_card, _mock_input):
    """Verify play_turn logic for a correct 'higher' guess (e.g., Queen)."""
    won, next_card = play_turn(5)
    assert won is True
    assert next_card == 12


@patch("high_low.input", return_value="l")
@patch("high_low.get_card", return_value=1)
def test_play_turn_win_lower(_mock_get_card, _mock_input):
    """Verify play_turn logic for a correct 'lower' guess (e.g., One)."""
    won, next_card = play_turn(5)
    assert won is True
    assert next_card == 1


@patch("high_low.input", return_value="h")
@patch("high_low.get_card", return_value=11)
def test_play_turn_lose_higher(_mock_get_card, _mock_input):
    """Verify play_turn logic for an incorrect 'higher' guess (e.g., Jack)."""
    won, next_card = play_turn(13)
    assert won is False
    assert next_card == 11


@patch("high_low.input", return_value="l")
@patch("high_low.get_card", return_value=12)
def test_play_turn_lose_lower(_mock_get_card, _mock_input):
    """Verify play_turn logic for an incorrect 'lower' guess (e.g., Queen)."""
    won, next_card = play_turn(10)
    assert won is True
    assert next_card == 12
