import os
import sys
import asyncio
# пробрасываем корневой каталог
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import keyboards as nav
from common.bot_text import menu_reply_text
from common.settings import ASYNC_TIMER




# создаем новый роутер 
# его нужно будет подключить в Dispatcher 
# Через dp.include_routers() в app.py
cmd_private_router = Router()

@cmd_private_router.message(Command('start'))
@cmd_private_router.message((F.text.lower() == 'меню') | 
                            (F.text.lower() == 'menu') |
                            (F.text.lower() == 'home') |
                            (F.text.lower() == 'домой') |
                            (F.text.lower() == 'старт') |
                            (F.text.lower() == 'начать') |
                            (F.text.lower() == 'начало') |
                            (F.text.lower() == 'start') |
                            (F.text.lower() == 'go') |
                            (F.text.lower() == 'begin'))
async def start_cmd(message: types.Message, state: FSMContext):
    

    # проверка значений машины состояния
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")
    if message.chat.type == 'private':
        await message.delete()
        await message.answer(menu_reply_text['hello_message'], reply_markup=nav.mainMenu)

"""
@cmd_private_router.message(F.text)
async def start_cmd(message: types.Message):
    if message:
        await message.delete()
"""


# /help команда справочной информации
@cmd_private_router.message(Command('help'))
@cmd_private_router.message((F.text.lower() == 'помощь') | 
                            (F.text.lower() == 'справка') | 
                            (F.text.lower() == 'help') | 
                            (F.text.lower() == '?') | 
                            (F.text.lower() == 'help') | 
                            (F.text.lower() == 'хелп'))
async def help_cmd(message: types.Message):
    if message.chat.type == 'private':
        await message.delete()
        await message.answer(f'Можно начать с команды /start или написать слово "меню"')
        await asyncio.sleep(2)
        await message.delete(ASYNC_TIMER)
