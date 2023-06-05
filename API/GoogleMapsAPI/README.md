# Проект:

Автотест для GoogleMapsAPI.

# Шаги автотеста:

1. Создание новой локации.
2. Запрос созданной локации.
3. Изменение локации.
4. Запрос измененной локации.
5. Удаление локации.
6. Запрос удаленной локации

# Структура проекта:

logs – содержит сгенерированные логи автотестов.  
test_result – содержит отчет Allure.  
tests – содержит автотесты.  
utils – содержит инструменты для построения автотестов.

# Запуск автотестов:

```Python
python -m pytest -s -v
```

# Запуск автотестов с сохранением отчета Allure:

```Python
python -m pytest --alluredir=test_result
```

# Запуск отчета Allure:

```Python
allure serve test_results/
```

Пример отчета Allure можно посмотреть здесь: <a href="https://github.com/karbolinivan/Portfolio/tree/main/Allure/GoogleMapsAPI" target="_blank">Report</a>
