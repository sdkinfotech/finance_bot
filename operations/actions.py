"""
Модуль содержит классы для оперативного 
функционирования бэкенд части бота.
В этом модуле описаны действия, которые бот 
выполняет после получения данных, или до их получения.
"""
import dataclasses

@dataclasses.dataclass
class NewRecord:
    """
    Используется для формирования объекта, переданного из телеграм канала, 

    Принимаемые значения:
    date: фактическая дата в момент создания записи берется из системы
    time: фактическое время в момент создания записи берется из системы
    expense_item: статья расхода, выбирается из предустановленного списка пользоваетелм
    item: наименование объекта, определяется автоматически при выборе категории
    description: описание объекта, определяется пользователем
    price: стоимость объекта в денежных единицах, определяется пользователем
    simbol: знак денежной единицы. по умолчанию RUB. изменения не предусмотрены на данный момент

    Методы:
    __init__ - инициализация экземпляра класса, определяем переменные внутри класса.
    send_record - Осуществляет запиь строки в БД
    """

    def __init__(self, price, expense_item, description='', simbol='RUB'):
        self.expense_item = expense_item
        self.description = description
        self.price = price
        self.simbol = simbol
        print("Create object", self.expense_item, self.price, self.simbol)

    def send_record(self):
        """
        :param expense_item: статья расходов
        :param price: цена
        :param description: описание
        """
        # отладочная информация
        # нужно убедиться, что данные получены верно из телеграм бота.
        # для этого в консоль выводим debug_info строку
        debug_info = f"\
            Категория расходов:{self.expense_item}\n\
            Описание:{self.description}\n\
            Cтоимость:{self.price}\n\
            Валюта:{self.simbol}"
        print(debug_info)
