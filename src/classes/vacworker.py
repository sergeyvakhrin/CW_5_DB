from src.classes.vacancy import Vacancy


class VacWorker:
    """ Класс для работы с объектами класса Vacancy
     Передаем объект Класса Employee
     Передаем список вакансий Работодателя
     """
    def get_vacancies(self, employee, vacancies: list) -> list:
        """ Получение спаска экземпляров Класса Вакансий """
        self.employee_id = employee.employee_id
        self.vacancies_list: list = []

        for vacancy in vacancies:

            vacancy_id = self.validation_data(vacancy.get("id", "Не указано"))
            name = self.validation_data(vacancy.get("name", "Не указано"))
            requirement = self.validation_data(vacancy.get("snippet").get("requirement", "Не указано")) \
                if isinstance(vacancy.get("snippet"), (dict, str, list, int, float)) else "Не указано"
            responsibility = self.validation_data(vacancy.get("snippet").get("responsibility", "Не указано")) \
                if isinstance(vacancy.get("snippet"), (dict, str, list, int, float)) else "Не указано"
            link = self.validation_data(vacancy.get("alternate_url", "Не указано"))
            salary_from = self.validation_data(vacancy.get("salary").get("from", "Не указано")) \
                if isinstance(vacancy.get("salary"), (dict, str, list, int, float)) else "Не указано"
            salary_to = self.validation_data(vacancy.get("salary").get("to", "Не указано")) \
                if isinstance(vacancy.get("salary"), (dict, str, list, int, float)) else "Не указано"

            self.vacancies_list.append(Vacancy(employee_id=self.employee_id,
                                              vacancy_id=vacancy_id,
                                              name=name,
                                              requirement=requirement,
                                              responsibility=responsibility,
                                              link=link,
                                              salary_from=salary_from,
                                              salary_to=salary_to))

        return self.vacancies_list

    def validation_data(self, valid_data):
        """ Метод для замены значения None на иное значение """
        return valid_data if valid_data is not None else "Не указано"
