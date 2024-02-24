from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons
from buttons import expense_buttons

# экшн кнопки 
button_add_new = InlineKeyboardButton(text=buttons.menu_buttons['add_new'], callback_data=buttons.add_new)
button_expense = InlineKeyboardButton(text=buttons.menu_buttons['expenses'], callback_data=buttons.expenses)
button_income = InlineKeyboardButton(text=buttons.menu_buttons['income'], callback_data=buttons.income)
button_back = InlineKeyboardButton(text=buttons.menu_buttons['back'], callback_data=buttons.back)

# Определение кнопок для главного меню, используя словарь expense_buttons
button_expenses = InlineKeyboardButton(text=buttons.menu_buttons['expenses'], callback_data=buttons.expenses)
button_income = InlineKeyboardButton(text=buttons.menu_buttons['income'], callback_data=buttons.income)
# Главное меню
mainMenu = InlineKeyboardMarkup(inline_keyboard=[
    [button_expenses],
    [button_income]
])

# Определение кнопок меню добавления записи
button_item = InlineKeyboardButton(text=buttons.menu_buttons['item'], callback_data=buttons.item_button)
button_descr = InlineKeyboardButton(text=buttons.menu_buttons['descr'], callback_data=buttons.descr_button)
button_add_record = InlineKeyboardButton(text=buttons.menu_buttons['add_record'], callback_data=buttons.add_record)
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
button_public_utilities = InlineKeyboardButton(text=buttons.expense_buttons['public_utilities'], callback_data="expButton_public_utilities")
button_housing_rent = InlineKeyboardButton(text=buttons.expense_buttons['housing_Rent'], callback_data="expButton_housing_Rent")
button_commission_payment = InlineKeyboardButton(text=buttons.expense_buttons['commission_payment'], callback_data="expButton_commission_payment")
button_subscription_payment = InlineKeyboardButton(text=buttons.expense_buttons['subscription_payment'], callback_data="expButton_subscription_payment")
button_household_products = InlineKeyboardButton(text=buttons.expense_buttons['household_products'], callback_data="expButton_household_products")
button_health = InlineKeyboardButton(text=buttons.expense_buttons['health'], callback_data="expButton_health")
button_sport_fitness = InlineKeyboardButton(text=buttons.expense_buttons['sport_fitness'], callback_data="expButton_sport_fitness")
button_hygiene_cosmetics = InlineKeyboardButton(text=buttons.expense_buttons['hygiene_cosmetics'], callback_data="expButton_hygiene_cosmetics")
button_alcohol = InlineKeyboardButton(text=buttons.expense_buttons['alcohol'], callback_data="expButton_alcohol")
button_products = InlineKeyboardButton(text=buttons.expense_buttons['products'], callback_data="expButton_products")
button_education = InlineKeyboardButton(text=buttons.expense_buttons['education'], callback_data="expButton_education")
button_trading_business = InlineKeyboardButton(text=buttons.expense_buttons['trading_business'], callback_data="expButton_trading_business")
button_investment = InlineKeyboardButton(text=buttons.expense_buttons['investment'], callback_data="expButton_investment")
button_charity = InlineKeyboardButton(text=buttons.expense_buttons['charity'], callback_data="expButton_charity")
button_gifts = InlineKeyboardButton(text=buttons.expense_buttons['gifts'], callback_data="expButton_gifts")
button_events = InlineKeyboardButton(text=buttons.expense_buttons['events'], callback_data="expButton_events")
button_restaurants = InlineKeyboardButton(text=buttons.expense_buttons['restaurants'], callback_data="expButton_restaurants")
button_entertainments = InlineKeyboardButton(text=buttons.expense_buttons['entertainments'], callback_data="expButton_entertainments")
button_flight_intercity = InlineKeyboardButton(text=buttons.expense_buttons['flight_Intercity'], callback_data="expButton_flight_Intercity")
button_taxi = InlineKeyboardButton(text=buttons.expense_buttons['taxi'], callback_data="expButton_taxi")
button_public_transport = InlineKeyboardButton(text=buttons.expense_buttons['public_transport'], callback_data="expButton_public_transport")
button_vehicle = InlineKeyboardButton(text=buttons.expense_buttons['vehicle'], callback_data="expButton_vehicle")
button_fuel = InlineKeyboardButton(text=buttons.expense_buttons['fuel'], callback_data="expButton_fuel")
button_everyday_life_tech = InlineKeyboardButton(text=buttons.expense_buttons['everyday_life_tech'], callback_data="expButton_everyday_life_tech")
button_house_furniture_tools = InlineKeyboardButton(text=buttons.expense_buttons['house_furniture_tools'], callback_data="expButton_house_furniture_tools")
button_clothes_footwear = InlineKeyboardButton(text=buttons.expense_buttons['clothes_footwear'], callback_data="expButton_clothes_footwear")
button_accessory = InlineKeyboardButton(text=buttons.expense_buttons['accessory'], callback_data="expButton_accessory")
button_hand_tools = InlineKeyboardButton(text=buttons.expense_buttons['hand_tools'], callback_data="expButton_hand_tools")
button_building_materials = InlineKeyboardButton(text=buttons.expense_buttons['building_materials'], callback_data="expButton_building_materials")
button_private_debt = InlineKeyboardButton(text=buttons.expense_buttons['private_debt'], callback_data="expButton_private_debt")
button_credit = InlineKeyboardButton(text=buttons.expense_buttons['credit'], callback_data="expButton_credit")
button_phone_internet = InlineKeyboardButton(text=buttons.expense_buttons['phone_Internet'], callback_data="expButton_phone_Internet")
button_other = InlineKeyboardButton(text=buttons.expense_buttons['other'], callback_data="expButton_other")
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

