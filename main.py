import sys
import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from config_reader import config
from handlers.user_handlers import user_handlers
from callbacks import game_modes_info_callback

async def main() -> None:
    """
    Main function for initializing and starting the bot.
    
    Comments:
        - The main function for configuring and launching the bot using the aiogram library.
        - Removes existing logging handlers and adds a new one for output to the standard error stream (console).
        - Creates an instance of the bot and a dispatcher.
        - Initializes and includes command handlers (routers) from the user_handlers module.
        - Sets up webhook parsing if configured.
        - Starts the continuous polling of updates by the bot.
    """
    
    logger.remove()
    logger.add(sys.stderr, format="<green>{time: DD-MM-YYYY at HH:mm:ss}</green> | <level>{level:^8}</level> | {message}")
    
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    
    logger.info("aiogram.dispatcher: Start Polling")
    logger.info("aiogram.dispatcher: Run polling for bot - \"Epic Game Hub\"")
    
    dp.include_routers(
        user_handlers.router,
        game_modes_info_callback.router
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
