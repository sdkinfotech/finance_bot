import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup

from dotenv import load_dotenv, find_dotenv

from handlers.cmd_private import cmd_private_router
from handlers.keyboard_private import keyboard_private_router

load_dotenv(find_dotenv()) # ищем .env и забираем переменне


# глобальные переменные для суммы вводимой с клавиатуры
current_price = ''
saved_price = ''

expense = ''  # глобальная переменная для хранения значения статьи расхода при выборе
price = ''  # глобальная переменная для хранения записи цены
item = ''  # глобальная переменная для хранения наименования
description = ''  # глобальная переменная для указания описания

# глобальные переменные для удаления сообщений при передвижении по меню
msg_add_descr_choice = ''  # в переменную помещатся сообщение, для управления из другой функции
add_descr_choice = False  # после удаления сообщения флаг меняется на True
msg_add_descr_input = ''

msg_add_item = ''
add_item_delete = False

msg_choice_action = ''
choice_action_delete = False
msg_edit = ''


def global_var_reset():
    """
    Функция которая сбрасывает значения глобальных переменных
    Вызов функции происходит при /start при back home
    также вызов функции осуществляется при add_record
    :return:
    """
    global current_price, saved_price, expense, price, item, description

    # глобальные переменные для суммы вводимой с клавиатуры
    current_price = ''
    saved_price = ''

    expense = ''  # глобальная переменная для хранения значения статьи расхода при выборе
    price = ''  # глобальная переменная для хранения записи цены
    item = ''  # глобальная переменная для хранения наименования
    description = ''  # глобальная переменная для указания описания
    # ---------------------------------------------------------
    print('current_price, saved_price, expense, price, item, description SET AS DEFAULT')


# States для машины состояний. Используется чтобы сохранять значения вводимые пользователем
class Form(StatesGroup):
    item_name = State()  # Will be represented in storage as 'Form:item_name'
    description_name = State()  # Will be represented in storage as 'Form:description_name'

# инициализация бота
TOKEN = os.getenv('TOKEN') # получаем токен из .env
ALLOWED_UPDATES = ['callback_query','message'] # разрешенные типы обновлений для pollyng

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
# память машины состояний
storage = MemoryStorage()  
dp = Dispatcher(storage=storage)
# имортируем роутеры из каталога handlers
dp.include_routers(cmd_private_router, keyboard_private_router) 


async def main():
        
        # удаление вебхуков, в случае если бот был оффлайн
        # на сервере могли накопиться сообщения, и после того 
        # как бот включится, все эти сообщения будут приходить 
        await bot.delete_webhook(drop_pending_updates=True)
        
        # проверка обновлений
        # allowed_updates примнимает список только разрешенных обновлений
        # можно почитать в документации https://core.telegram.org/bots/api#getupdates
        await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES) 

if __name__ == "__main__":
    asyncio.run(main())
