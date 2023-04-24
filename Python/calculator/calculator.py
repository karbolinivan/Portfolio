while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        symbol = input('Введите арифметическое действие (/, *, +, -): ')
        if symbol == "/" or symbol == "*" or symbol == "+" or symbol == "-":  # Проверка на ввод арифметического знака
            if symbol == "/":
                result = a / b
                print(f"Результат деления {a} на {b} равен: {result}")
            elif symbol == "*":
                result = a * b
                print(f"Результат умножения {a} и {b} равен: {result}")
            elif symbol == "+":
                result = a + b
                print(f"Результат сложения {a} и {b} равен: {result}")
            elif symbol == "-":
                result = a - b
                print(f"Результат вычитания {a} из {b} равен: {result}")
        else:
            print("Неверный арифметический знак.")
    except ZeroDivisionError:
        print("На ноль делить нельзя.")  # Проверка деления на ноль
    except ValueError:
        print("Введено неверное значение.")  # Проверка на ввод строчных значений