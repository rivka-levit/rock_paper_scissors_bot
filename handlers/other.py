"""
Handler for all the messages out of logic of the bot.
"""

from aiogram import Router
from aiogram.types import Message

from lexicon import LEXICON_RU

router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
