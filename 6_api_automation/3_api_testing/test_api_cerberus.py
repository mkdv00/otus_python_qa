import cerberus
import requests


def test_api_json_schema(base_url):
    """ Проверка структуры ответа из запроса /todos/1 """
    res = requests.get(base_url + "/todos/1")
    
    schema = {
        "id": {"type": "number"},
        "userId": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    }

    validator = cerberus.Validator()
    assert validator.validate(res.json(), schema)
