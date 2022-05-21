from create_rec_object import NewRecord
from google.key import api_key
from google import google_requests


def add_record(expense_item, price, item='none', description='none'):
    """
    принимает значения для заполнения полей записи
    item: наименование товара
    expense_item: статья расхода
    price: цена товара
    description: описание товара
    переменная record содержит новый экземпляр класса NewRecord
    Далее метод возвращает созданный объект
    """
    record = NewRecord(expense_item=expense_item, price=price, item=item, description=description)
    return record


def write_data(record):
    """
    создает  write, при создании которого происходит
    отправка запроса на запись объекта create_rec_object в google sheets
    record: экземляр класса create_rec_object
    creds_file принимает ключ из файла json
    google_sheets_key принимает ID таблицы.
    api_key находится в файле key.py
    """
    write = google_requests.WriteData(creds_file=api_key['json'],
                                      google_sheet_key=api_key['sheet'],
                                      record=record)
    return write


def read_data():
    """
    метод создает экземпляр класса ReadData при вызове которого
    происходит запрос на вывод данных из таблицы google sheets в консоль
    creds_file принимает ключ из файла json
    google_sheets_key принимает ID таблицы.
    переменная api_key с ключами находится файле key.py
    """
    read = google_requests.ReadData(creds_file=api_key['json'],
                                    google_sheet_key=api_key['sheet'])
    return read
