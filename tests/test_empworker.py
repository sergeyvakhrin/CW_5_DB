from src.classes.empworker import EmpWorker


def test_get_employres(data_none):
    emp = EmpWorker()
    emp_list = emp.get_employres(data_none)
    assert emp_list[0].hh_id == "Не задано"
    assert emp_list[0].name == "Не задано"
    assert emp_list[0].url == "Не задано"
    assert emp_list[0].alternate_url == "Не задано"
    assert emp_list[0].vacancies_url == "Не задано"
    assert emp_list[0].open_vacancies == "Не задано"
    assert emp_list[0].vacancies == []


def test_EmpWorker():
    emp = EmpWorker()
    assert isinstance(emp.employers_list, list)
