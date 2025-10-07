from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards import game_request_keyboard, choices_keyboard
from lexicon import LEXICON_RU

router = Router()