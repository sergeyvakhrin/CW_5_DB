from abc import ABC, abstractmethod

import requests


class APIRequests(ABC):
    """ Абстрактный метод для наследования классами запросов """

    @abstractmethod
    def __init__(self):
        pass

    def get_api(self):
        pass


class HH(APIRequests):
    """ Класс для API запроса """
    def __init__(self, keyword=''):
        self.url = 'https://api.hh.ru/employers/'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_vacancies': False, 'sort_by': 'by_name'}
        self.employers_list = []
        self.params['text'] = keyword

    def get_api(self):
        """ Метод для отправки API запроса """
        while self.params['page'] != 20:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            employers = response.json()['items']
            self.employers_list.extend(employers)
            self.params['page'] += 1
        return self.employers_list


