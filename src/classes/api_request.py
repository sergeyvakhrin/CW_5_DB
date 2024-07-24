from abc import ABC, abstractmethod

import requests


class APIRequests(ABC):
    """ Абстрактный метод для наследования классами запросов """

    @abstractmethod
    def get_api(self):
        pass


class HH(APIRequests):
    """ Класс для API запроса на HH.ru """
    def __init__(self, url, keyword=""):
        self.url = url
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_vacancies': False, 'sort_by': 'by_name'}
        self.employers_list = []
        self.params['text'] = keyword

    def get_api(self):
        """ Метод для отправки API запроса на HH.ru"""
        while self.params['page'] != 20:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            employers = response.json()['items']
            self.employers_list.extend(employers)
            self.params['page'] += 1
        return self.employers_list

#
# hh = HH('https://api.hh.ru/employers/', 'python')
# a = hh.get_api()
#
# print(type(a))
# print(a)