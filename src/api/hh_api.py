import typing

import requests

from src.api.abstract_api import Parser


class HH(Parser):
    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def __make_request(self, params: dict) -> typing.Mapping[str, typing.Any]:
        response = requests.get(self.__url, headers=self.__headers, params=params)
        if response.status_code != 200:
            raise ConnectionError(f"Ошибка при подключении: {response.status_code}")
        return typing.cast(typing.Mapping[str, typing.Any], response.json())

    def load_vacancies(self, keyword: str) -> list[dict]:
        vacancies: list[dict] = []
        for page in range(5):  # чтобы не перегружать API
            params = {"text": keyword, "page": page, "per_page": 50}
            data = self.__make_request(params)
            items = data.get("items", [])
            if isinstance(items, list):
                vacancies.extend(items)
        return vacancies
