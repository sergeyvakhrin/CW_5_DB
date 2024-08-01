import pytest

from src.classes.vacancy import Vacancy


@pytest.fixture
def employer():
    return {"hh_id": "1", "name": "1", "url": "1", "alternate_url": "1", "vacancies_url": "1", "open_vacancies": 1,
            "vacancies": [1]}


@pytest.fixture
def vacancy():
    return {'employee_sql_id': 1, 'employee_id': "1", 'hh_id': "1", 'name': "1", 'requirement': "1",
            'responsibility': "1", 'link': "1", 'salary_from': 1, 'salary_to': 1}


@pytest.fixture
def data_none():
    return


@pytest.fixture
def data_digit():
    return 1


@pytest.fixture
def data_tuple():
    return ()


@pytest.fixture
def emp_tuple_none():
    return


@pytest.fixture
def emp_tuple_digit():
    return 1


@pytest.fixture
def emp_tuple_tuple():
    return ()


@pytest.fixture
def emp_tuple():
    return 1, '1', '1'


@pytest.fixture
def data_vac():
    return [{"employee_sql_id": 1, "employee_id": '1', "id": '1', "name": '1', "requirement": '1',
            "responsibility": '1', "link": '1', "salary_from": 1, "salary_to": 1}]
