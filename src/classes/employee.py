from dataclasses import dataclass

from src.classes.api_request import HH


@dataclass
class Employee:
    """ Класс для работы с работодателями """
    employee_id: str
    name: str
    url: str
    alternate_url: str
    vacancies_url: str
    open_vacancies: int

    def get_vacansies(self) -> list:
        api_request = HH(self.vacancies_url)
        vacancies_list = api_request.get_api()
        return vacancies_list


#
# emp = Employee("8940297", "Частная компания Python RPA Ltd.", "https://api.hh.ru/employers/8940297",
#                "https://hh.ru/employer/8940297", "https://api.hh.ru/vacancies?employer_id=8940297", 2)
#
# a = emp.get_vacansies()
#
# print(len(a))
# print(a)