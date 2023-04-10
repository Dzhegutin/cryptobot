import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Устанавливаем уровень логов
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token='6128955126:AAF-_Gyyn7SXROMn9l4_Oe5a1pYQpBEl_E8')

# Создаем объект диспетчера
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ телеграм бот.")

# Обработчик текстовых сообщений
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def process_text_message(message: types.Message):
    await message.reply("Вы написали: " + message.text)

# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
