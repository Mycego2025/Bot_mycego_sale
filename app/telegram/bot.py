from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from telegram.handlers import start
from core.config import settings
from telegram.middlewares.user_activity import UserActivityMiddleware

bot = Bot(
    token=settings.telegram_bot_token,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

dp.message.middleware(UserActivityMiddleware())
dp.include_router(start.router)
