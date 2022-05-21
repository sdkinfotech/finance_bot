import os

# Модуль содержит в себе переменную api_key в виде словаря
# В словаре хранятся пути для авторизации google sheets и ID таблицы

script_dir = os.path.dirname(__file__)
creds_file = os.path.join(script_dir, 'creds.json')

api_key = {
        'json': creds_file,
        'sheet': 'your_google_sheet_key_here'}
