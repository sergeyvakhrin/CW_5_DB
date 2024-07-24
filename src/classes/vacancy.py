from dataclasses import dataclass


@dataclass
class Vacancy:
    """ Класс для работы с вакансиями """
    id_vac: str
    name: str
    requirement: str
    responsibility: str
    link: str
    salary_from: int | str
    salary_to: int | str

