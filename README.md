# finance_bot

Телеграм бот для контроля расходов.
Ветка доходов находится в разработке. 

Бот отправляет информацию в гугл таблицу, 

Для запуска используйте bot.py

Чтобы все работало нужно пердварительно получить ключи для работы с Google Sheets и Telegram bot

google/key.py содержит данные для работы с google API и google sheets
В папке google должен присутствовать creds.json полученный из гугла.

api_key = {
        'json': creds_file,
        'sheet': 'your_google_sheet_key_here'}

bot/key.txt содержит токен для Telegram BOT

https://zen.yandex.ru/video/watch/6288b1f2ca007263a781516d демонстрационное видео
