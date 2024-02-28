"""
Модуль содержит в себе команды бота
Обрабатываются отдельным роутером
"""
import os
import sys
import asyncio

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import keyboards.keyboard as nav
from common.text_blocks import help_text, menu_text
from common.settings import ASYNC_TIMER

# пробрасываем корневой каталог
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    """
    /start команда боту начать диалог
    Стандартная команда в любом боте
    При активации команды сбрасываются значения 
    машины состояний и пользователь перебрасывается 
    в главное меню. Команду также можно вызнавть 
    если написать боту одну из перечисленных в декораторах 
    команд в магичесих фильтрах
    """

    # проверка значений машины состояния
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")
    if message.chat.type == 'private':
        await message.delete()
        await message.answer(menu_text['hello_message'], reply_markup=nav.mainMenu)

# /help команда справочной информации
@cmd_private_router.message(Command('help'))
@cmd_private_router.message((F.text.lower() == 'помощь') |
                            (F.text.lower() == 'справка') |
                            (F.text.lower() == 'help') |
                            (F.text.lower() == '?') |
                            (F.text.lower() == 'help') |
                            (F.text.lower() == 'хелп'))
async def help_cmd(message: types.Message):
    """
    /help справочная инфрмация для пользователя
    Сообщение исчезает через установленное время в ASYNC_TIMER
    """
    if message.chat.type == 'private':
        await message.delete() 
        sent_message = await message.answer(help_text['main_help'])
        await asyncio.sleep(ASYNC_TIMER)
        await sent_message.delete()
