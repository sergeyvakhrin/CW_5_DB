import json
from abc import ABC, abstractmethod

from config import EMPLOYEE_PATH


class ABCWorker(ABC):
    """ Абстрактный класс для сохранения данных """
    @abstractmethod
    def save_data(self, data: list, path: str, mode: str):
        pass


class FileWorker(ABCWorker):
    """ Класс для работы с файлами """
    def save_data(self, data: list, path: str, mode: str):
        """ Сетод для сохранения полученных данных в файл в формате json """
        self.data = data
        self.path = path
        self.mode = mode
        with open(self.path, self.mode, encoding="UTF-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)


