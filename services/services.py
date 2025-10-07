"""
Game logic.
"""

import random

from lexicon import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice(LEXICON_RU['choices'].keys())


def _normalize_user_answer(user_answer: str) -> str | None:
    """Returns the key if the value is the user answer."""

    for key in LEXICON_RU['choices']:
        if LEXICON_RU['choices'][key] == user_answer:
            return key

    return None



def get_winner(user_choice: str, bot_choice: str) -> str:
    """Define winner of the game."""

    user_choice = _normalize_user_answer(user_choice)
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    if user_choice == bot_choice:
        return "nobody_won"
    elif rules[user_choice] == bot_choice:
        return "user_won"

    return "bot_won"
