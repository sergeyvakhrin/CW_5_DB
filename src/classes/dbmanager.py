import psycopg2


class DBManager:
    """ Класс для получения данных из базы данных - SQL запросы """

    def __init__(self, host, dbname, user, password, port):
        """ Конструктор класса """
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """ Получает список всех компаний и количество вакансий у каждой компании """
        cur = self.conn.cursor()
        cur.execute("SELECT name, open_vacancies FROM employee")
        res = cur.fetchall()
        cur.close()
        return res

    def get_all_vacancies(self):
        """ Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты
            и ссылки на вакансию """
        cur = self.conn.cursor()
        cur.execute("SELECT vacancy.name AS vacancy, employee.name AS employer, salary_from, vacancy.url  FROM "
                    "vacancy LEFT JOIN employee USING(employer_id)")
        res = cur.fetchall()
        cur.close()
        return res

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям """
        cur = self.conn.cursor()
        cur.execute("SELECT AVG(salary_from) FROM vacancy")
        res = cur.fetchall()
        cur.close()
        return res

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям """
        cur = self.conn.cursor()
        cur.execute("SELECT name, salary_from FROM vacancy WHERE salary_from > (SELECT AVG(salary_from) FROM vacancy)")
        res = cur.fetchall()
        cur.close()
        return res

    def get_vacancies_with_keyword(self, keyword=''):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        cur = self.conn.cursor()
        cur.execute(f"SELECT name FROM vacancy WHERE name LIKE '%{keyword}%'")
        res = cur.fetchall()
        cur.close()
        return res

