from src.classes.fileworker import ABCWorker


class DataBaseWorker(ABCWorker):
    """ Класс для заполнения базы данных """
    def __init__(self):
        """ Конструктор класса """
        pass

    def db_exists(self) -> bool:
        """ Проверяет наличие базы данных """

    def create_db(self):
        """ Создает Базу данных """
        pass

    def create_table_emp(self):
        """ Создает Таблицу Работодателей """
        pass

    def create_table_vac(self):
        """ Создает Таблицу Вакансий """
        pass

    def insert_emp(self):
        """ Заполняет Таблицу Работодателей """
        pass

    def insert_vac(self):
        """ Заполняет таблицу вакансий """
        pass

    def truncate_table(self) -> bool:
        """ Очищает таблицу от старых данных. Возвращает True, если успешно """
        pass

    def save_data(self): # TODO: вероятно не понядобится. А значит и не нужно будет наследоваться от ABCWorker
        pass

