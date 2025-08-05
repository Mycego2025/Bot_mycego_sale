import asyncio
from core.logger import logger
from telegram.bot import dp, bot

async def main():
    logger.info("Starting application...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
