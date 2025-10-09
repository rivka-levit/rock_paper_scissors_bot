import logging

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from lexicon import LEXICON_RU

logger = logging.getLogger(__name__)


async def set_main_menu(bot: Bot) -> None:
    menu_commands = [
        BotCommand(
            command=cm,
            description=descr
        ) for cm, descr in LEXICON_RU['commands'].items()
    ]
    await bot.set_my_commands(
        commands=menu_commands,
        scope=BotCommandScopeDefault()
    )
