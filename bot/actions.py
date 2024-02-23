class NewRecord:
    """
    Используется для формирования объекта, переданного из телеграм канала, 

    Принимаемые значения:
    date: фактическая дата в момент создания записи берется из системы
    time: фактическое время в момент создания записи берется из системы
    expense_item: статья расхода, выбирается из предустановленного списка пользоваетелм
    item: наименование объекта, определяется пользователем
    description: описание объекта, определяется пользователем
    price: стоимость объекта в денежных единицах, определяется пользователем
    simbol: знак денежной единицы. по умолчанию RUB. изменения не предусмотрены на данный момент

    Методы:
    __init__ - инициализация экземпляра класса, определяем переменные внутри класса.
    send_record - Осуществляет запиь строки в БД
    """

    def __init__(self, price, expense_item, item='', description='', simbol='RUB'):
     
        self.expense_item = expense_item
        self.item = item
        self.description = description
        self.price = price
        self.simbol = simbol
        print("Create object", self.item)


    def send_record(self):
        """
        :param expense_item: статья расходов
        :param price: цена
        :param item: наименование товара
        :param description: подробное описание
        """
        # отладочная информация
        # нужно убедиться, что данные получены верно из телеграм бота.
        print(self.expense_item, self.price, self.item, self.description, self.simbol)

