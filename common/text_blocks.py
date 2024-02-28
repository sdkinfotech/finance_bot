"""
Модуль содержит в себе текстовые блоки,
которыми бот отвечает в диалогах и в меню
menu_reply_text: словарь с фразами в меню бота
alert_text: словарь с предупреждениями об ошибках
"""

menu_text = {
    'hello_message' : 'Приветствую! Что будем добавлять?',
    'choose_category' : 'Выберите категорию',
    'dev_mode' : 'Раздел находится в разработке',
    'enter_price' : 'Введите сумму:',
    'add_rec_without_descr' : 'Добавить описание \nзаписать в базу',
    'add_rec_with_descr' : "Описание добавлено, \nРедактировать описание, \nзаписать в базу",
    'description' : '🗒️Описание:',
    'go_to_main' : 'Что будем добавлять?'

}

alert_text = {
    'two_zerro_err' : 'Значение не может начинаться с двух нулей подряд.',
    'first_dot_err' : 'Значение не может начинаться со знака разделителя.',
    'two_dots_err' : 'Значение не может содержать более двух знаков разделителя.',
    'zero_value_err': 'Вы указали нулевое значение, в этом нет никакого смысла.',
    'forgot_price' : 'Вы забыли указать стоимость.'

}

debug_text ={
    'unknown_callback' : 'Нажата кнопка с необработанным callback_data:'
}

help_text = {
    'main_help' : 'Тут и так все понятно'
}
