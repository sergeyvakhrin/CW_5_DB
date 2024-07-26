from src.classes.employee import Employee


class EmpWorker:
    """ Класс для работы с объектами класс Employee """
    def get_employres(self, employers) -> list:
        """ Получение спаска экземпляров Класса Работодателей """
        employers_list: list = []
        for employee in employers:
            if isinstance(employee, dict):
                employers_list.append(Employee(employee_id=employee.get('id', "Не задано"),
                                               name=employee.get('name', "Не задано"),
                                               url=employee.get('url', "Не задано"),
                                               alternate_url=employee.get('alternate_url', "Не задано"),
                                               vacancies_url=employee.get('vacancies_url', "Не задано"),
                                               open_vacancies=employee.get('open_vacancies', "Не задано")))
            else:
                continue
        return employers_list

