"""
Модуль содержит в себе все обшие настройки, 
которые могут использоваться ботом.

private_cmd: список команд бота
TOKEN: содержит токен бота
ALLOWED_UPDATES: установка фильтров получения обновлений
ASYNC_TIMER: значение ассинхронного таймера задержки 
"""
import os
from aiogram.types import BotCommand
from dotenv import load_dotenv, find_dotenv

# список команд меню бота,
# отображаются в телеграм при вызове копки меню слева
# Это встроенный функционал телеграма.
# передается в app.py bot.set_my_commands(commands=)
# !!!ВАЖНО!!! объявляется обязательно до start_polling
private_cmd = [

    BotCommand(command='start', description="Начало работы с ботом"),
    BotCommand(command='help', description="Справка"),
]

# Получаем токен из переменных окружения
load_dotenv(find_dotenv()) # ищем .env и забираем переменне
TOKEN = os.getenv('TOKEN') # получаем токен из .env

# в этом списке разрешенные типы обновлений для pollyng
# передаются в app.py в start_polling(allowed_updates=)
ALLOWED_UPDATES = ['callback_query','message']

# таймер после которого сообщения исчезают
# Удаляют пользовательские сообщения, и сообщения бота через время
ASYNC_TIMER = 3
