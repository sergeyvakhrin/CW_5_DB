import json

from config import EMPLOYEE_PATH, VACANCIES_PATH
from src.classes.api_request import HH
from src.classes.empworker import EmpWorker
from src.classes.fileworker import FileWorker
from src.classes.vacworker import VacWorker


def main():

    # Запрос Работодателей
    emp_api_request = HH()

    # Получение списка Работодалетей
    employers: list = emp_api_request.get_api('https://api.hh.ru/employers/', 'водитель')

    # Сохранение в .json
    emp_fileworker = FileWorker()
    emp_fileworker.save_data(employers, EMPLOYEE_PATH, 'wt')

    # Получение списка экземпляров класса Работодателей
    emp_worker = EmpWorker()
    employer_list: list = emp_worker.get_employres(employers)

    # Получение списка экземлпров класса Вакансий всех работодателей с id работодателя
    vac_api_request = HH()
    vac_fileworker = FileWorker()
    vac_worker = VacWorker()

    vacancies_list: list = []
    for employee in employer_list:
        vacancies: list = vac_api_request.get_api(employee.vacancies_url)

        vac_fileworker.save_data(vacancies, VACANCIES_PATH, 'wt')

        emp_vacancies: list = vac_worker.get_vacancies(employee, vacancies)
        vacancies_list.extend(emp_vacancies)








if __name__ == "__main__":
    main()
