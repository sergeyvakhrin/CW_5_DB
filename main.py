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

    # db_worker.create_table()

    #
    # # Получение списка Работодалетей
    # emp_api_request = HH('https://api.hh.ru/employers/', 'it')
    # employers: list = emp_api_request.get_api()
    #
    # # Сохранение в .json
    # emp_fileworker = FileWorker()
    # emp_fileworker.save_data(employers, EMPLOYEE_PATH, 'wt')
    #
    # # Получение списка экземпляров класса Работодателей
    # emp_worker = EmpWorker()
    # employer_list: list = emp_worker.get_employres(employers)
    #
    # Заполняем таблицу Работодателями
    # db_worker.insert_table_emp(employer_list)

    # Получаем 10 работодателей из базы данных по ТЗ курсовой
    ten_employee: list[tuple] = db_worker.get_top_ten_employee()
    print("Получили Топ 10 Работодателей")
    print(ten_employee)


    # Получение списка экземлпров класса Вакансий выбранных работодателей
    vac_fileworker = FileWorker()

    list_to_save_json_vacancy = []
    for employee in ten_employee:
        print("Циркулируемся по списку работодателей")
        vac_api_request = HH(employee[-1])
        print(f"заглянули в url {employee[-1]}")
        vacancies = vac_api_request.get_api()
        print("получили апи ответ")

        list_to_save_json_vacancy.extend(vacancies)
        print("пристегнули к списку")
        print(list_to_save_json_vacancy)
        print()

        # Получение списка экземпляров класса Вакансий
        emp_vacancies: list = VacWorker.get_vacancies(employee, vacancies)
        print("получили объекты вакинсий")
        print(emp_vacancies)
        print()

        db_worker.insert_table_vac(emp_vacancies)

        # employee.vacancies = emp_vacancies
        # print("воткнули вакансии в объект работодателей")
        # print(employee.vacancies)
        # print()

    # Сохранение в .json
    vac_fileworker.save_data(list_to_save_json_vacancy, VACANCIES_PATH, 'wt')





if __name__ == "__main__":
    main()
