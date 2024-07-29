from config import EMPLOYEE_PATH, VACANCIES_PATH
from src.classes.api_request import HH
from src.classes.dbworker import DataBaseWorker
from src.classes.empworker import EmpWorker
from src.classes.fileworker import FileWorker
from src.classes.vacworker import VacWorker
from src.utils.config import config


def main():

    # Создание Таблиц в базе данных
    param = config()
    db_worker = DataBaseWorker(**param)

    db_worker.create_table()


    # Получение списка Работодалетей
    emp_api_request = HH('https://api.hh.ru/employers/', 'java')
    employers: list = emp_api_request.get_api()
    # Сохранение в .json
    emp_fileworker = FileWorker()
    emp_fileworker.save_data(employers, EMPLOYEE_PATH, 'wt')

    # Получение списка экземпляров класса Работодателей
    emp_worker = EmpWorker()
    employer_list: list = emp_worker.get_employres(employers)


    # Получение списка экземлпров класса Вакансий всех работодателей

    vac_fileworker = FileWorker()
    # vac_worker = VacWorker()

    list_to_save_json_vacancy = []
    for employee in employer_list:

        vac_api_request = HH(employee.vacancies_url)
        vacancies = vac_api_request.get_api()

        list_to_save_json_vacancy.extend(vacancies)

        # Получение списка экземпляров класса Вакансий
        emp_vacancies: list = VacWorker.get_vacancies(employee, vacancies)
        employee.vacancies = emp_vacancies

    # Сохранение в .json
    vac_fileworker.save_data(list_to_save_json_vacancy, VACANCIES_PATH, 'wt')

    db_worker.insert_table_emp(employer_list)
    db_worker.insert_table_vac(employer_list)

















if __name__ == "__main__":
    main()
