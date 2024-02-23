from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons
from buttons import expense_buttons

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
    [button_num_ok]
])


# Главное меню
mainMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=buttons.menu_buttons['expenses'], callback_data=buttons.expenses)],
    [InlineKeyboardButton(text=buttons.menu_buttons['income'], callback_data=buttons.income)],
])

# Меню для ввода наименования, описания и добавления записи
item_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=buttons.menu_buttons['item'], callback_data=buttons.item_button)],
    [InlineKeyboardButton(text=buttons.menu_buttons['descr'], callback_data=buttons.descr_button)],
    [InlineKeyboardButton(text=buttons.menu_buttons['add_record'], callback_data=buttons.add_record)],
    [InlineKeyboardButton(text=buttons.menu_buttons['back'], callback_data=buttons.back)]
])


# Меню выбора статьи расхода - в этом случае у вас будет много кнопок,
# и вы можете организовать их в несколько рядов.
expensesMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=expense_buttons['public_utilities'], callback_data="expButton_public_utilities"),
     InlineKeyboardButton(text=expense_buttons['housing_Rent'], callback_data="expButton_housing_Rent")],
    # Добавляйте кнопки в новых рядах по мере необходимости
    # ...
])

# Продолжайте организовывать остальные кнопки в ряды по аналогии