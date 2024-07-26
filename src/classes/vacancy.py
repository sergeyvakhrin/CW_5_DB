from dataclasses import dataclass


@dataclass
class Vacancy:
    """ Класс для работы с вакансиями """
    employee_id: str
    vacancy_id: str
    name: str
    requirement: str
    responsibility: str
    link: str
    salary_from: int | str
    salary_to: int | str

