import json
import os
from typing import List

from src.models.vacancy import Vacancy
from src.storage.abstract_storage import AbstractStorage


class JSONSaver(AbstractStorage):
    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_all()
        if not any(v.url == vacancy.url for v in vacancies):
            vacancies.append(vacancy)
            self.__save_all(vacancies)

    def get_all(self) -> List[Vacancy]:
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Ожидался список словарей.")
            return [Vacancy.from_dict(item) for item in data if isinstance(item, dict)]
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            return []

    def get_vacancies(self, keyword: str = "") -> List[Vacancy]:
        return [v for v in self.get_all() if keyword.lower() in v.description.lower()]

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = [v for v in self.get_all() if v.url != vacancy.url]
        self.__save_all(vacancies)

    def __save_all(self, vacancies: List[Vacancy]) -> None:
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in vacancies], f, ensure_ascii=False, indent=4)
