import json

"""Методы для проверки ответов наших запросов"""


class Checking:

    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert result.status_code == status_code
        print(f'Статус код = {result.status_code}')

    """Метод для проверки наличия обязательных полей"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)  # Преобразует строку в формат json
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} верный')

    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'Слово {field_name} присутствует')
