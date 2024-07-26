from config import EMPLOYEE_PATH
from src.classes.api_request import HH
from src.classes.empworker import EmpWorker
from src.classes.fileworker import FileWorker
from src.classes.vacworker import VacWorker


def main():

    # Запрос Работодателей
    api_request = HH()

    # Получение списка Работодалетей
    employers: list = api_request.get_api('https://api.hh.ru/employers/', 'python')

    # Сохранение в .json
    fileworker = FileWorker(employers, EMPLOYEE_PATH)
    fileworker.save_data()

    # Получение списка экземпляров класса Работодателей
    emp_worker = EmpWorker()
    employer_list: list = emp_worker.get_employres(employers)

    # Получение списка экземлпров класса Вакансий всех работодателей с id работодателя
    vac_worker = VacWorker()
    vacancies_list: list = []
    for employee in employer_list:
        vacancies: list = api_request.get_api(employee.vacancies_url)
        emp_vacancies: list = vac_worker.get_vacancies(employee, vacancies)
        vacancies_list.extend(emp_vacancies)






if __name__ == "__main__":
    main()
