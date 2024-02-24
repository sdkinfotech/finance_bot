from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import common.text as text
from common.text import expense_buttons_text

# экшн кнопки 
button_add_new = InlineKeyboardButton(text=text.menu_buttons_text['add_new'], callback_data=text.add_new)
button_expense = InlineKeyboardButton(text=text.menu_buttons_text['expenses'], callback_data=text.expenses)
button_income = InlineKeyboardButton(text=text.menu_buttons_text['income'], callback_data=text.income)
button_back = InlineKeyboardButton(text=text.menu_buttons_text['back'], callback_data=text.back)

# Определение кнопок для главного меню, используя словарь expense_buttons
button_expenses = InlineKeyboardButton(text=text.menu_buttons_text['expenses'], callback_data=text.expenses)
button_income = InlineKeyboardButton(text=text.menu_buttons_text['income'], callback_data=text.income)
# Главное меню
mainMenu = InlineKeyboardMarkup(inline_keyboard=[
    [button_expenses],
    [button_income]
])

# Определение кнопок меню добавления записи
button_item = InlineKeyboardButton(text=text.menu_buttons_text['item'], callback_data=text.item_button)
button_descr = InlineKeyboardButton(text=text.menu_buttons_text['descr'], callback_data=text.descr_button)
button_add_record = InlineKeyboardButton(text=text.menu_buttons_text['add_record'], callback_data=text.add_record)
# клавиатура для добавления записи
item_menu = InlineKeyboardMarkup(inline_keyboard=[
    
    [button_back],
    [button_item], 
    [button_descr],
    [button_add_record]
])

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

# Определение кнопок для клавиатуры статьи расходов, используя словарь expense_buttons
button_public_utilities = InlineKeyboardButton(text=text.expense_buttons_text['public_utilities'], callback_data="expButton_public_utilities")
button_housing_rent = InlineKeyboardButton(text=text.expense_buttons_text['housing_Rent'], callback_data="expButton_housing_Rent")
button_commission_payment = InlineKeyboardButton(text=text.expense_buttons_text['commission_payment'], callback_data="expButton_commission_payment")
button_subscription_payment = InlineKeyboardButton(text=text.expense_buttons_text['subscription_payment'], callback_data="expButton_subscription_payment")
button_household_products = InlineKeyboardButton(text=text.expense_buttons_text['household_products'], callback_data="expButton_household_products")
button_health = InlineKeyboardButton(text=text.expense_buttons_text['health'], callback_data="expButton_health")
button_sport_fitness = InlineKeyboardButton(text=text.expense_buttons_text['sport_fitness'], callback_data="expButton_sport_fitness")
button_hygiene_cosmetics = InlineKeyboardButton(text=text.expense_buttons_text['hygiene_cosmetics'], callback_data="expButton_hygiene_cosmetics")
button_alcohol = InlineKeyboardButton(text=text.expense_buttons_text['alcohol'], callback_data="expButton_alcohol")
button_products = InlineKeyboardButton(text=text.expense_buttons_text['products'], callback_data="expButton_products")
button_education = InlineKeyboardButton(text=text.expense_buttons_text['education'], callback_data="expButton_education")
button_trading_business = InlineKeyboardButton(text=text.expense_buttons_text['trading_business'], callback_data="expButton_trading_business")
button_investment = InlineKeyboardButton(text=text.expense_buttons_text['investment'], callback_data="expButton_investment")
button_charity = InlineKeyboardButton(text=text.expense_buttons_text['charity'], callback_data="expButton_charity")
button_gifts = InlineKeyboardButton(text=text.expense_buttons_text['gifts'], callback_data="expButton_gifts")
button_events = InlineKeyboardButton(text=text.expense_buttons_text['events'], callback_data="expButton_events")
button_restaurants = InlineKeyboardButton(text=text.expense_buttons_text['restaurants'], callback_data="expButton_restaurants")
button_entertainments = InlineKeyboardButton(text=text.expense_buttons_text['entertainments'], callback_data="expButton_entertainments")
button_flight_intercity = InlineKeyboardButton(text=text.expense_buttons_text['flight_Intercity'], callback_data="expButton_flight_Intercity")
button_taxi = InlineKeyboardButton(text=text.expense_buttons_text['taxi'], callback_data="expButton_taxi")
button_public_transport = InlineKeyboardButton(text=text.expense_buttons_text['public_transport'], callback_data="expButton_public_transport")
button_vehicle = InlineKeyboardButton(text=text.expense_buttons_text['vehicle'], callback_data="expButton_vehicle")
button_fuel = InlineKeyboardButton(text=text.expense_buttons_text['fuel'], callback_data="expButton_fuel")
button_everyday_life_tech = InlineKeyboardButton(text=text.expense_buttons_text['everyday_life_tech'], callback_data="expButton_everyday_life_tech")
button_house_furniture_tools = InlineKeyboardButton(text=text.expense_buttons_text['house_furniture_tools'], callback_data="expButton_house_furniture_tools")
button_clothes_footwear = InlineKeyboardButton(text=text.expense_buttons_text['clothes_footwear'], callback_data="expButton_clothes_footwear")
button_accessory = InlineKeyboardButton(text=text.expense_buttons_text['accessory'], callback_data="expButton_accessory")
button_hand_tools = InlineKeyboardButton(text=text.expense_buttons_text['hand_tools'], callback_data="expButton_hand_tools")
button_building_materials = InlineKeyboardButton(text=text.expense_buttons_text['building_materials'], callback_data="expButton_building_materials")
button_private_debt = InlineKeyboardButton(text=text.expense_buttons_text['private_debt'], callback_data="expButton_private_debt")
button_credit = InlineKeyboardButton(text=text.expense_buttons_text['credit'], callback_data="expButton_credit")
button_phone_internet = InlineKeyboardButton(text=text.expense_buttons_text['phone_Internet'], callback_data="expButton_phone_Internet")
button_other = InlineKeyboardButton(text=text.expense_buttons_text['other'], callback_data="expButton_other")
# Клавиатура с кнопками статей расходов
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

