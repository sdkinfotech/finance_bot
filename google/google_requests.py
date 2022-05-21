import os
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from google.logs import RowNum
from google.logs import LogFile

from pprint import pprint

script_dir = os.path.dirname(__file__)
row_file = os.path.join(script_dir, 'row.txt')


class WriteData:
    """
     экземпляр класса который записывает инормацию об объекте record в google sheets
     при создании экземпляра класса также осуществляется запись объекта record в лог
     creds_file: принимает ключ из JSON
     google_sheet_key: принимает ID таблицы
     record: принимает экземпляр класса NewRecord
    """

    def __init__(self, creds_file, google_sheet_key, record):
        # создает экземпляр класса rowNom порядковыйномер строки
        row_num = RowNum(row_file)
        # метод считывает последний номер строки
        row = row_num.get_index()
        # формирует строку которая определяет диапазон ячеек и номер строки в таблице
        range_sheet = "A" + str(row + 1) + ":" + "H" + str(row + 1)

        # заполнение ячеек из create_rec_object
        self.cells = {
            'id': row,
            'date': record.date,
            'time': record.time,
            'expense_item': record.expense_item,
            'item': record.item,
            'description': record.description,
            'price': record.price,
            'simbol': record.simbol
        }
        print("Crete cells items")

        # подключение к таблице  google

        self.creds_file = creds_file
        self.google_sheet_key = google_sheet_key

        CREDITIANS_FILE = self.creds_file
        spreadsheet_id = self.google_sheet_key

        # тут я использовал код из примера c сайта гугла
        credentianls = ServiceAccountCredentials. \
            from_json_keyfile_name(CREDITIANS_FILE,
                                   ['https://www.googleapis.com/auth/spreadsheets',
                                    'https://www.googleapis.com/auth/drive'])
        httpAuth = credentianls.authorize(httplib2.Http())
        service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

        # добавление данных в таблицу
        values = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    # заполняем ячейки
                    {"range": range_sheet,
                     "majorDimension": "ROWS",
                     "values":
                         [[self.cells['id'],
                           self.cells['date'],
                           self.cells['time'],
                           self.cells['expense_item'],
                           self.cells['item'],
                           self.cells['description'],
                           self.cells['price'],
                           self.cells['simbol'], ]]}]}).execute()
        print("Send object to google sheets")

        # перезаписываем файл row.txt с информацией о текущей строке
        row_num.update_row()
        # создаем объект с инфой для лог файла
        log_file = LogFile(self.cells)
        # перезаписываем лог файл
        log_file.update_log()


class ReadData:
    """
    класс формирует объект который осуществляет запрос в google sheets
    при помощи этого объекта данные из таблицы могут быть выведены в консоль
    """

    def __init__(self, creds_file, google_sheet_key):
        self.creds_file = creds_file
        self.google_sheet_key = google_sheet_key

        CREDITIANS_FILE = self.creds_file
        spreadsheet_id = self.google_sheet_key

        credentianls = ServiceAccountCredentials. \
            from_json_keyfile_name(CREDITIANS_FILE,
                                   ['https://www.googleapis.com/auth/spreadsheets',
                                    'https://www.googleapis.com/auth/drive'])

        httpAuth = credentianls.authorize(httplib2.Http())
        service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

        self.values = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='A1:H100',  # указываем диапазон
            majorDimension='ROWS').execute()

    def print_table(self, values):
        """
        метод для распечатки таблицы в консоль
        values: эквивалентны вскем значениям в таблце
        """
        pprint(values)
        exit()

