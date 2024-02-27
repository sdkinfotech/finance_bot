import os
import sys
import asyncio
# пробрасываем корневой каталог
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import types, Router, F
# вызовы машины состояний
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import keyboards.keyboard as nav
from keyboards.buttons import expense_buttons_text
from common.text_blocks import menu_reply_text

from common.settings import ASYNC_TIMER
from operations.actions import NewRecord

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
    await state.update_data(description='Нет описания')
    await state.update_data(price=0)
    await state.update_data(numeric_state = '')
    # проверка информации в машине состояний
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")

    await query.message.edit_text('<b>Выберите категорию</b>', reply_markup=nav.expense_buttons_markup)
    await query.answer()

# Обработка кнопки доходы
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
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_.")
async def listen_callback(query: types.CallbackQuery, state: FSMContext):
    # записываем коллбэк в переменную 
    callback_data = query.data
    # выводим отладочное сообщение в консоли, какой коллбэк получен
    print(f"Получен callback_data: {callback_data}")

    # Разделяем строку по "_" для того чтобы вытащить значение кнопки из коллбэка
    parts = callback_data.split("_")
    # Выбираем последний элемент полученного списка, который и будет числом
    button_value = parts[-1] if len(parts) > 1 else None  # '0' если существует, None в противном случае

    # получаем значение из машины состояний
    data = await state.get_data()
        
    # проверяем, существует ли ключ 'numeric_state' в data
    # если нет, инициализируем его значением соответствующим нажатой кнопки
    if 'numeric_state' not in data:
        row = button_value
        await query.message.edit_text(row, reply_markup=nav.numeric_menu)
        await state.update_data(numeric_state=row)      
    else:
        row = data['numeric_state'] + button_value
        
        # проверка на валидность вводимого значения
        # если значение начинается с 00
        if row == '00':
             # сбрасываем значение машины состояний
             await state.update_data(numeric_state='')
             # выводим информационное сообщение для пользователя
             await query.answer("Значение не может начинаться c двух нулей", show_alert=True)
             await query.message.edit_text('Введите сумму:', reply_markup=nav.numeric_menu)
             return
        elif row == '.':
            # сбрасываем значение машины состояний
             await state.update_data(numeric_state='')
             # выводим информационное сообщение для пользователя
             await query.answer("Значение не может начинаться со знака разделителя", show_alert=True)
             await query.message.edit_text('Введите сумму:', reply_markup=nav.numeric_menu)
             return
        else:
            # Проверка на появление двойной точки в значении
            if row.count('.') > 1:
                # Сбрасываем значение и сообщаем о некорректном вводе
                await state.update_data(numeric_state='')
                await query.answer("Значение не может содержать более двух знаков разделителя.", show_alert=True)
                await query.message.edit_text('Введите сумму:', reply_markup=nav.numeric_menu)
                return  # Снова не нужно обновлять сообщение или состояние
            await query.message.edit_text(row, reply_markup=nav.numeric_menu)
            await state.update_data(numeric_state=row)

    await query.answer()

# очистка введенных значений с клавиатуры
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_clear")
async def listen_callback(query: types.CallbackQuery, state: FSMContext):
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    # сбрасываем введенные значения
    await state.update_data(numeric_state='')
    await query.message.edit_text('Введите сумму:', reply_markup=nav.numeric_menu) 
    await query.answer()

# подтвержение введенных значений с клавиатуры
@keyboard_private_router.callback_query(lambda query: query.data == "numButton_ok")
async def listen_callback(query: types.CallbackQuery, state: FSMContext):
    
    callback_data = query.data
    print(f"Получен callback_data: {callback_data}")
    
    try:
        # сначала получаем то, что у нас в numeric_state
        # это значение вводилось пользователем с номерной 
        data = await state.get_data()
        row = data['numeric_state']
        print(f"Данные машины состояний на текущий момент:\n{data}")

        # Если строка оканчивается на точку, добавляем "0" в конец строки
        if row.endswith('.'):
            row += '0'
        price = float(row)

        # Проверка на нулевое значение: 
        if price == 0:
            await query.answer("Вы указали нулевое значение, в этом нет никакого смысла.", show_alert=True)
            await state.update_data(numeric_state='')
            await query.message.edit_text('Введите сумму:', reply_markup=nav.numeric_menu) 
            return  # Прекращаем дальнейшее выполнение обработчика
        
        # теперь записываем это значение в price для
        # передачи в базу данных, конвертируем в формат float
        await state.update_data(price = price)
        await state.update_data()
        await query.message.edit_text("Добавить описание \nзаписать в базу", reply_markup=nav.item_menu) 
    
    except ValueError:
        # не удалось преобразовать введенные данные, отправим сообщение пользователю
        await query.answer("Вы забыли указать стоимость.", show_alert=True)
        await state.update_data(numeric_state='')
        return  # прерываем выполнение функции и не записываем данные

    # Если исключения нет, значит преобразование прошло успешно, 
    # и мы можем продолжить дальнейшие действия
    # сбрасываем numeric_states, тут он нам не нужен
    await state.update_data(numeric_state=None) 
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
    await message.answer("Описание добавлено, \nРедактировать описание, \nзаписать в базу", reply_markup=nav.item_menu)

# Обработчик добавления записи в базу данных
@keyboard_private_router.callback_query(lambda query: query.data == "add_record")
# :param expense_item: статья расходов
# :param price: цена
# :param description: подробное описание
async def handle_callback(query: types.CallbackQuery, state: FSMContext):
     # Значение в машине состояний представлено в виде словарей
     # например {'description': 'Это тестовое сообщение'}
     # Записываем его в переменную для передачи в вывод через метод send.record()
    data = await state.get_data()
    print(f"Данные машины состояний на текущий момент:\n{data}")
    
    # название категории берем из словаря кнопок по ключу полученному из машины состояний
    # item = expense_buttons_text[data['item']]

    # Получаем название категории и убираем emoji
    raw_item = expense_buttons_text[data['item']]
    # Регулярное выражение для поиска и удаления emoji
    import re
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F700-\U0001F77F"  # alchemical symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                           u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           u"\U00002702-\U000027B0"  # Dingbats
                           u"\U000024C2-\U0001F251" 
                           "]+", flags=re.UNICODE)
    
    item = emoji_pattern.sub(r'', raw_item)  # Заменяем найденные emoji на пустую строку
    # убираем пробелы в начале и в конце строки
    item = item.strip() 
    # Вытаскиваем остальные значения  по ключу из машины состояний
    description = data['description']
    # также убираем пробелы для строки описания
    description = description.strip()
    price = data['price']
    
    # формирование записи 
    new_record = NewRecord(expense_item=item,  description=description, price=price)
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
