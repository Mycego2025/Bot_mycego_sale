from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Привет, {name}!\n\n"
        "Я — бот **MPBridge** 🚀\n"
        "Помогу тебе автоматизировать задачи, собирать аналитику и ускорять работу с маркетплейсами.\n\n"
        "🛠 Доступные команды:\n"
        "• /help — список всех команд\n"
        "• /tasks — управление задачами\n"
        "• /reports — отчёты и аналитика\n\n"
        "💡 Готов начать прямо сейчас!"
        .format(name=message.from_user.first_name)
    )
