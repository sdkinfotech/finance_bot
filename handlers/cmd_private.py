from aiogram import types, Router
from aiogram.filters import CommandStart, Command

import markups as nav


# создаем новый роутер 
# его нужно будет подключить в Dispatcher 
# Через dp.include_routers() в app.py
cmd_private_router = Router()

# /start стандартная команда
@cmd_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    # global_var_reset()
    if message.chat.type == 'private':
        await message.answer("hello_message", reply_markup=nav.mainMenu)

# /help команда справочной информации
@cmd_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    if message.chat.type == 'private':
        global from_user
        from_user = message.text
        await message.answer(f"Для начала введите /start")

# /реакция на ввод неотфильтрованного сообщения
# пока этот хендлер возвращает главное меню в любом случае
@cmd_private_router.message(CommandStart())
async def any_messages(message: types.Message):
    # global_var_reset()
    if message.chat.type == 'private':
        await message.answer("hello_message", reply_markup=nav.mainMenu)