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
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_vacancies': False, 'sort_by': 'by_name'}
        self.data_list = []
        self.url = url
        self.params['text'] = keyword

    def get_api(self) -> list[dict]:
        """ Метод для отправки API запроса на HH.ru"""

        while self.params['page'] != 20:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            data = response.json()['items']
            # data = response.json()
            # print(data)

            self.data_list.extend(data)
            self.params['page'] += 1
        return self.data_list

#