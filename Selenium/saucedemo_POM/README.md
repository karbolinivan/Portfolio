# Проект:

Учебный проект автотестирования сайта: <a href="https://www.saucedemo.com/" target="_blank">https://www.saucedemo.com/</a>  
Проект реализован с использованием модели Page Object.

# Структура проекта:

base – содержит общие файлы для всего проекта.  
logs – содержит сгенерированные логи автотестов.  
pages – содержит описание страниц тестируемого сайта.  
screen - содержит сохраненные скриншоты выполненных автотестов.  
test_result – содержит отчет Allure.  
test – содержит автотесты.  
Utilites – содержит логгер, который сохраняет логи в папку logs.

# Путь:

В base\path.py необходимо указать путь к webdriver.

# Запуск автотестов:

python -m pytest -s -v

# Запуск автотестов с сохранением отчета Allure:

python -m pytest --alluredir=test_result

# Запуск отчета Allure:

allure serve test_results/

Пример отчета Allure можно посмотреть здесь: <a href="https://github.com/karbolinivan/Portfolio/tree/main/Allure/saucedemo" target="_blank">Report</a>
