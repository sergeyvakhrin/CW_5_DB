import psycopg2


class DataBaseWorker:
    """ Класс для заполнения базы данных """
    def __init__(self, host, dbname, user, password, port):
        """ Конструктор класса """
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)

    def db_exists(self) -> bool:
        """ Проверяет наличие базы данных """
        pass

    def create_db(self) -> None:
        """ Создает Базу данных """
        pass

    def create_table(self) -> None:
        """ Создает Таблицу Работодателей """
        cur = self.conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Employee(
                        employer_id SERIAL PRIMARY KEY,
                        hh_id VARCHAR(20),
                        name VARCHAR(255),
                        url VARCHAR(255),
                        alternate_url VARCHAR(255),
                        vacancies_url VARCHAR(255),
                        open_vacancies INT                        
                    );
                            """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Vacancy(
                        vacancy_id SERIAL PRIMARY KEY,
                        employer_id INT REFERENCES Employee(employer_id),
                        hh_id VARCHAR(20),
                        name VARCHAR(255),
                        requirement text,
                        responsibility text,
                        url VARCHAR(255),
                        salary_from INT,
                        salary_to INT
                    );
                        """)
        self.conn.commit()

    def check_in_base(self, data):
        """ Проверяет наличие в базе """
        cur = self.conn.cursor()
        cur.execute(f"""
                SELECT hh_id FROM {data.__class__.__name__}
                WHERE hh_id = '{data.hh_id}'
                LIMIT 1
        """)
        try: res_id = cur.fetchone()[0]
        except: return False
        cur.close()
        return True if res_id else False

    def get_sql_id_employer(self, employee):
        """ Получает sql_id работодателя, если он уже есть в базе """
        cur = self.conn.cursor()
        cur.execute(f"""
                        SELECT employer_id FROM Employee
                        WHERE hh_id = '{employee.hh_id}'
                        LIMIT 1
                """)
        res_id = cur.fetchone()[0]
        cur.close()
        return res_id

    def add_sql_id_in_vacancy(self, employee, employee_sql_id) -> None:
        """ Заполняет поле vacancy.employee_sql_id """
        # next_sql_id: int = self.get_next_id_employee()
        for vacancy in employee.vacancies:
            vacancy.employee_sql_id = employee_sql_id

    def insert_table_emp(self, employer_list) -> None:
        """ Заполняет Таблицу работодателей """
        cur = self.conn.cursor()
        for employee in employer_list:
            # проверяем работодателя на присутствие в базе
            if self.check_in_base(employee):
                # если работодатель уже есть в базе, получаем его sql_id
                employee_sql_id = self.get_sql_id_employer(employee)
                # вакансиям этого работодателя присваиваем его sql_id
                self.add_sql_id_in_vacancy(employee, employee_sql_id)
                cur.execute(f"UPDATE employee SET name='{employee.name}', url='{employee.url}', alternate_url='{employee.alternate_url}', vacancies_url='{employee.vacancies_url}', open_vacancies='{employee.open_vacancies}' WHERE hh_id='{employee.hh_id}'")
                # берем следующего работодателя
                continue # TODO: можно реализовать метод обновления данных о работодателе с подстановкой даты обновления
            else:
                # если работодатель отсутствует, добавляем его в базу
                cur.executemany("INSERT INTO Employee (hh_id, name, url, alternate_url, vacancies_url, open_vacancies) VALUES (%s, %s, %s, %s, %s, %s)",
                            [(employee.hh_id, employee.name, employee.url, employee.alternate_url,
                             employee.vacancies_url, employee.open_vacancies)])
                # получаем присвоенный ему sql_id
                employee_sql_id = self.get_sql_id_employer(employee)
                # вакансиям этого работодателя присваиваем его sql_id
                self.add_sql_id_in_vacancy(employee, employee_sql_id)
        self.conn.commit()

    def insert_table_vac(self, emp_vacancies: list) -> None:
        """ Заполняет таблицу вакансий """
        cur = self.conn.cursor()
        for vacancy in emp_vacancies:
            if self.check_in_base(vacancy):
                cur.execute(f"UPDATE vacancy SET name='{vacancy.name}', requirement='{vacancy.requirement}', responsibility='{vacancy.responsibility}', url='{vacancy.link}', salary_from='{vacancy.salary_from}', salary_to='{vacancy.salary_to}' WHERE hh_id='{vacancy.hh_id}'")
                continue # TODO: можно реализовать метод обновления данных о вакансии с подстановкой даты обновления
            else:
                cur.executemany(
                    "INSERT INTO vacancy (employer_id, hh_id, name, requirement, responsibility, url, salary_from, salary_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    [(vacancy.employee_sql_id, vacancy.hh_id, vacancy.name, vacancy.requirement, vacancy.responsibility,
                      vacancy.link, vacancy.salary_from, vacancy.salary_to)])
        self.conn.commit()

    def get_top_ten_employee(self):
        """ Получаем 10 работодателей """
        cur = self.conn.cursor()
        cur.execute("""
                        SELECT employer_id, hh_id, vacancies_url FROM employee
                        ORDER BY open_vacancies DESC
                        LIMIT 10""")
        res_id = cur.fetchall()
        cur.close()
        return res_id
