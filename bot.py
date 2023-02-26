import asyncio
import logging

from config_data.config import load_config, Config

from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers


# Logger initialization
logger = logging.getLogger(__name__)

# Configuration function and bot starting
async def main():
    # Logger configuration
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )

    # Information about start of the bot is displayd in the console
    logger.info('Starting bot')

    # Load config in config variable
    config : Config = load_config('.env')

    # Initialization Bot and Dispather
    bot : Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp : Dispatcher = Dispatcher()

    # Register routers in dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')