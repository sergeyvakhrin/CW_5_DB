from src.classes.vacancy import Vacancy


def test_employee(vacancy):
    vac = Vacancy(**vacancy)
    assert vac.employee_sql_id == 1
    assert vac.employee_id == '1'
    assert vac.hh_id == '1'
    assert vac.name == '1'
    assert vac.requirement == '1'
    assert vac.responsibility == '1'
    assert vac.link == '1'
    assert vac.salary_from == 1
    assert vac.salary_to == 1