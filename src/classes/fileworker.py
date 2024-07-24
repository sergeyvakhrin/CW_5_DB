import json
from abc import ABC, abstractmethod

from config import EMPLOYEE_PATH


class ABCFileWorker(ABC):
    """ Абстрактный класс для сохранения данных """
    def save_data(self):
        pass


class FileWorker(ABCFileWorker):
    """ Класс для работы с файлами """
    def __init__(self, data: list, path: str):
        self.data = data
        self.path = path

    def save_data(self):
        """ Сетод для сохранения полученных данных в файл в формате json """
        with open(self.path, 'wt', encoding="UTF-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
#
#
# a = [{'id': '5713306', 'name': 'BTS Python shoes', 'url': 'https://api.hh.ru/employers/5713306', 'alternate_url': 'https://hh.ru/employer/5713306', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/890820.jpg', '240': 'https://img.hhcdn.ru/employer-logo/4003968.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/4003967.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5713306', 'open_vacancies': 0}, {'id': '2219347', 'name': 'Luis Python', 'url': 'https://api.hh.ru/employers/2219347', 'alternate_url': 'https://hh.ru/employer/2219347', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2219347', 'open_vacancies': 0}, {'id': '97962', 'name': 'Python', 'url': 'https://api.hh.ru/employers/97962', 'alternate_url': 'https://hh.ru/employer/97962', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=97962', 'open_vacancies': 0}, {'id': '3115724', 'name': 'Python', 'url': 'https://api.hh.ru/employers/3115724', 'alternate_url': 'https://hh.ru/employer/3115724', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3115724', 'open_vacancies': 0}, {'id': '10347404', 'name': 'Python Flowers', 'url': 'https://api.hh.ru/employers/10347404', 'alternate_url': 'https://hh.ru/employer/10347404', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10347404', 'open_vacancies': 0}, {'id': '10467249', 'name': 'Python Flowers', 'url': 'https://api.hh.ru/employers/10467249', 'alternate_url': 'https://hh.ru/employer/10467249', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10467249', 'open_vacancies': 0}, {'id': '8940297', 'name': 'Частная компания Python RPA Ltd.', 'url': 'https://api.hh.ru/employers/8940297', 'alternate_url': 'https://hh.ru/employer/8940297', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1293673.png', '240': 'https://img.hhcdn.ru/employer-logo/6794987.png', '90': 'https://img.hhcdn.ru/employer-logo/6794986.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=8940297', 'open_vacancies': 2}, {'id': '4599861', 'name': 'Школа Python', 'url': 'https://api.hh.ru/employers/4599861', 'alternate_url': 'https://hh.ru/employer/4599861', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/734716.png', '240': 'https://img.hhcdn.ru/employer-logo/3379842.png', '90': 'https://img.hhcdn.ru/employer-logo/3379841.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4599861', 'open_vacancies': 0}]
#
#
# fw = FileWorker(a, EMPLOYEE_PATH)
# fw.save_data()
