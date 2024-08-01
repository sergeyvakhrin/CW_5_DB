from src.classes.employee import Employee


def test_employee(employer):
    emp = Employee(**employer)
    assert emp.hh_id == '1'
    assert emp.name == '1'
    assert emp.url == '1'
    assert emp.alternate_url == '1'
    assert emp.vacancies_url == '1'
    assert emp.open_vacancies == 1
    assert emp.vacancies == [1]
