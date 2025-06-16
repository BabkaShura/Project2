from src.models.vacancy import Vacancy
from src.utils.filters import filter_by_keywords
from src.utils.filters import filter_by_salary_range
from src.utils.filters import get_top_vacancies
from src.utils.filters import sort_vacancies

vacancies = [
    Vacancy("A", "url1", 50000, 60000, "Python Django"),
    Vacancy("B", "url2", 80000, 90000, "Flask FastAPI"),
    Vacancy("C", "url3", 30000, 40000, "No skills"),
]


def test_filter_by_keywords() -> None:
    result = filter_by_keywords(vacancies, ["python"])
    assert len(result) == 1
    assert result[0].title == "A"


def test_filter_by_salary_range() -> None:
    result = filter_by_salary_range(vacancies, 40000, 85000)
    assert len(result) == 2


def test_sort_vacancies() -> None:
    sorted_v = sort_vacancies(vacancies)
    assert sorted_v[0].salary_from == 80000


def test_get_top() -> None:
    top = get_top_vacancies(vacancies, 2)
    assert len(top) == 2
