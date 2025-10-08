import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import Config, load_config

from handlers.other import router as other_router
from handlers.user import router as user_router

from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


async def main():
    """Entry point to config and run the bot."""

    config: Config = load_config()

    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
        stream=config.log.stream
    )

    # Initialize the bot
    logger.info('Starting bot...')
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Register routers en dispatcher
    logger.info('Setting up routers...')
    dp.include_router(user_router)
    dp.include_router(other_router)

    # Set up maim menu
    logger.info('Setting up main menu commands...')
    await set_main_menu(bot=bot)

    # Skip old updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
