from aiogram import BaseMiddleware
from aiogram.types import Message
from services.user_service import update_or_create_user

class UserActivityMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            success = update_or_create_user(
                id_tg=event.from_user.id,
                username=event.from_user.username
            )
            if not success:
                await event.answer("⚠ Сервис временно недоступен. Попробуйте позже.")
                return
        return await handler(event, data)