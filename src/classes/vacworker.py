from src.classes.vacancy import Vacancy


class VacWorker:
    """ Класс для работы с объектами класса Vacancy
     Передаем объект Класса Employee
     Передаем список вакансий Работодателя
     """
    def get_vacancies(self, employee, vacancies: list) -> list:
        """ Получение спаска экземпляров Класса Вакансий """
        self.employee_id = employee.employee_id
        vacancies_list: list = []
        for vacancy in vacancies:

                vacancy_id = vacancy.get("id", "Не задано")
                name = vacancy.get("name", "Не задано")
                requirement = vacancy.get("snippet", {}).get("requirement", "Не задано")
                responsibility = vacancy.get("snippet", {}).get("responsibility", "Не задано")
                link = vacancy.get("alternate_url", "Не задано")
                salary_from = vacancy.get("salary", {}).get("from", "Не задано")
                salary_to = vacancy.get("salary", {}).get("to", "Не задано")

                vacancies_list.append(Vacancy(employee_id=self.employee_id,
                                              vacancy_id=vacancy_id,
                                              name=name,
                                              requirement=requirement,
                                              responsibility=responsibility,
                                              link=link,
                                              salary_from=salary_from,
                                              salary_to=salary_to))

        return vacancies_list

