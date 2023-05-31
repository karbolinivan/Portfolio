# Program:

API - <a href="https://api.chucknorris.io/" target="_blank">ChuckNorris</a>

1. Получаем список категорий.
2. Пользователь вводит категорию и получает шутку.

# Methods:

1. get_categories - возвращает все категории шуток.

   Результат:

   ```Python
   Запрос категорий шуток.
   Статус код: 200
   Список всех категорий:
   ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
   ```

2. get_user_category - получает категорию шутки от пользователя.

   Результат:

   ```Python
   Введите категорию:
   dev
   ```

3. get_jokes - возвращает шутку по выбранной категории.

   Результат:

   ```
   Запрос шутки.
   Статус код: 200
   Запрошенная категоря шутки: dev
   Полученная категория шутки: dev
   Шутка категории dev:
   Chuck Norris can solve the Towers of Hanoi in one move.
   ХА-ХА очень смешно Chuck
   ```

# Results:

Вызов методов:

```Python
winner = ChuckNorris()
winner.get_categories()
winner.get_jokes(winner.get_user_category())
```

Результат выполнения программы:

```
Запрос категорий шуток.
Статус код: 200
Список всех категорий:
['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
Введите категорию:
dev
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: dev
Полученная категория шутки: dev
Шутка категории dev:
Chuck Norris can solve the Towers of Hanoi in one move.
ХА-ХА очень смешно Chuck.
```
