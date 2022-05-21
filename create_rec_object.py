import datetime


class NewRecord:
    """
    создание нового объекта с полями для записи
    id: идентификатор строки записи. формируется автоматически с шагом 1 в logs.py
    date: фактическая дата в момент создания записи берется из системы
    time: фактическое время в момент создания записи берется из системы
    expense_item: статья расхода, выбирается из предустановленного списка пользоваетелм
    item: наименование объекта, определяется пользователем
    description: описание объекта, определяется пользователем
    price: стоимость объекта в денежных единицах, определяется пользователем
    simbol: знак денежной единицы. по умолчанию RUB. изменения не предусмотрены на данный момент
    """

    def __init__(self, price, expense_item, item='', description='', simbol='RUB'):
        self.date = str(datetime.datetime.now().date())
        self.time = str(datetime.datetime.now().time())[:-10]
        self.expense_item = expense_item
        self.item = item
        self.description = description
        self.price = price
        self.simbol = simbol
        print("Create object", self.item)
