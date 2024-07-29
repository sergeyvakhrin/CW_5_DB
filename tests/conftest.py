import pytest

from src.classes.dbworker import Employee
from src.classes.vacancy import Vacancy


@pytest.fixture
def employer_list():
    return [
        Employee(employee_id="1", name="1", url="1", alternate_url="1", vacancies_url="1", open_vacancies=1),
        Employee(employee_id="2", name="2", url="2", alternate_url="2", vacancies_url="2", open_vacancies=2),
        Employee(employee_id="3", name="3", url="3", alternate_url="3", vacancies_url="3", open_vacancies=3)
    ]


@pytest.fixture
def vacancies_list():
    return [
        Vacancy(employee_id="1", vacancy_id="1", name="1", requirement="1", responsibility="1", link="1", salary_from=1,
                salary_to=1),
        Vacancy(employee_id="2", vacancy_id="2", name="2", requirement="2", responsibility="2", link="2", salary_from=2,
                salary_to=2),
        Vacancy(employee_id="3", vacancy_id="3", name="3", requirement="3", responsibility="3", link="3", salary_from=3,
                salary_to=3)
    ]
