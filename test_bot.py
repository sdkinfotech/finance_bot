import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging
import common.text as text
from actions import NewRecord

import os
from dotenv import load_dotenv, find_dotenv




# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
load_dotenv()
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    exit("Error: no token provided")

# инициализация бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()  # память машины состояний
dp = Dispatcher(storage=storage)


# States для машины состояний
class Form(StatesGroup):
    item_name = State()
    description_name = State()


# Главное меню
mainMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=text.menu_buttons_text['expenses'], callback_data=text.expenses)],
    [InlineKeyboardButton(text=text.menu_buttons_text['income'], callback_data=text.income)]
])

# Далее добавьте оставшиеся клавиатуры, используя тот же формат
# ...

# Обработчики состояний и команд
@dp.message()
async def start(message: Message):
    await message.answer("Привет! Выбери что записать.", reply_markup=mainMenu)

# Добавьте здесь другие обработчики
# ...

async def main():
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())