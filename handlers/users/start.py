from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.postgres import DB
import psycopg2
from loader import dp
import datetime
from keyboards.default.menu import check

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        conn = psycopg2.connect(host="localhost", port=5432, database="telegram", user="postgres", password="111111")
        cur = conn.cursor()
        now = datetime.datetime.now()
        cur.execute("INSERT INTO main_client(user_id, username, name, lastname,created_at) VALUES (%s,%s,%s,%s,%s);", (message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name,now))
        conn.commit()
    except: error = 'Пользователь уже существует'

    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=check())
