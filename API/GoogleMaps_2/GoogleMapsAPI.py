import requests


class Location:
    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"
        self.key = "?key=qaclick123"

    def create_new_location(self):
        """Создает новую локацию и возвращает place_id"""
        post_resource = "/maps/api/place/add/json"
        post_url = self.base_url + post_resource + self.key
        print(f'URL создания новой локации: {post_url}')
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
        print(f'Создание новой локации.\n'
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
        """Запрос информации о локации по place_id и возвращает status_code ответа."""
        get_resource = "/maps/api/place/get/json"
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        result_get = requests.get(get_url)
        print(f'URL новой локации: {get_url}\n'
              f'Запрос информации. ID: {place_id}\n'
              f'Ответ сервера: {result_get.text}')
        if 200 == result_get.status_code:  # Ничего умнее не придумал =(
            print(f'Успешный запрос информации.\n'
                  f'Статус код: {result_get.status_code}')
            return result_get.status_code
        elif 404 == result_get.status_code:
            print(f'Локации с таким ID не существует.\n'
                  f'Статус код: {result_get.status_code}')
            return result_get.status_code

    def delete_location(self, place_id):
        """Удаление локации по place_id"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = self.base_url + delete_resource + self.key
        print(f'URL удаления локации: {delete_url}')
        json_for_delete_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        print(f'Удаление локации: ID {place_id}\n'
              f"Ответ сервера: {result_delete.json().get('status')}")
        assert 200 == result_delete.status_code
        print(f'Успешное удаление локации.\n'
              f'Статус код: {result_delete.status_code}')


def save_place_id(file, place_id):
    """Записывает place_id локации в file"""
    with open(file, 'a') as file_new_locations:
        file_new_locations.write(f'{place_id}\n')
    print(f'Локация добавлена в файл. ID: {place_id}')


def save_n_place_id(file, amount):
    """Создает n локаций и сохраняет place_id в file"""
    print(('\n' + '=' * 100) * 3)
    with open(file, 'w'):
        print(f'Файл {file} очищен')
    for i in range(amount):
        save_place_id(file, new_location.create_new_location())
        print('-' * 100)
    print(f'Сохранено {amount} ID.')


def get_info_locations_from_file(file):
    """Выводит информацию о локациях из file"""
    print(('\n' + '=' * 100) * 3)
    with open(file, 'r') as location_from_file:
        for _ in open(file, 'r'):
            id_from_file = location_from_file.readline().strip()
            print(f'ID из файла {file}: {id_from_file}')
            new_location.get_info_location(id_from_file)
            print('-' * 100)


def delete_location_from_file(file, a, b):
    """Удаляет локацию a и b из file, где a и b целые положительные числа в диапазоне amount_locations"""
    print(('\n' + '=' * 100) * 3)
    with open(file, 'r') as location_from_file:
        line_count = 0
        for _ in open(file, 'r'):
            id_from_file = location_from_file.readline().strip()
            if line_count == a - 1 or line_count == b - 1:
                print(f'Удаление локации номер {line_count + 1}: ID {id_from_file}')
                new_location.delete_location(id_from_file)
                print('-' * 100)
            line_count += 1


def check_locations_from_file(file, new_file):
    """Проверяет локацию из file. Если локация существует сохраняет её в new_file"""
    print(('\n' + '=' * 100) * 3)
    with open(new_file, 'w'):
        print(f'Файл {new_file} очищен.')
    with open(file, 'r') as location_from_file:
        for _ in open(file, 'r'):
            id_from_file = location_from_file.readline().strip()
            print(f'ID из файла {file}: {id_from_file}')
            if new_location.get_info_location(id_from_file) == 404:
                print('-' * 100)
                continue
            save_place_id(new_file, id_from_file)
            print('-' * 100)


new_location = Location()

amount_locations = 5
delete_location_a = 2
delete_location_b = 4
file_name = 'new_locations.txt'
checked_file_name = 'checked_locations.txt'

save_n_place_id(file_name, amount_locations)
get_info_locations_from_file(file_name)
delete_location_from_file(file_name, delete_location_a, delete_location_b)
check_locations_from_file(file_name, checked_file_name)
