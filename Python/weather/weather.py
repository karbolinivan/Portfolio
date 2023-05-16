import requests
import json

while True:
    try:
        print("Введите название города: ")
        city = str(input())
        url = (
                'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

        weather_data = requests.get(url).json()
        weather_data_json = json.dumps(weather_data, indent=2)

        temperature = round(weather_data['main']['temp'])
        feels = round(weather_data['main']['feels_like'])
        wind_speed = round(weather_data['wind']['speed'])

        if abs(temperature) == 1 or abs(temperature) == 21 or abs(temperature) == 31 or abs(temperature) == 41 or abs(
                temperature) == 51 or abs(temperature) == 61 or abs(temperature) == 71:
            print('Сейчас в городе', city, str(temperature), 'градус')
        elif abs(temperature) in range(2, 5) or abs(temperature) in range(22, 25) or abs(temperature) in range(32,
                                                                                                               35) or abs(
                temperature) in range(42, 45) or abs(temperature) in range(52, 55) or abs(temperature) in range(62,
                                                                                                                65) or abs(
                temperature) in range(72, 75):
            print('Сейчас в городе', city, str(temperature), 'градуса')
        else:
            print('Сейчас в городе', city, str(temperature), 'градусов')

        print('Скорость ветра', str(wind_speed), 'м/с')

        if abs(feels) == 1 or abs(feels) == 21 or abs(feels) == 31 or abs(feels) == 41 or abs(feels) == 51 or abs(
                feels) == 61 or abs(feels) == 71:
            print('Ощущается как', str(feels), 'градус')
        elif abs(temperature) in range(2, 5) or abs(feels) in range(22, 25) or abs(feels) in range(32, 35) or abs(
                feels) in range(42, 45) or abs(feels) in range(52, 55) or abs(feels) in range(62, 65) or abs(
                feels) in range(72, 75):
            print('Ощущается как', str(feels), 'градуса')
        else:
            print('Ощущается как', str(feels), 'градусов')
    except:
        print("Такого города не существует")
