from abc import ABC
from abc import abstractmethod


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        pass
