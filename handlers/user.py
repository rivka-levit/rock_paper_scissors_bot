import asyncio

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards import game_request_keyboard, choices_keyboard
from lexicon import LEXICON_RU
from services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=game_request_keyboard()
    )


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=game_request_keyboard()
    )


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    """Handler for `Yes` button pressed."""
    await message.answer(
        text=LEXICON_RU['yes'],
        reply_markup=choices_keyboard()
    )


@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_button(message: Message):
    """Handler for `No` button pressed."""
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text.in_(LEXICON_RU['choices'].values()))
async def process_game_button(message: Message):
    """Handler for any game button pressed."""

    bot_choice = get_bot_choice()

    await message.answer(
        text=f'{LEXICON_RU["bot_choice"]}: {LEXICON_RU["choices"][bot_choice]}'
    )

    winner = get_winner(user_choice=message.text, bot_choice=bot_choice)
    effect_id = '5046509860389126442' if winner == 'user_won' else None

    await asyncio.sleep(1)

    await message.answer(
        text=LEXICON_RU[winner],
        message_effect_id=effect_id,
        reply_markup=game_request_keyboard()
    )
