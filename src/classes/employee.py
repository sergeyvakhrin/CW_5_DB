from dataclasses import dataclass


@dataclass
class Employee:
    """ Класс для работы с работодателями """
    employee_id: str
    name: str
    url: str
    alternate_url: str
    vacancies_url: str
    open_vacancies: int | str

