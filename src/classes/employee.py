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
    open_vacancies: int | str

    def get_employres(self, employers) -> list:
        """ Получение спаска экземпляров Класса Работодателей """
        employers_list: list = []
        for employer in employers:
            if isinstance(employer, dict):
                employers_list.append(Employee(employee_id=employer.get('id', "Не задано"),
                                               name=employer.get('name', "Не задано"),
                                               url=employer.get('url', "Не задано"),
                                               alternate_url=employer.get('alternate_url', "Не задано"),
                                               vacancies_url=employer.get('vacancies_urlid', "Не задано"),
                                               open_vacancies=employer.get('open_vacancie', "Не задано")))
            else:
                continue
        return employers_list

    def get_vacansies(self) -> list[dict]:
        """ Отдает список вакансий работодателя """
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