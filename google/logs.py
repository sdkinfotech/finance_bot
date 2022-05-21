from collections import deque
import os


script_dir = os.path.dirname(__file__)
row_file = os.path.join(script_dir, 'row.txt')


class RowNum:

    """
    Запоминает позицию в google таблице
    Построчно сверху вниз. Обновляет значение
    после каждой новой записи
    """

    def __init__(self, row):
        self.row = row
        pass

    def update_row(self):
        next_id = self.get_index()
        with open(row_file, 'a') as file:
            file.write('\n')
            file.write('#' + str(next_id))
            # отладочное сообщение
            print("Write ROW #", next_id)

    def get_index(self):
        with open(self.row, 'r') as f:
            [last_line] = deque(f, maxlen=1) or ['']
            current_id = int(last_line[1:])
            next_id = current_id + 1
            return next_id


class LogFile:

    """
    Формирует поля для записи лога
    и записывает их методом update_log
    """

    def __init__(self, record):
        self.id = record['id']
        self.date = record['date']
        self.time = record['time']
        self.expense_item = record['expense_item']
        self.item = record['item']
        self.description = record['description']
        self.price = record['price']
        self.simbol = record['simbol']

    def update_log(self):
        """
        Записывает лог в файл. В логе содержится
        информация о записи статьи расхода.
        """
        with open('log.txt', 'a') as file:
            file.write('#' +
                       ' ' + str(self.id) +
                       ' ' + str(self.date) +
                       ' ' + str(self.time) +
                       ' ' + str(self.expense_item) +
                       ' ' + str(self.item) +
                       ' ' + str(self.description) +
                       ' ' + str(self.price) +
                       ' ' + str(self.simbol))
            file.write('\n')
            print("Update log.txt file")
