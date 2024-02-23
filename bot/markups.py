from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons
from buttons import expense_buttons



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

# Цифровая клавиатура для ввода суммы затрат
numeric_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='numButton_1'), 
     InlineKeyboardButton(text='2', callback_data='numButton_2'),
     InlineKeyboardButton(text='3', callback_data='numButton_3')],
    # Добавьте остальные кнопки аналогичным образом
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