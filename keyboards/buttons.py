"""
Модуль используется для хранения значений 
кнопок для кдавиатуры. Также тут могут 
храниться коллбэки для удобства
"""

# Словарь с названиями кнопок и соответствующими emoji
# Используется для клавиатуры, отображающей категории расходов
expense_buttons_text = {
    'public_utilities': '🏠 Комм.услуги',
    'housing_Rent': '🏘 аренда',
    'phone_Internet': '📱 тел.интернет',
    'commission_payment': '💸 комиссионные',
    'subscription_payment': '📺 абонентсая плата',
    'household_products': '🛍 товары для дома',
    'health': '🩺 здоровье',
    'sport_fitness': '🏋️ спорт и фитнес',
    'hygiene_cosmetics': '💄 гигиена, косметика',
    'alcohol': '🍷 алкоголь',
    'products': '🛒 продукты питания',
    'education': '🎓 образование',
    'trading_business': '📈 трейдинг, бизнес',
    'investment': '💰 инвестиции',
    'charity': '❤️ благотворительность',
    'gifts': '🎁 подарки',
    'events': '🎫 события',
    'restaurants': '🍽 рестораны, кафе',
    'entertainments': '🎢 развлечения',
    'flight_Intercity': '✈️ авиа, межгород. транспорт',
    'taxi': '🚕 такси',
    'public_transport': '🚌 общественный транспорт',
    'vehicle': '🚗 автотранспорт',
    'fuel': '⛽ топливо',
    'everyday_life_tech': '🖥 бытовая техника',
    'house_furniture_tools': '🛏 мебель,предметы для дома',
    'clothes_footwear': '👕 одежда, обувь',
    'accessory': '👜 аксесуары',
    'hand_tools': '🛠 ручные инструменты',
    'building_materials': '🧱 стройматериалы',
    'private_debt': '💵 частный займ',
    'credit': '💳 банковский кредит',
    'other': '🔖 прочие'
}

menu_buttons_text = {
    'add_new': '📝 Добавить',
    'expenses': '💵 Расходы',
    'income': '💰 Доходы',
    'back': '⬅️ Домой',
    'descr':'🗒️ Редактировать описание',
    'add_record': '✏️ Записать в базу'
}

# menu_buttons для обработки call.data
# приложение к предыдущему блоку
ADD_NEW = 'add_new'
EXPENSES = 'expenses'
INCOME = 'income'
BACK = 'back'
ITEM_BUTTON = 'item'
DESCR_BUTTON = 'description'
ADD_RECORD = 'add_record'
