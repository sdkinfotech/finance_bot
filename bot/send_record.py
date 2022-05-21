from google import actions


def send_record(expense_item, price, item='', description=''):
    """
    :param expense_item: статья расходов
    :param price: цена
    :param item: наименование товара
    :param description: подробное описание
    :return: none
    """
    # пересылаемый объект
    record = actions.add_record(expense_item=expense_item, price=price, item=item, description=description)

    # запись данных в таблицу
    actions.write_data(record)

