from aiogram import types
from aiogram.dispatcher import FSMContext
import psycopg2

from keyboards.default.menu import check
from loader import dp
from bs4 import BeautifulSoup
import requests


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    try:
        currency = message.text.lower()
        link = 'https://coinmarketcap.com/currencies/' + currency
        responce = requests.get(link).text
        soup = BeautifulSoup(responce, 'lxml')
        info = soup.find('div', class_='priceValue___11gHJ').text
        messages = 'Сейчас 1 '+message.text+' стоит '+info
        await message.answer(messages, reply_markup=check())
    except:
        await message.answer('Данной криптовалюты не существует', reply_markup=check())




