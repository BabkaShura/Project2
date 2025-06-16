from src.api.hh_api import HH
from src.models.vacancy import Vacancy
from src.storage.json_storage import JSONSaver
from src.utils.filters import filter_by_keywords
from src.utils.filters import filter_by_salary_range
from src.utils.filters import get_top_vacancies
from src.utils.filters import sort_vacancies


def user_interaction() -> None:
    hh_api = HH()
    saver = JSONSaver()

    print("\n--- Поиск вакансий на hh.ru ---")
    keyword = input("Введите поисковый запрос (например: Python разработчик): ").strip()
    print("Загружаю вакансии с hh.ru...")

    raw_vacancies = hh_api.load_vacancies(keyword)
    if not raw_vacancies:
        print("Не удалось получить данные с hh.ru.")
        return

    # Преобразуем словари в объекты Vacancy и сохраняем
    for item in raw_vacancies:
        salary = item.get("salary") or {}
        salary_from = salary.get("from", 0)
        salary_to = salary.get("to", 0)

        vacancy = Vacancy(
            title=item["name"],
            url=item["alternate_url"],
            salary_from=salary_from,
            salary_to=salary_to,
            description=item.get("snippet", {}).get("requirement", ""),
        )
        saver.add_vacancy(vacancy)

    print(f"Получено и сохранено вакансий: {len(raw_vacancies)}")

    # Фильтрация по ключевым словам
    filter_keywords = (
        input("Введите ключевые слова для фильтрации (через пробел, Enter — пропустить): ").strip().split()
    )
    if filter_keywords:
        filtered_vacancies = filter_by_keywords(saver.get_all(), filter_keywords)
    else:
        filtered_vacancies = saver.get_all()

    # Фильтрация по диапазону зарплат
    try:
        min_salary = int(input("Введите минимальную зарплату (Enter — 0): ") or "0")
        max_salary = int(input("Введите максимальную зарплату (Enter — 1000000): ") or "1000000")
    except ValueError:
        print("Неверный формат зарплаты. Использую значения по умолчанию.")
        min_salary, max_salary = 0, 1000000

    salary_filtered = filter_by_salary_range(filtered_vacancies, min_salary, max_salary)

    # Сортировка
    sorted_vacancies = sort_vacancies(salary_filtered)
    try:
        top_n = int(input("Введите количество топ-вакансий по зарплате для отображения: "))
    except ValueError:
        print("Неверное значение, покажу 5 по умолчанию.")
        top_n = 5
    print(f"\nТоп {top_n} вакансий:\n")
    for i, vacancy in enumerate(get_top_vacancies(sorted_vacancies, top_n), start=1):
        print(f"{i}. {vacancy}")
    print("\n--- Конец списка ---")


if __name__ == "__main__":
    user_interaction()
