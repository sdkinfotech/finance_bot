import os
import sys
# пробрасываем корневой каталог
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import types, Router, F
from actions import NewRecord

from aiogram.fsm.context import FSMContext
import keyboards as nav
from common.bot_text import menu_reply_text
from common.bot_text import expense_buttons_text


# import common.text as text
# в этом модуле собраны все клавиатурные хендлеры
# требуется основательно их переработать
# кроме того, требуется поработать и с машиной состояний.
# пока ее обработка не совсем понятна

# создаем новый роутер 
# его нужно будет подключить в Dispatcher 
# Через dp.include_routers() в app.py
keyboard_private_router = Router()


### ЭКРАН ГЛАВНОГО МЕНЮ

# обработка вызова меню 
@keyboard_private_router.callback_query(lambda query: query.data == "expenses")
async def handle_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.message.answer('Выберите категорию', reply_markup=nav.expense_buttons_markup)
    await query.answer()


### ВЫЗОВ НОМЕРНОЙ КЛАВИАТУРЫ
    
# Обработка номерной клавиатуры для ввода суммы
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_1")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_2")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_3")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_4")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_5")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_6")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_7")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_8")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_9")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_0")
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_point")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    await query.answer(callback_data)

# очистка введенных значений с клавиатуры
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_clear")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.answer(callback_data)

# подтвержение введенных значений с клавиатуры
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_ok")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.answer(callback_data)

### ЭКРАН МЕНЮ ВЫБОРА КАТЕГОРИИ
    
@keyboard_private_router.callback_query(lambda query: query.data == "expButton_public_utilities")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.message.answer('Введите сумму', reply_markup=nav.numeric_menu)
    await query.answer()

### ОБЩИЕ ВЫЗОВЫ
    
# Обработка кнопки Домой(назад в главное меню)
@keyboard_private_router.callback_query(lambda query: query.data == "back")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.message.answer("Главное меню", reply_markup=nav.mainMenu)
    await query.answer()

# отлавливает все коллбэки, которые не были обработаны выше, пишет информацию в лог и консоль
@keyboard_private_router.callback_query()
async def handle_callback(query: types.CallbackQuery):
    print(f"Нажата кнопка с необработанным callback_data: {query.data}")


"""
# обрабатываем кнопки для статьи расходов
# кнопки которые содержат в коллбэке expButton
@keyboard_private_router.message()
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