from abc import ABC
from abc import abstractmethod
from typing import List

from src.models.vacancy import Vacancy


class AbstractStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в хранилище"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str = "") -> List[Vacancy]:
        """Получает вакансии по ключевому слову"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из хранилища"""
        pass
