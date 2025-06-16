class Vacancy:
    __slots__ = ("title", "url", "salary_from", "salary_to", "description")

    def __init__(self, title: str, url: str, salary_from: int, salary_to: int, description: str):
        self.title = title
        self.url = url
        self.salary_from = self.__validate_salary(salary_from)
        self.salary_to = self.__validate_salary(salary_to)
        self.description = description

    def __validate_salary(self, value: int) -> int:
        return value if isinstance(value, int) and value > 0 else 0

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary_from < other.salary_from

    def __le__(self, other: "Vacancy") -> bool:
        return self.salary_from <= other.salary_from

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from == other.salary_from

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Vacancy":
        return cls(**data)

    def __str__(self) -> str:
        salary = (
            f"{self.salary_from}-{self.salary_to} руб."
            if self.salary_from and self.salary_to
            else "Зарплата не указана"
        )
        return f"{self.title} | {salary} | {self.url}"
