from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import psycopg2

def check():
    mainKeyBoard = ReplyKeyboardMarkup()

    conn = psycopg2.connect(host="localhost", port=5432, database="telegram", user="postgres", password="111111")
    cur = conn.cursor()
    cur.execute("SELECT * FROM main_currency")
    all_currency = cur.fetchall()
    for i in all_currency:
        a = KeyboardButton(i[1])
        mainKeyBoard.add(a)

    return mainKeyBoard