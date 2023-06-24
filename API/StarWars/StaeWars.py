import requests


class StarWars:

    def __init__(self):
        self.base_url = "https://swapi.dev/api/"

    def get_all_characters(self):
        """
        :return: Список всех персонажей
        """
        list_characters = list()
        get_resource = f'people?page={1}'
        get_url = self.base_url + get_resource
        print(f'URL запроса имен пресонажей: {get_url}\n')
        result_get = requests.get(get_url)
        assert result_get.status_code == 200
        print(f'Успешный запрос.')
        data_results = result_get.json().get('results')
        data_next_pade = result_get.json().get('next')
        while data_next_pade is not None:
            for char in data_results:
                list_characters.append(char["name"])
            get_url = data_next_pade
            print(f'URL запроса имен пресонажей: {get_url}\n')
            result_get = requests.get(get_url)
            assert result_get.status_code == 200
            print(f'Успешный запрос.')
            data_results = result_get.json().get('results')
            data_next_pade = result_get.json().get('next')
        return list_characters

    def get_films_with_character(self, list_c, number):
        """
        :param list_c: Список всех персонажей
        :param number: Номер персонажа
        :return: Список фильмов с персонажем number
        """
        number -= 1
        get_resource = f"people/{number}"
        get_url = self.base_url + get_resource
        print(f'URL для запроса списка фильмов с {list_c[number]}: {get_url}')
        result_get = requests.get(get_url)
        print(f'Результат запроса: \n{result_get.text}')
        assert result_get.status_code == 200
        print(f'Успешный запрос.')
        list_of_films = result_get.json().get('films')
        print(f'Список фильмов с {list_c[number]}:',
              *list_of_films, sep="\n")
        return list_of_films


def get_link_characters_from_film(film):
    """
    :param film: Ссылка на фильм
    :return: Список персонажей в фильме
    """
    get_url = film
    print(f'URL запорса фильма: {get_url}')
    result_get = requests.get(get_url)
    title = result_get.json().get('title')
    print(f'Название фильма: {title}')
    print(f'Результат запроса: \n{result_get.text}')
    assert result_get.status_code == 200
    print(f'Успешный запрос.')
    list_characters = result_get.json().get('characters')
    print(f'Список персонажей в фильме:',
          *list_characters, sep="\n")
    return list_characters


def get_name_character(link_character):
    """
    :param link_character: Ссылка на персонажа
    :return: Имя персонажа
    """
    get_url = link_character
    print(f'URL персонажа: {get_url}')
    result_get = requests.get(get_url)
    print(f'Результат запроса: \n{result_get.text}')
    assert result_get.status_code == 200
    name_character = result_get.json().get('name')
    print(name_character)
    return name_character


def add_name_in_file(file, name):
    """
    :param file: Название файла для записи
    :param name: Имя персонаж
    """
    with open(file, 'r+') as character_file:
        ex = character_file.read()
        if name not in ex:
            character_file.write(f'{name}\n')
            print(f"Персонаж {name} записан в файл")


def main(films, file):
    """
    :param films: список фильмов
    :param file: Файл для записи
    """
    with open(file, "w"):
        print(f'Файл {file} очищен.')
    for char in films:
        link = get_link_characters_from_film(char)
        for item in link:
            name = get_name_character(item)
            add_name_in_file(file, name)


character = StarWars()
number_of_character = 4
file_name = "character_name.txt"
l_characters = character.get_all_characters()
l_film = character.get_films_with_character(l_characters, number_of_character)
main(l_film, file_name)
