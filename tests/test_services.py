"""
Tests for the functions of bot service logic.
Command: pytest tests\test_services.py
"""

from lexicon import LEXICON_RU
from services import get_bot_choice, get_winner


def test_random_bot_choice() -> None:
    """Test bot choice choose the answer from appropriate choices."""

    correct_choices = LEXICON_RU['choices'].keys()
    bot_choices = [get_bot_choice() for _ in range(3)]

    assert all(choice in correct_choices for choice in bot_choices)
