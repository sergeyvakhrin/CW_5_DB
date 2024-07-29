from src.classes.vacancy import Vacancy


class VacWorker:
    """ Класс для работы с объектами класса Vacancy
     Передаем объект Класса Employee
     Передаем список вакансий Работодателя
     """

    @classmethod
    def get_vacancies(cls, employee, vacancies: list) -> list:
        """ Получение спаска экземпляров Класса Вакансий """
        cls.employee_id = employee.hh_id
        cls.vacancies_list: list = []

        for vacancy in vacancies:
            hh_id = cls.validation_data(vacancy.get("id", "Не указано"))
            name = cls.validation_data(vacancy.get("name", "Не указано"))
            requirement = cls.validation_data(vacancy.get("snippet").get("requirement", "Не указано")) \
                if isinstance(vacancy.get("snippet"), (dict, str, list, int, float)) else "Не указано"
            responsibility = cls.validation_data(vacancy.get("snippet").get("responsibility", "Не указано")) \
                if isinstance(vacancy.get("snippet"), (dict, str, list, int, float)) else "Не указано"
            link = cls.validation_data(vacancy.get("alternate_url", "Не указано"))
            salary_from = cls.validation_data(vacancy.get("salary").get("from", "Не указано")) \
                if isinstance(vacancy.get("salary"), (dict, str, list, int, float)) else "Не указано"
            salary_to = cls.validation_data(vacancy.get("salary").get("to", "Не указано")) \
                if isinstance(vacancy.get("salary"), (dict, str, list, int, float)) else "Не указано"

            cls.vacancies_list.append(Vacancy(employee_sql_id=0, employee_id=cls.employee_id, hh_id=hh_id,
                                              name=name, requirement=requirement, responsibility=responsibility,
                                              link=link, salary_from=salary_from, salary_to=salary_to))

        return cls.vacancies_list

    @classmethod
    def validation_data(cls, valid_data):
        """ Метод для замены значения None на иное значение """
        return valid_data if valid_data is not None else "Не указано"
