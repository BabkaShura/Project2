from src.models.vacancy import Vacancy


def test_vacancy_creation_and_str() -> None:
    vacancy = Vacancy("Python Dev", "https://example.com", 100000, 150000, "Опыт Python")
    assert vacancy.title == "Python Dev"
    assert vacancy.salary_from == 100000
    assert str(vacancy).startswith("Python Dev")


def test_salary_validation() -> None:
    vacancy = Vacancy("NoSalary", "url", None, "notint", "desc")  # type: ignore
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_vacancy_comparison() -> None:
    v1 = Vacancy("v1", "url1", 50000, 60000, "desc")
    v2 = Vacancy("v2", "url2", 70000, 80000, "desc")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
