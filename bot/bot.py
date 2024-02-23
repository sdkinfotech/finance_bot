import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


import os
import logging
import markups as nav
from actions import NewRecord
# import buttons


# глобальные переменные для суммы вводимой с клавиатуры
current_price = ''
saved_price = ''

expense = ''  # глобальная переменная для хранения значения статьи расхода при выборе
price = ''  # глобальная переменная для хранения записи цены
item = ''  # глобальная переменная для хранения наименования
description = ''  # глобальная переменная для указания описания


# сообщения бота
hello_message = 'Привет! Выбери что записать 🙂'

expense_message = 'Выберите из списка:'

completed_message = 'Запись добавлена в Google таблицу'

after_descr_msg = 'Если нужно отредактировать значения наименования ' \
                  'и описания можно повторно нажать на 1 или 2, ' \
                  'или просто нажмите добавить запись'

add_discr_msg = 'Укажите описание тут. Его можно будет ' \
                'изменить при необходимости до отправки'

after_item_msg = 'Также можно указать подробное описание нажмите на кнопу 2, ' \
                 'для редактирования названия нажмите 1, ' \
                 'или просто нажмите добавить запись'

add_item_msg = 'Укажите наименование тут. Его можно будет изменить ' \
               'при необходимости до отправки'


# глобальные переменные для удаления сообщений при передвижении по меню
msg_add_descr_choice = ''  # в переменную помещатся сообщение, для управления из другой функции
add_descr_choice = False  # после удаления сообщения флаг меняется на True
msg_add_descr_input = ''

msg_add_item = ''
add_item_delete = False

msg_choice_action = ''
choice_action_delete = False
msg_edit = ''


# States для машины состояний. Используется чтобы сохранять значения вводимые пользователем
class Form(StatesGroup):
    item_name = State()  # Will be represented in storage as 'Form:item_name'
    description_name = State()  # Will be represented in storage as 'Form:description_name'


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


# получаем токен из файла
script_dir = os.path.dirname(__file__)
key_file = os.path.join(script_dir, 'key.txt')
with open(key_file, 'r') as f:
    TOKEN = f.read()

# инициализация бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()  # память машины состояний
dp = Dispatcher(storage=storage)



# ОБРАБОТКА ХЕНДЛЕРОВ

@dp.message()
async def start_cmd(message: types.Message):
    # global_var_reset()
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, hello_message, reply_markup=nav.mainMenu)

"""
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        global from_user
        from_user = message.text
        return from_user


# обрабатываем кнопки для статьи расходов
# кнопки которые содержат в коллбэке expButton
@dp.callback_query_handler(text_contains='expButton')
async def listen_callback(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    global expense  # получаем доступ к глобальной переменной
    expense = str(call.data)[10:]  # обрезаем expButton в строке
    await bot.send_message(call.from_user.id, 'Укажите сумму', reply_markup=nav.numeric_menu)


# обрабатываем цифровую клавиатуру, добавлена защита от дурака
@dp.callback_query_handler(text_contains='numButton')
async def listen_callback(call: types.CallbackQuery):
    # await bot.delete_message(call.from_user.id, call.message.message_id)
    # строка выше закоментирована, так как мы будем редактировать сообщение а не удалять его
    data = call.data  # читаем что у нас нажато
    print('Нажата кнопка', data)
    global current_price, saved_price  # получаем доступ к переменной
    if data == 'no':
        pass
   # Очистка значений
    elif data == 'numButton_clear':
        current_price = ''
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id, 'Укажите сумму', reply_markup=nav.numeric_menu)

    # Проверка на ошибки и сохранение результата
    elif data == 'numButton_ok':

        if current_price == '' or current_price == 'Укажите сумму' or current_price == 'Вы не указали сумму!':
            print(current_price)
            await bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text='Вы не указали сумму!',
                reply_markup=nav.numeric_menu)
            current_price = ''
        elif current_price[:1] == '0' \
                or current_price[:1] == '.' \
                or current_price[-1] == '.' \
                or current_price.count('.') > 1:
            await bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text='Некорректное значение!',
                reply_markup=nav.numeric_menu)
            current_price = ''
        else:
            global msg_choice_action
            await bot.delete_message(call.from_user.id, call.message.message_id)

            msg_choice_action = await bot.send_message(
                call.from_user.id,
                'Можно указать наименование, описание, или оставить так.',
                reply_markup=nav.item_menu)
            print("Сохранение суммы", current_price)
            global price
            price = current_price
            saved_price = current_price
            current_price = ''
    # добавляем к строке значение ипереписываем
    else:
        current_price += str(data[10:])
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=current_price,
            reply_markup=nav.numeric_menu)


@dp.callback_query_handler(text=buttons.income)
async def main_menu_income(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'этот раздел пока в разработке', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text=buttons.expenses)
async def main_menu_expenses(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, expense_message, reply_markup=nav.expensesMenu)


@dp.callback_query_handler(text=buttons.back)
async def rand(message: types.Message):
    # очистка значения цены при возврате в главное меню
    global_var_reset()
    global current_price

    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, hello_message, reply_markup=nav.mainMenu)


@dp.callback_query_handler(text=buttons.add_new)
async def rand(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, hello_message, reply_markup=nav.expensesMenu)


@dp.callback_query_handler(text=buttons.add_record)
async def rand(message: types.Message):
    print(current_price)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, completed_message, reply_markup=nav.mainMenu)
    new_record = NewRecord(buttons.expense_buttons[expense], price, item, description) 
    new_record.send_record() 
    global_var_reset()  # обнуляем переменные


#  обработка ввода с клавиатуры при помощи машины состояний
@dp.callback_query_handler(text=buttons.item_button)
async def rand(message: types.Message):
    global msg_add_item, msg_choice_action, choice_action_delete

    if not choice_action_delete:
        await msg_choice_action.delete()
        choice_action_delete = True

    msg_add_item = await bot.send_message(message.from_user.id, add_item_msg)
    await Form.item_name.set()  # ожидаем плдучения значения item_name


# теперь обработаем полученное значение item_name
@dp.message_handler(state=Form.item_name)
async def process_item_name(message: types.Message, state: FSMContext):
   
    async with state.proxy() as data:
        global item, msg_add_descr_choice, add_item_delete
        data['item_name'] = message.text
        item = data['item_name']
        await state.finish()
        print('Наименование:', item)

        if not add_item_delete:
            await msg_add_item.delete()
            add_item_delete = True

        msg_add_descr_choice = await bot.send_message(message.from_user.id, after_item_msg, reply_markup=nav.item_menu)


@dp.callback_query_handler(text=buttons.descr_button)
async def rand(message: types.Message):
    global msg_add_descr_input, add_descr_choice

    if not add_descr_choice:
        await msg_add_descr_choice.delete()
        add_descr_choice = True

    msg_add_descr_input = await bot.send_message(message.from_user.id, add_discr_msg)
    await Form.description_name.set()  # ожидаем получения значения description_name


# теперь обработаем полученное значение description_name
@dp.message_handler(state=Form.description_name)
async def process_description_name(message: types.Message, state: FSMContext):
    
    await msg_add_descr_input.delete()
    async with state.proxy() as data:
        global description
        data['description_name'] = message.text
        description = data['description_name']
        await state.finish()
        print('Описание:', description)
        await bot.send_message(message.from_user.id, after_descr_msg, reply_markup=nav.item_menu)

"""
async def main():
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
