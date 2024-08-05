from src.classes.vacancy import Vacancy


class VacWorker:
    """ Класс для работы с объектами класса Vacancy """

    @classmethod
    def get_vacancies(cls, employee: tuple, vacancies: list) -> list:
        """ Получение спаска экземпляров Класса Вакансий """

        if isinstance(employee, tuple) and len(employee) == 3:
            cls.employee_sql_id = employee[0]
            cls.employee_id = employee[1]
        else:
            return []

        cls.vacancies_list: list = []

        if isinstance(vacancies, list) and len(vacancies) > 0:
            for vacancy in vacancies:
                if isinstance(vacancy, dict) and len(vacancy) > 0:
                    hh_id = cls.validation_data(vacancy.get("id", "Не указано"))
                    name = cls.validation_data(vacancy.get("name", "Не указано"))
                    requirement = cls.validation_data(vacancy.get("snippet").get("requirement", "Не указано")) \
                        if isinstance(vacancy.get("snippet"), (dict, str, list, int, float)) else "Не указано"
                    responsibility = cls.validation_data(vacancy.get("snippet").get("responsibility", "Не указано")) \
                        if isinstance(vacancy.get("snippet"), (dict, str, list, int, float)) else "Не указано"
                    link = cls.validation_data(vacancy.get("alternate_url", "Не указано"))
                    salary_from = cls.validation_data(vacancy.get("salary").get("from", 0)) \
                        if isinstance(vacancy.get("salary"), (dict, str, list, int, float)) else 0
                    salary_to = cls.validation_data(vacancy.get("salary").get("to", 0)) \
                        if isinstance(vacancy.get("salary"), (dict, str, list, int, float)) else 0

                    cls.vacancies_list.append(
                        Vacancy(employee_sql_id=cls.employee_sql_id, employee_id=cls.employee_id, hh_id=hh_id,
                                name=name, requirement=requirement, responsibility=responsibility,
                                link=link, salary_from=salary_from, salary_to=salary_to))
                else:
                    continue
        else:
            return []
        return cls.vacancies_list

    @classmethod
    def validation_data(cls, valid_data):
        """ Метод для замены значения None на иное значение """
        return valid_data if valid_data is not None else 0


# vac = VacWorker()
# list_vac = vac.get_vacancies(
#                     (1, '1', '1'),
#                     [{"employee_sql_id": 1, "employee_id": '1', "id": '1', "name": '1', "snippet": {"requirement": '1',
#                                "responsibility": '1'}, "alternate_url": '1', "salary": {"from": 1, "to": 1}}])
# list_vac2 = vac.get_vacancies(
#                     (1, 1, 1),
#                     [])
#
# print(list_vac2)
# print(len(list_vac2))
# print(type(list_vac2))

