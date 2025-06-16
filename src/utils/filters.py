from typing import List

from src.models.vacancy import Vacancy


def filter_by_keywords(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по наличию любого из ключевых слов в описании.
    """
    return [vacancy for vacancy in vacancies if any(word.lower() in vacancy.description.lower() for word in keywords)]


def filter_by_salary_range(
    vacancies: List[Vacancy], min_salary: int = 0, max_salary: int = 1_000_000
) -> List[Vacancy]:
    """
    Фильтрует вакансии по заданному диапазону зарплат.
    """
    return [vacancy for vacancy in vacancies if min_salary <= vacancy.salary_from <= max_salary]


def sort_vacancies(vacancies: List[Vacancy], by: str = "salary_from", reverse: bool = True) -> List[Vacancy]:
    """
    Сортирует вакансии по указанному полю (по умолчанию: от большей зарплаты к меньшей).
    """
    return sorted(vacancies, key=lambda v: getattr(v, by), reverse=reverse)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """
    Возвращает топ-N вакансий.
    """
    return vacancies[:top_n]
