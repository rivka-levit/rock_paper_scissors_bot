import logging

from aiogram.types import BotCommand

from lexicon import LEXICON_RU

logger = logging.getLogger(__name__)


def get_menu_commands() -> list[BotCommand]:
    menu_commands = [
        BotCommand(command=cm, description=descr) for cm, descr in
        LEXICON_RU['commands'].items()
    ]
    return menu_commands
