# Program:

API - <a href="https://api.chucknorris.io/" target="_blank">ChuckNorris</a>

1. Получаем список категорий.
2. Получаем шутку по каждой категории.

# Methods:

1. get_categories - возвращает все категории шуток.

   ```
   Запрос категорий шуток.
   Статус код: 200
   Список всех категорий:
   ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
   ```

2. get_jokes - Получает категорию и возвращает шутку.

   ```
   Запрос шутки.
   Статус код: 200
   Запрошенная категоря шутки: animal
   Полученная категория шутки: animal
   Шутка категории "animal": Chuck Norris can set ants on fire with a magnifying glass. At night.
   ```

3. Получение шуток каждой категории:
   ```Puthon
   winner = ChuckNorris()
   for char in winner.get_categories():
       winner.get_jokes(char)
   ```

# Results:

Результат выполнения программы:

```
Запрос категорий шуток.
Статус код: 200
Список всех категорий:
['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: animal
Полученная категория шутки: animal
Шутка категории "animal": They say curiosity killed the cat. This is false. Chuck Norris killed the cat. Every single one of them.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: career
Полученная категория шутки: career
Шутка категории "career": In the beginning there was nothing...then Chuck Norris Roundhouse kicked that nothing in the face and said "Get a job". That is the story of the universe.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: celebrity
Полученная категория шутки: celebrity
Шутка категории "celebrity": Everything King Midas touches turnes to gold. Everything Chuck Norris touches turns up dead.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: dev
Полученная категория шутки: dev
Шутка категории "dev": Chuck Norris finished World of Warcraft.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: explicit
Полученная категория шутки: explicit
Шутка категории "explicit": Hitler got raped because Chuck Norris raped him.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: fashion
Полученная категория шутки: fashion
Шутка категории "fashion": Chuck Norris does not follow fashion trends, they follow him. But then he turns around and kicks their ass. Nobody follows Chuck Norris.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: food
Полученная категория шутки: food
Шутка категории "food": When Chuck Norris wants an egg, he cracks open a chicken.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: history
Полученная категория шутки: history
Шутка категории "history": In the Words of Julius Caesar, "Veni, Vidi, Vici, Chuck Norris". Translation: I came, I saw, and I was roundhouse-kicked inthe face by Chuck Norris.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: money
Полученная категория шутки: money
Шутка категории "money": If Chuck Norris steals money from a bank, the owner of the bank gets arrested for not just giving Chuck Norris the money.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: movie
Полученная категория шутки: movie
Шутка категории "movie": For Bruce Willis' birthday, he received a DVD of Chuck Norris banging Demi Moore while repeatedly yelling 'Yippee Ki Yay, Motherfucker'. Norris then felt a rare twinge of guilt, so he then sent Willis a DVD of him pummeling Ashton Kutcher with Charlie Sheen.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: music
Полученная категория шутки: music
Шутка категории "music": The Drummer for Def Leppard's only got one arm. Chuck Norris needed a back scratcher.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: political
Полученная категория шутки: political
Шутка категории "political": Chuck Norris is responsible for China's over-population. He hosted a Karate tournament in Beijing and all women within 1,000 miles became pregnant instantly.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: religion
Полученная категория шутки: religion
Шутка категории "religion": In the Bible, Jesus turned water into wine. But then Chuck Norris turned that wine into beer.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: science
Полученная категория шутки: science
Шутка категории "science": Chuck Norris knows the last digit of pi.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: sport
Полученная категория шутки: sport
Шутка категории "sport": Chuck Norris used to play baseball. When Babe Ruth was hailed as the better player, Chuck Norris killed him with a baseball bat to the throat. Lou Gehrig got off easy.
===============================================================================================
Запрос шутки.
Статус код: 200
Запрошенная категоря шутки: travel
Полученная категория шутки: travel
Шутка категории "travel": Chuck Norris did in fact, build Rome in a day.
===============================================================================================
```
