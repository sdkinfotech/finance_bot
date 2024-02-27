import os
import sys
import asyncio
# пробрасываем корневой каталог
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import types, Router, F
# вызовы машины состояний
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import keyboards as nav
from common.bot_text import menu_reply_text, expense_buttons_text
from common.settings import ASYNC_TIMER
from actions import NewRecord

# создаем новый роутер 
# его нужно будет подключить в Dispatcher 
# Через dp.include_routers() в app.py
keyboard_private_router = Router()

#Классы определения машины состояний
class UserStates(StatesGroup):
    
    description = State() # Описание расходов
    item = State() # Категория расходов, устанавливается автоматически
    price = State() # стоимость расходов
    numeric_state = State() # промежуточное значение для номерной клавиатуры

### ЭКРАН ГЛАВНОГО МЕНЮ

# обработка расходы 
@keyboard_private_router.callback_query(lambda query: query.data == "expenses")
async def handle_callback(query: types.CallbackQuery, state: FSMContext):
    # записываем коллбэк в переменную 
    callback_data = query.data
    # выводим отладочное сообщение в консоли, какой коллбэк получен
    print(f"Получен callback_data: {callback_data}")
    
    # пресет значений машины состояний для следующих шагов
    await state.update_data(item=None)
    await state.update_data(description=None)
    await state.update_data(price=None)
    # проверка информации в машине состояний
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")

    await query.message.edit_text('<b>Выберите категорию</b>', reply_markup=nav.expense_buttons_markup)
    await query.answer()

# Обработка кнопки доходы)
@keyboard_private_router.callback_query(lambda query: query.data == "income")
async def listen_callback(query: types.CallbackQuery):
    # записываем коллбэк в переменную 
    callback_data = query.data
    # выводим отладочное сообщение в консоли, какой коллбэк получен
    print(f"Получен callback_data: {callback_data}")
    await query.answer("Раздел находится в разработке")


### ЭКРАН МЕНЮ ВЫБОРА КАТЕГОРИИ

# каждый раз, когда нажата эта кнопка, требуется записать в значение машины состояний
# категорию расходов для передачи в конечный запрос.  
@keyboard_private_router.callback_query(lambda query: query.data == "public_utilities")
@keyboard_private_router.callback_query(lambda query: query.data == "housing_Rent")
@keyboard_private_router.callback_query(lambda query: query.data == "phone_Internet")
@keyboard_private_router.callback_query(lambda query: query.data == "commission_payment")
@keyboard_private_router.callback_query(lambda query: query.data == "subscription_payment")
@keyboard_private_router.callback_query(lambda query: query.data == "household_products")
@keyboard_private_router.callback_query(lambda query: query.data == "health")
@keyboard_private_router.callback_query(lambda query: query.data == "sport_fitness")
@keyboard_private_router.callback_query(lambda query: query.data == "hygiene_cosmetics")
@keyboard_private_router.callback_query(lambda query: query.data == "alcohol")
@keyboard_private_router.callback_query(lambda query: query.data == "products")
@keyboard_private_router.callback_query(lambda query: query.data == "education")
@keyboard_private_router.callback_query(lambda query: query.data == "trading_business")
@keyboard_private_router.callback_query(lambda query: query.data == "investment")
@keyboard_private_router.callback_query(lambda query: query.data == "charity")
@keyboard_private_router.callback_query(lambda query: query.data == "gifts")
@keyboard_private_router.callback_query(lambda query: query.data == "events")
@keyboard_private_router.callback_query(lambda query: query.data == "restaurants")
@keyboard_private_router.callback_query(lambda query: query.data == "entertainments")
@keyboard_private_router.callback_query(lambda query: query.data == "flight_Intercity")
@keyboard_private_router.callback_query(lambda query: query.data == "taxi")
@keyboard_private_router.callback_query(lambda query: query.data == "public_transport")
@keyboard_private_router.callback_query(lambda query: query.data == "vehicle")
@keyboard_private_router.callback_query(lambda query: query.data == "fuel")
@keyboard_private_router.callback_query(lambda query: query.data == "everyday_life_tech")
@keyboard_private_router.callback_query(lambda query: query.data == "house_furniture_tools")
@keyboard_private_router.callback_query(lambda query: query.data == "clothes_footwear")
@keyboard_private_router.callback_query(lambda query: query.data == "accessory")
@keyboard_private_router.callback_query(lambda query: query.data == "hand_tools")
@keyboard_private_router.callback_query(lambda query: query.data == "building_materials")
@keyboard_private_router.callback_query(lambda query: query.data == "private_debt")
@keyboard_private_router.callback_query(lambda query: query.data == "credit")
@keyboard_private_router.callback_query(lambda query: query.data == "other")
async def listen_callback(query: types.CallbackQuery, state: FSMContext):
    # записываем коллбэк в переменную 
    callback_data = query.data
    # выводим отладочное сообщение в консоли, какой коллбэк получен
    print(f"Получен callback_data: {callback_data}")
    # записываем значение callback в машину состояний
    await state.update_data(item=callback_data)
    print("Запись значения в машину состояний")
    # проверка информации в машине состояний
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")
    await query.message.edit_text('Введите сумму', reply_markup=nav.numeric_menu)
    await query.answer()

### ВЫЗОВЫ НОМЕРНОЙ КЛАВИАТУРЫ
    
# Можно также распаковать через FOR в дальнейшем
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
async def listen_callback(query: types.CallbackQuery, state: FSMContext):
    # записываем коллбэк в переменную 
    callback_data = query.data
    # выводим отладочное сообщение в консоли, какой коллбэк получен
    print(f"Получен callback_data: {callback_data}")

    # обрабатываем ввод цифр в зависимости от полученного коллбэка
    if callback_data == 'numButton_1' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '1'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '1'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
        
    
    if callback_data == 'numButton_2' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '2'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '2'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_3' : 
        
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '3'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '3'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_4' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '4'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '4'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_5' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '5'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '5'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_6' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '6'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '6'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_7' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '7'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '7'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_8' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '8'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '8'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_9' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '9'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '9'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
    
    if callback_data == 'numButton_0' : 
        # получаем значение из машины состояний
        data = await state.get_data()
        
        # проверяем, существует ли ключ 'numeric_state' в data
        # если нет, инициализируем его значением соответствующим нажатой кнопки
        if 'numeric_state' not in data:
            row = '0'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)
            
        else:
            row = data['numeric_state'] + '0'
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)

    await query.answer()

# очистка введенных значений с клавиатуры
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_clear")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.message.edit_text('Введите сумму:', reply_markup=nav.numeric_menu) 
    await query.answer("Сброс значений")

# подтвержение введенных значений с клавиатуры
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_ok")
async def listen_callback(query: types.CallbackQuery):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.message.edit_text('Введите сумму:', reply_markup=nav.item_menu) 
    await query.answer("")

### ДОБАВЛЕНИЕ ЗАПИСИ
    #'descr':'🗒️ Добавить описание',
    #'add_record': '✏️ Записать'
    
@keyboard_private_router.callback_query(lambda query: query.data == 'description')
async def handle_callback(query: types.CallbackQuery, state: FSMContext):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    await query.message.edit_text('🗒️Описание:', reply_markup=None)
    # ожидаем значение введенное пользователем
    await state.set_state(UserStates.description)
    await query.answer()

# Обработчик машины состояния
@keyboard_private_router.message(UserStates.description, F.text)
async def description_received(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Описание добавлено", reply_markup=nav.item_menu)

@keyboard_private_router.callback_query(lambda query: query.data == "add_record")
# :param expense_item: статья расходов
# :param price: цена
# :param description: подробное описание
async def handle_callback(query: types.CallbackQuery, state: FSMContext):
     # Значение в машине состояний представлено в виде словарей
     # например {'description': 'Это тестовое сообщение'}
     # Записываем его в переменную для передачи в вывод через метод send.record()
    data = await state.get_data()
    # Вытаскиваем значение по ключу
    description = data['description']
    print(data)
    # формирование записи 
    new_record = NewRecord(expense_item="test",  description=description, price="15")
    # Отправляем в базу
    new_record.send_record()
    # Очистка значений машины состояний
    await state.clear()
    await query.answer()


### ОБЩИЕ ВЫЗОВЫ
    
# Обработка кнопки Домой(назад в главное меню)
# Каждый раз, когда нажата эта кнопка, 
# машина состояний очищается await state.clear()
@keyboard_private_router.callback_query(lambda query: query.data == "back")
async def handle_callback(query: types.CallbackQuery, state: FSMContext):
    await query.message.edit_text("Главное меню", reply_markup=nav.mainMenu)
    # не забываем очистить все что есть в машине состояний
    
    # Очистка машины состояния 
    await state.clear()
    # проверка значений машины состояния
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")
    await query.answer()

# отлавливает все коллбэки, которые не были обработаны выше, пишет информацию в лог и консоль
@keyboard_private_router.callback_query()
async def handle_callback(query: types.CallbackQuery, state: FSMContext):
    print(f"Нажата кнопка с необработанным callback_data: {query.data}")
