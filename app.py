import asyncio
import logging

from aiogram import Bot, Dispatcher, types

from handlers.cmd_private import cmd_private_router
from handlers.keyboard_private import keyboard_private_router
from common import settings


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


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.TOKEN)
dp = Dispatcher()
# имортируем роутеры из каталога handlers
dp.include_routers(cmd_private_router, keyboard_private_router) 


async def main():
        
        # удаление вебхуков, в случае если бот был оффлайн
        # на сервере могли накопиться сообщения, и после того 
        # как бот включится, все эти сообщения будут приходить 
        await bot.delete_webhook(drop_pending_updates=True)

        # передаем все команды из common.bot_command_list.py для отображения команд в меню ТГ
        # указываем scope=BotCommandScopeAllPrivateChats
        # слкдующая закомментированная конструкция чищает список
        # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
        await bot.set_my_commands(commands=settings.private_cmd, scope=types.BotCommandScopeAllPrivateChats())
        
        # проверка обновлений
        # allowed_updates примнимает список только разрешенных обновлений
        # можно почитать в документации https://core.telegram.org/bots/api#getupdates
        await dp.start_polling(bot, allowed_updates=settings.ALLOWED_UPDATES)
        
        

if __name__ == "__main__":
    asyncio.run(main())
