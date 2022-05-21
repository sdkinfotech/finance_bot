from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import buttons
from buttons import expense_buttons

# тут создаются клавиатуры

mainMenu = InlineKeyboardMarkup(row_width=2)
expensesMenu = InlineKeyboardMarkup(row_width=2)
record_completed_menu = InlineKeyboardMarkup(row_width=2)
numeric_menu = InlineKeyboardMarkup(row_width=3)
item_menu = InlineKeyboardMarkup(row_width=3)

# экшн кнопки с названием text и вызовом callback_data для хендлеорв

button_add_new = InlineKeyboardButton(text=buttons.menu_buttons['add_new'], callback_data=buttons.add_new)
button_expense = InlineKeyboardButton(text=buttons.menu_buttons['expenses'], callback_data=buttons.expenses)
button_income = InlineKeyboardButton(text=buttons.menu_buttons['income'], callback_data=buttons.income)
button_back = InlineKeyboardButton(text=buttons.menu_buttons['back'], callback_data=buttons.back)

button_item = InlineKeyboardButton(text=buttons.menu_buttons['item'], callback_data=buttons.item_button)
button_descr = InlineKeyboardButton(text=buttons.menu_buttons['descr'], callback_data=buttons.descr_button)
button_add_record = InlineKeyboardButton(text=buttons.menu_buttons['add_record'], callback_data=buttons.add_record)

# кнопки для клавиатуры статьи  расходов

button1 = InlineKeyboardButton(text=expense_buttons['public_utilities'],
                               callback_data="expButton_public_utilities")

button2 = InlineKeyboardButton(text=expense_buttons['housing_Rent'],
                               callback_data="expButton_housing_Rent")

button3 = InlineKeyboardButton(text=expense_buttons['commission_payment'],
                               callback_data="expButton_commission_payment")

button4 = InlineKeyboardButton(text=expense_buttons['subscription_payment'],
                               callback_data="expButton_subscription_payment")

button5 = InlineKeyboardButton(text=expense_buttons['household_products'],
                               callback_data="expButton_household_products")

button6 = InlineKeyboardButton(text=expense_buttons['health'],
                               callback_data="expButton_health")

button7 = InlineKeyboardButton(text=expense_buttons['sport_fitness'],
                               callback_data="expButton_sport_fitness")

button8 = InlineKeyboardButton(text=expense_buttons['hygiene_cosmetics'],
                               callback_data="expButton_hygiene_cosmetics")
button9 = InlineKeyboardButton(text=expense_buttons['alcohol'],
                               callback_data="expButton_alcohol")

button10 = InlineKeyboardButton(text=expense_buttons['products'],
                                callback_data="expButton_products")

button11 = InlineKeyboardButton(text=expense_buttons['education'],
                                callback_data="expButton_education")

button12 = InlineKeyboardButton(text=expense_buttons['trading_business'],
                                callback_data="expButton_trading_business")

button13 = InlineKeyboardButton(text=expense_buttons['investment'],
                                callback_data="expButton_investment")

button14 = InlineKeyboardButton(text=expense_buttons['charity'],
                                callback_data="expButton_charity")

button15 = InlineKeyboardButton(text=expense_buttons['gifts'],
                                callback_data="expButton_gifts")

button16 = InlineKeyboardButton(text=expense_buttons['events'],
                                callback_data="expButton_events")

button17 = InlineKeyboardButton(text=expense_buttons['restaurants'],
                                callback_data="expButton_restaurants")

button18 = InlineKeyboardButton(text=expense_buttons['entertainments'],
                                callback_data="expButton_entertainments")

button19 = InlineKeyboardButton(text=expense_buttons['flight_Intercity'],
                                callback_data="expButton_flight_Intercity")

button20 = InlineKeyboardButton(text=expense_buttons['taxi'],
                                callback_data="expButton_taxi")

button21 = InlineKeyboardButton(text=expense_buttons['public_transport'],
                                callback_data="expButton_public_transport")

button22 = InlineKeyboardButton(text=expense_buttons['vehicle'],
                                callback_data="expButton_vehicle")

button23 = InlineKeyboardButton(text=expense_buttons['fuel'],
                                callback_data="expButton_fuel")

button24 = InlineKeyboardButton(text=expense_buttons['everyday_life_tech'],
                                callback_data="expButton_everyday_life_tech")

button25 = InlineKeyboardButton(text=expense_buttons['house_furniture_tools'],
                                callback_data="expButton_house_furniture_tools")

button26 = InlineKeyboardButton(text=expense_buttons['clothes_footwear'],
                                callback_data="expButton_clothes_footwear")

button27 = InlineKeyboardButton(text=expense_buttons['accessory'],
                                callback_data="expButton_accessory")

button28 = InlineKeyboardButton(text=expense_buttons['hand_tools'],
                                callback_data="expButton_hand_tools")

button29 = InlineKeyboardButton(text=expense_buttons['building_materials'],
                                callback_data="expButton_building_materials")

button30 = InlineKeyboardButton(text=expense_buttons['private_debt'],
                                callback_data="expButton_private_debt")

button31 = InlineKeyboardButton(text=expense_buttons['credit'],
                                callback_data="expButton_credit")

button32 = InlineKeyboardButton(text=expense_buttons['phone_Internet'],
                                callback_data="expButton_phone_Internet")

button33 = InlineKeyboardButton(text=expense_buttons['other'],
                                callback_data="expButton_other")

# клавиатура для ввода цифр  от 0 до 9 и разделитель
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
button_num_point = InlineKeyboardButton(text=',', callback_data='numButton_,')
button_num_clear = InlineKeyboardButton(text='↩️ Заново', callback_data='numButton_clear')
button_num_ok = InlineKeyboardButton(text='Готово ➡️', callback_data='numButton_ok')

# в этой части кнопки добавляются в клавиатуры созданные выше

# главное меню

mainMenu.insert(button_expense)
mainMenu.insert(button_income)

#  меню для ввода наименования описания и добавления записи

item_menu.insert(button_back)
item_menu.insert(button_item)
item_menu.insert(button_descr)
item_menu.insert(button_add_record)

# цифровая клавиатура для ввода ссуммы затрат

numeric_menu.insert(button_num_1)
numeric_menu.insert(button_num_2)
numeric_menu.insert(button_num_3)
numeric_menu.insert(button_num_4)
numeric_menu.insert(button_num_5)
numeric_menu.insert(button_num_6)
numeric_menu.insert(button_num_7)
numeric_menu.insert(button_num_8)
numeric_menu.insert(button_num_9)
numeric_menu.insert(button_num_0)
numeric_menu.insert(button_num_point)
numeric_menu.insert(button_num_clear)
numeric_menu.insert(button_back)
numeric_menu.insert(button_num_ok)

# меню выбора статьи расхода

expensesMenu.insert(button_back)
expensesMenu.insert(button1)
expensesMenu.insert(button2)
expensesMenu.insert(button3)
expensesMenu.insert(button4)
expensesMenu.insert(button5)
expensesMenu.insert(button6)
expensesMenu.insert(button7)
expensesMenu.insert(button8)
expensesMenu.insert(button9)
expensesMenu.insert(button10)
expensesMenu.insert(button11)
expensesMenu.insert(button12)
expensesMenu.insert(button13)
expensesMenu.insert(button14)
expensesMenu.insert(button15)
expensesMenu.insert(button16)
expensesMenu.insert(button17)
expensesMenu.insert(button18)
expensesMenu.insert(button19)
expensesMenu.insert(button20)
expensesMenu.insert(button21)
expensesMenu.insert(button22)
expensesMenu.insert(button23)
expensesMenu.insert(button24)
expensesMenu.insert(button25)
expensesMenu.insert(button26)
expensesMenu.insert(button27)
expensesMenu.insert(button28)
expensesMenu.insert(button29)
expensesMenu.insert(button30)
expensesMenu.insert(button31)
expensesMenu.insert(button32)
expensesMenu.insert(button33)
