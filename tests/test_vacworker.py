from src.classes.vacworker import VacWorker


def test_get_vacancies(emp_tuple_none, data_none):
    vac = VacWorker()
    vac_list = vac.get_vacancies(emp_tuple_none, data_none)
    assert vac_list == []


def test_get_vacancies(emp_tuple_digit, data_digit):
    vac = VacWorker()
    vac_list = vac.get_vacancies(emp_tuple_digit, data_digit)
    assert vac_list == []


def test_get_vacancies(emp_tuple_tuple, data_tuple):
    vac = VacWorker()
    vac_list = vac.get_vacancies(emp_tuple_tuple, data_tuple)
    assert vac_list == []

def test_get_vacancies(emp_tuple, data_vac):
    vac = VacWorker()
    vac_list = vac.get_vacancies(emp_tuple, data_vac)
    assert vac_list[0].employee_sql_id == 1
    assert vac_list[0].employee_id == '1'
    assert vac_list[0].hh_id == '1'
    assert vac_list[0].name == '1'
    assert vac_list[0].requirement == '1'
    assert vac_list[0].responsibility == '1'
    assert vac_list[0].link == '1'
    assert vac_list[0].salary_from == 1
    assert vac_list[0].salary_to == 1
