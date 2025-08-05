from loguru import logger
import sys
import os

# Создаем папку logs если её нет
os.makedirs("logs", exist_ok=True)

# Убираем стандартный вывод
logger.remove()

# Логи в консоль
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    level="DEBUG"
)

# Все логи в один файл
logger.add(
    "logs/bot.log",  # один файл
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    rotation="10 MB",
    retention="10 days",
    level="DEBUG",
    enqueue=True
)
