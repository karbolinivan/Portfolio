import requests


class ChuckNorris:
    def __init__(self):
        self.url_categories = 'https://api.chucknorris.io/jokes/categories'
        self.url_joke = f'https://api.chucknorris.io/jokes/random?category='

    def get_categories(self):
        print(self.url_categories)
        result_categories = requests.get(self.url_categories)
        assert 200 == result_categories.status_code
        print(f'Запрос категорий шуток.\n'
              f'Статус код: {result_categories.status_code}')
        categories = result_categories.json()
        print(f'Список всех категорий:\n{categories}')
        return categories

    def get_jokes(self, category):
        url_joke = self.url_joke + category
        result_joke = requests.get(url_joke)
        assert 200 == result_joke.status_code
        print(f'Запрос шутки.\n'
              f'Статус код: {result_joke.status_code}')
        assert category == result_joke.json().get('categories')[0]
        print(f'Запрошенная категоря шутки: {category}\n'
              f'Полученная категория шутки: {result_joke.json().get("categories")[0]}')
        joke = result_joke.json().get('value')
        return print(f'Шутка категории "{category}": {joke}')


winner = ChuckNorris()
for char in winner.get_categories():
    winner.get_jokes(char)
