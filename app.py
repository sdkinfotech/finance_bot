import asyncio
import logging

from aiogram import Bot, Dispatcher, types

# для форматирования сообщений HTML
# передается при инициализации бота
# parse_mode=ParseMode.HTML
from aiogram.enums import ParseMode
from handlers.cmd_private import cmd_private_router
from handlers.keyboard_private import keyboard_private_router
from common import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.TOKEN, parse_mode=ParseMode.HTML)
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
        # слкдующая закомментированная конструкция очищает список
        # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
        await bot.set_my_commands(commands=settings.private_cmd, scope=types.BotCommandScopeAllPrivateChats())
        
        # проверка обновлений
        # allowed_updates примнимает список только разрешенных обновлений
        # можно почитать в документации https://core.telegram.org/bots/api#getupdates
        await dp.start_polling(bot, allowed_updates=settings.ALLOWED_UPDATES)
        
        

if __name__ == "__main__":
    asyncio.run(main())
