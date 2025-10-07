from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import LEXICON_RU

# ------------ Enter game keyboard ---------------

def game_request_keyboard() -> ReplyKeyboardMarkup:
    """Create the game keyboard with two buttons."""

    # Create buttons
    yes_btn = KeyboardButton(text=LEXICON_RU['yes_button'])
    no_btn = KeyboardButton(text=LEXICON_RU['no_button'])

    builder = ReplyKeyboardBuilder()
    builder.row(yes_btn, no_btn, width=2)
    keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)

    return keyboard

# ----------- Choices keyboard --------------

def choices_keyboard() -> ReplyKeyboardMarkup:
    """Create the choices keyboard with three buttons."""

    rock_btn = KeyboardButton(text=LEXICON_RU['rock'])
    paper_btn = KeyboardButton(text=LEXICON_RU['paper'])
    scissors_btn = KeyboardButton(text=LEXICON_RU['scissors'])

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[rock_btn], [paper_btn], [scissors_btn]],
        resize_keyboard=True
    )

    return keyboard
