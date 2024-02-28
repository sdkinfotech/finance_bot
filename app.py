"""
Главный модуль приложения
Отсюда стартует бот и выполняются 
Различные предустановки
"""
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
    """
    bot.delete_webhook:
    удаление вебхуков, в случае если бот был оффлайн
    на сервере могли накопиться сообщения, и после того 
    как бот включится, все эти сообщения будут приходить

    bot.set_my_commands:
    передаем все команды из common.bot_command_list.py 
    для отображения команд в меню ТГ
    указываем scope=BotCommandScopeAllPrivateChats
        
    bot.delete_my_commands:
    закомментированная конструкция очищает список

    dp.start_polling:
    проверка обновлений
    
    allowed_updates:
    примнимает список только разрешенных обновлений
    почитать в документации https://core.telegram.org/bots/api#getupdates
    """
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands\
    # (scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=settings.private_cmd, \
    scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=settings.ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
