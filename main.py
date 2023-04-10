#6128955126:AAF-_Gyyn7SXROMn9l4_Oe5a1pYQpBEl_E8


import logging
import asyncio
import requests

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Устанавливаем уровень логов
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token='6128955126:AAF-_Gyyn7SXROMn9l4_Oe5a1pYQpBEl_E8')

# Создаем объект диспетчера
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # Создаем кнопки
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text='Кнопка 1', callback_data='button1')
    button2 = InlineKeyboardButton(text='Кнопка 2', callback_data='button2')
    keyboard.add(button1, button2)

    # Отправляем сообщение с кнопками
    await message.reply("Привет!\nЯ телеграм бот.", reply_markup=keyboard)

# Обработчик команды /crypto
@dp.message_handler(commands=['crypto'])
async def process_crypto_command(message: types.Message):
    # Получаем данные о курсе биткоина
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()['bpi']['USD']
    # Отправляем сообщение с курсом биткоина и кнопкой "Назад"
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_back = InlineKeyboardButton(text='Назад', callback_data='button_back')
    keyboard.add(button_back)
    await message.reply(f"Курс биткоина:\n{data['rate']} {data['code']}\nИсточник: {response.json()['disclaimer']}", reply_markup=keyboard)

# Обработчик текстовых сообщений
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def process_text_message(message: types.Message):
    await message.reply("Вы написали: " + message.text)

# Обработчик нажатия на кнопку
@dp.callback_query_handler(lambda c: c.data == 'button_back')
async def process_callback_button_back(callback_query: types.CallbackQuery):
    # Отправляем сообщение с кнопками
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text='Кнопка 1', callback_data='button1')
    button2 = InlineKeyboardButton(text='Кнопка 2', callback_data='button2')
    keyboard.add(button1, button2)
    await bot.send_message(callback_query.from_user.id, "Привет!\nЯ телеграм бот.", reply_markup=keyboard)



@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_query(callback_query: types.CallbackQuery):
    # Получаем данные о курсе биткоина
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()['bpi']['USD']
    # Отправляем сообщение с курсом биткоина и кнопкой "Назад"
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_back = InlineKeyboardButton(text='Назад', callback_data='button_back')
    keyboard.add(button_back)
    await bot.send_message(callback_query.from_user.id, f"Курс биткоина:\n{data['rate']} {data['code']}", reply_markup=keyboard)



@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_query(callback_query: types.CallbackQuery):
    # Отправляем запрос на получение курса эфириума
    response = requests.get('https://api.coingecko.com/api/v3/coins/ethereum')
    data = response.json()['market_data']['current_price']['usd']

    # Создаем кнопку "Назад"
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_back = InlineKeyboardButton(text='Назад', callback_data='button_back')
    keyboard.add(button_back)

    # Отправляем сообщение с курсом эфириума и кнопкой "Назад"
    await bot.send_message(callback_query.from_user.id, f"Курс эфириума:\n{data} USD", reply_markup=keyboard)

# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
