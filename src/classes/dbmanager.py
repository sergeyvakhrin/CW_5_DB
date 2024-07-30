import psycopg2


class DBManager:
    """ Класс для получения данных из базы данных - SQL запросы """

    def __init__(self, host, dbname, user, password, port):
        """ Конструктор класса """
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)

    def get_companies_and_vacancies_count(self):
        """ Получает список всех компаний и количество вакансий у каждой компании """
        cur = self.conn.cursor()
        cur.execute("""
                           
                                   """)
        res = cur.fetchall()
        self.conn.commit()
        return res

    def get_all_vacancies(self):
        """ Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты
            и ссылки на вакансию """
        pass

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям """
        pass

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям """
        pass

    def get_vacancies_with_keyword(self):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        pass