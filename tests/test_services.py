"""
Tests for the functions of bot service logic.
Command: pytest tests\test_services.py
"""
import pytest

from lexicon import LEXICON_RU
from services import get_bot_choice, get_winner


def test_random_bot_choice() -> None:
    """Test bot choice choose the answer from appropriate choices."""

    correct_choices = LEXICON_RU['choices'].keys()
    bot_choices = [get_bot_choice() for _ in range(3)]

    assert all(choice in correct_choices for choice in bot_choices)


@pytest.mark.parametrize("user_choice,bot_choice,expected", [
    (LEXICON_RU['choices']['rock'], 'rock', 'nobody_won'),
    (LEXICON_RU['choices']['rock'], 'scissors', 'user_won'),
    (LEXICON_RU['choices']['rock'], 'paper', 'bot_won'),
])
def test_get_winner_correct_winner(user_choice, bot_choice, expected):
    """Test function get_winner() returns correct winner."""

    assert get_winner(user_choice, bot_choice) == expected
