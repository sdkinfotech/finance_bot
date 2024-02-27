from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import common.bot_text as bot_text
from common.bot_text import expense_buttons_text

### ЭКШН КНОПКИ

# экшн кнопки 
button_add_new = InlineKeyboardButton(text=bot_text.menu_buttons_text['add_new'], callback_data=bot_text.add_new)
button_expense = InlineKeyboardButton(text=bot_text.menu_buttons_text['expenses'], callback_data=bot_text.expenses)
button_income = InlineKeyboardButton(text=bot_text.menu_buttons_text['income'], callback_data=bot_text.income)
button_back = InlineKeyboardButton(text=bot_text.menu_buttons_text['back'], callback_data=bot_text.back)


### КНОПКИ ГЛАВНОГО МЕНЮ

# Определение кнопок для главного меню, используя словарь expense_buttons
button_expenses = InlineKeyboardButton(text=bot_text.menu_buttons_text['expenses'], callback_data=bot_text.expenses)
button_income = InlineKeyboardButton(text=bot_text.menu_buttons_text['income'], callback_data=bot_text.income)
# Главное меню
mainMenu = InlineKeyboardMarkup(inline_keyboard=[
    [button_expenses],
    [button_income]
])

# Определение кнопок меню добавления записи
# button_item = InlineKeyboardButton(text=bot_text.menu_buttons_text['item'], callback_data=bot_text.item_button)
button_descr = InlineKeyboardButton(text=bot_text.menu_buttons_text['descr'], callback_data=bot_text.descr_button)
button_add_record = InlineKeyboardButton(text=bot_text.menu_buttons_text['add_record'], callback_data=bot_text.add_record)

# клавиатура для добавления записи
item_menu = InlineKeyboardMarkup(inline_keyboard=[
    
    [button_back],
  # [button_item], 
    [button_descr],
    [button_add_record]
])

### КНОПКИ ВВОДА ЦЕНЫ

# Определение кнопок для цифровой клавиатуры
button_num_1 = InlineKeyboardButton(text='1', callback_data='numButton_1')
button_num_2 = InlineKeyboardButton(text='2', callback_data='numButton_2')
button_num_3 = InlineKeyboardButton(text='3', callback_data='numButton_3')
button_num_4 = InlineKeyboardButton(text='4', callback_data='numButton_4')
button_num_5 = InlineKeyboardButton(text='5', callback_data='numButton_5')
button_num_6 = InlineKeyboardButton(text='6', callback_data='numButton_6')
button_num_7 = InlineKeyboardButton(text='7', callback_data='numButton_7')
button_num_8 = InlineKeyboardButton(text='8', callback_data='numButton_8')
button_num_9 = InlineKeyboardButton(text='9', callback_data='numButton_9')
button_num_0 = InlineKeyboardButton(text='0', callback_data='numButton_0')
button_num_point = InlineKeyboardButton(text=',', callback_data='numButton_point')
button_num_clear = InlineKeyboardButton(text='↩️ Заново', callback_data='numButton_clear')
button_num_ok = InlineKeyboardButton(text='Готово ➡️', callback_data='numButton_ok')

# Цифровая клавиатура для ввода суммы затрат
numeric_menu = InlineKeyboardMarkup(inline_keyboard=[
    [button_num_1, button_num_2, button_num_3],
    [button_num_4, button_num_5, button_num_6],
    [button_num_7, button_num_8, button_num_9],
    [button_num_clear, button_num_0, button_num_point],
    [button_back],[button_num_ok]
])


### КНОПКИ КАТЕГОРИЙ РАСХОДОВ

# Определение кнопок для клавиатуры, используя словарь expense_buttons, 
# В дальнейшем сдеаю через функцию формирования кнопок в цикле по словарю.

button_public_utilities = InlineKeyboardButton(text=bot_text.expense_buttons_text['public_utilities'], callback_data="public_utilities")
button_housing_rent = InlineKeyboardButton(text=bot_text.expense_buttons_text['housing_Rent'], callback_data="housing_Rent")
button_commission_payment = InlineKeyboardButton(text=bot_text.expense_buttons_text['commission_payment'], callback_data="commission_payment")
button_subscription_payment = InlineKeyboardButton(text=bot_text.expense_buttons_text['subscription_payment'], callback_data="subscription_payment")
button_household_products = InlineKeyboardButton(text=bot_text.expense_buttons_text['household_products'], callback_data="household_products")
button_health = InlineKeyboardButton(text=bot_text.expense_buttons_text['health'], callback_data="health")
button_sport_fitness = InlineKeyboardButton(text=bot_text.expense_buttons_text['sport_fitness'], callback_data="sport_fitness")
button_hygiene_cosmetics = InlineKeyboardButton(text=bot_text.expense_buttons_text['hygiene_cosmetics'], callback_data="hygiene_cosmetics")
button_alcohol = InlineKeyboardButton(text=bot_text.expense_buttons_text['alcohol'], callback_data="alcohol")
button_products = InlineKeyboardButton(text=bot_text.expense_buttons_text['products'], callback_data="products")
button_education = InlineKeyboardButton(text=bot_text.expense_buttons_text['education'], callback_data="education")
button_trading_business = InlineKeyboardButton(text=bot_text.expense_buttons_text['trading_business'], callback_data="trading_business")
button_investment = InlineKeyboardButton(text=bot_text.expense_buttons_text['investment'], callback_data="investment")
button_charity = InlineKeyboardButton(text=bot_text.expense_buttons_text['charity'], callback_data="charity")
button_gifts = InlineKeyboardButton(text=bot_text.expense_buttons_text['gifts'], callback_data="gifts")
button_events = InlineKeyboardButton(text=bot_text.expense_buttons_text['events'], callback_data="events")
button_restaurants = InlineKeyboardButton(text=bot_text.expense_buttons_text['restaurants'], callback_data="restaurants")
button_entertainments = InlineKeyboardButton(text=bot_text.expense_buttons_text['entertainments'], callback_data="entertainments")
button_flight_intercity = InlineKeyboardButton(text=bot_text.expense_buttons_text['flight_Intercity'], callback_data="flight_Intercity")
button_taxi = InlineKeyboardButton(text=bot_text.expense_buttons_text['taxi'], callback_data="taxi")
button_public_transport = InlineKeyboardButton(text=bot_text.expense_buttons_text['public_transport'], callback_data="public_transport")
button_vehicle = InlineKeyboardButton(text=bot_text.expense_buttons_text['vehicle'], callback_data="vehicle")
button_fuel = InlineKeyboardButton(text=bot_text.expense_buttons_text['fuel'], callback_data="fuel")
button_everyday_life_tech = InlineKeyboardButton(text=bot_text.expense_buttons_text['everyday_life_tech'], callback_data="everyday_life_tech")
button_house_furniture_tools = InlineKeyboardButton(text=bot_text.expense_buttons_text['house_furniture_tools'], callback_data="house_furniture_tools")
button_clothes_footwear = InlineKeyboardButton(text=bot_text.expense_buttons_text['clothes_footwear'], callback_data="clothes_footwear")
button_accessory = InlineKeyboardButton(text=bot_text.expense_buttons_text['accessory'], callback_data="accessory")
button_hand_tools = InlineKeyboardButton(text=bot_text.expense_buttons_text['hand_tools'], callback_data="hand_tools")
button_building_materials = InlineKeyboardButton(text=bot_text.expense_buttons_text['building_materials'], callback_data="building_materials")
button_private_debt = InlineKeyboardButton(text=bot_text.expense_buttons_text['private_debt'], callback_data="private_debt")
button_credit = InlineKeyboardButton(text=bot_text.expense_buttons_text['credit'], callback_data="credit")
button_phone_internet = InlineKeyboardButton(text=bot_text.expense_buttons_text['phone_Internet'], callback_data="phone_Internet")
button_other = InlineKeyboardButton(text=bot_text.expense_buttons_text['other'], callback_data="other")

# Клавиатура с кнопками статей расходов
# Маску клавиатуры возможно так и оставлю,
# В таком виде удобно управлять расположением

expense_buttons_markup = InlineKeyboardMarkup(inline_keyboard=[
    [button_back],
    [button_public_utilities, button_housing_rent],
    [button_commission_payment, button_subscription_payment],
    [button_household_products, button_health],
    [button_sport_fitness, button_hygiene_cosmetics],
    [button_alcohol, button_products],
    [button_education, button_trading_business],
    [button_investment, button_charity],
    [button_gifts, button_events],
    [button_restaurants, button_entertainments],
    [button_flight_intercity, button_taxi],
    [button_public_transport, button_vehicle],
    [button_fuel, button_everyday_life_tech],
    [button_house_furniture_tools, button_clothes_footwear],
    [button_accessory, button_hand_tools],
    [button_building_materials, button_private_debt],
    [button_credit, button_phone_internet],
    [button_other]
])

