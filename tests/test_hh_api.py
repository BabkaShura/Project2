from unittest.mock import MagicMock
from unittest.mock import patch

from src.api.hh_api import HH


@patch("requests.get")
def test_load_vacancies(mock_get: MagicMock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [{"name": "Mock", "alternate_url": "url", "snippet": {"requirement": "req"}}]
    }

    hh = HH()
    result = hh.load_vacancies("Python")
    assert isinstance(result, list)
    assert result[0]["name"] == "Mock"
