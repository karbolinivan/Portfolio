import requests


class Location:
    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"  # Базовая URL
        self.key = "?key=qaclick123"  # Параметр для всех запросов

    def create_new_location(self):
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post
        print("=======================================================")
        """Создает новую локацию и возвращает place_id"""
        post_url = self.base_url + post_resource + self.key
        print(f'URL создания новой локации:\n{post_url}')

        json_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_new_location)
        print(f'Создание новой локации\n'
              f'Ответ сервера:\n{result_post.text}')

        assert 200 == result_post.status_code
        print(f'Успешное создание локации.\n'
              f'Статус код: {result_post.status_code}')

        value_status_post = result_post.json().get('status')
        assert value_status_post == "OK"
        print(f'Статус создания новой локации: {value_status_post}')

        place_id_new_location = result_post.json().get('place_id')
        print(f'ID новой локации: {place_id_new_location}')

        return place_id_new_location

    def get_info_location(self, place_id):
        get_resource = "/maps/api/place/get/json"

        """Получает информацию о локации"""
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        result_get = requests.get(get_url)
        print(f'URL новой локации: {get_url}\n'
              f'Запрос информации. ID: {place_id}\n'
              f'Ответ сервера: {result_get.text}')

        assert 200 == result_get.status_code
        print(f'Успешный запрос информации.\n'
              f'Статус код: {result_get.status_code}')
        print("=======================================================")


def save_place_id(place_id):
    """Записывает place_id локации в файл new_locations"""
    with open('new_locations.txt', 'a') as file_new_locations:
        file_new_locations.write(f'{place_id}\n')
    print(f'Локация добавлена в файл. ID: {place_id}')


def save_n_place_id(amount):
    """Создает n локаций и сохраняет place_id в файл new_locations"""
    with open('new_locations.txt', 'w'):
        print('Файл с локациями очищен')
    for i in range(amount):
        save_place_id(new_location.create_new_location())
    print(f'Сохранено {amount} ID.')


def get_info_locations_from_file():
    """Выводит информацию о локациях из файла new_locations"""
    with open('new_locations.txt', 'r') as location_from_file:
        for _ in open('new_locations.txt', 'r'):
            id_from_file = location_from_file.readline().strip()
            print(f'ID из файла: {id_from_file}')
            new_location.get_info_location(id_from_file)


new_location = Location()
amount_locations = 5
save_n_place_id(amount_locations)
get_info_locations_from_file()
