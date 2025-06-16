import os
import tempfile

from src.models.vacancy import Vacancy
from src.storage.json_storage import JSONSaver


def test_add_and_get_vacancy() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        path = tf.name

    try:
        saver = JSONSaver(path)
        vacancy = Vacancy("Test", "http://t.com", 100000, 150000, "desc")
        saver.add_vacancy(vacancy)
        result = saver.get_all()
        assert len(result) == 1
        assert result[0].title == "Test"
    finally:
        os.remove(path)


def test_delete_vacancy() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        path = tf.name

    try:
        saver = JSONSaver(path)
        vacancy = Vacancy("DeleteMe", "http://del.com", 50000, 60000, "desc")
        saver.add_vacancy(vacancy)
        saver.delete_vacancy(vacancy)
        assert saver.get_all() == []
    finally:
        os.remove(path)
