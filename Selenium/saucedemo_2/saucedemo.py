from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def item(input_number):

    """Определяем пути названия и цены товара, а также кнопки 'добавить'"""
    # У каждой карточки товара есть id="item_4_title_link".
    # Будем менять цифру товара на введенное пользователем число.
    # И отностительно выбраного товара определять цену.
    item_number = input_number - 1  # номер товара в HTML начинается с 0
    xpath_product = "//a[@id='item_" + str(item_number) + "_title_link']"
    xpath_price_product = "//a[@id='item_" + str(item_number) + "_title_link']/..//following-sibling::div/div[@class='inventory_item_price']"
    xpath_select_product = "//a[@id='item_" + str(item_number) + "_title_link']/..//following-sibling::div/button"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('') # Указать путь к драйверу
    driver_g = webdriver.Chrome(options=options, service=g)
    base_url = 'https://www.saucedemo.com/'
    driver_g.get(base_url)
    driver_g.delete_all_cookies()
    driver_g.minimize_window()

    """Authorization"""
    login_standard_user = "standard_user"
    password_all = "secret_sauce"


    user_name = driver_g.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys(login_standard_user)
    print("Login Page - Input Login")

    password = driver_g.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys(password_all)
    print("Login Page - Input Password")

    button_login = driver_g.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()
    print("Login Page - Click on Login Button")


    """Info Product"""
    product = driver_g.find_element(By.XPATH, xpath_product)
    value_product = product.text
    print("Select - Name Product " + str(input_number) + ": " + value_product)

    price_product = driver_g.find_element(By.XPATH, xpath_price_product)
    value_price_product = price_product.text
    value_price_product = float(value_price_product.replace('$', ''))
    print("Select - Price Product " + str(input_number) + ": $" + str(value_price_product))

    select_product = driver_g.find_element(By.XPATH, xpath_select_product)
    select_product.click()
    print("Select - Add Product " + str(input_number))

    """Info Cart"""
    cart = driver_g.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart.click()
    print("Select - Enter Cart")

    cart_product = driver_g.find_element(By.XPATH, xpath_product)
    cart_value_product = cart_product.text
    print("Cart - Name Product " + str(input_number) + ": " + cart_value_product)

    cart_price_product = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_value_price_product = cart_price_product.text
    cart_value_price_product = float(cart_value_price_product.replace('$', ''))
    print("Cart - Price Product " + str(input_number) + ": $" + str(cart_value_price_product))

    checkout = driver_g.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()
    print("Cart - Click Checkout")

    """Checkout Information"""
    first_name = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
    first_name.send_keys("Ivan")
    print("Checkout - Input First Name")

    last_name = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
    last_name.send_keys("Petrov")
    print("Checkout - Input last_name")

    zip_code = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
    zip_code.send_keys("000000")
    print("Checkout - Input Zip")

    cont = driver_g.find_element(By.XPATH, "//input[@id='continue']")
    cont.click()
    print("Checkout - Click on Continue")

    """Overview"""
    finish_product = driver_g.find_element(By.XPATH, xpath_product)
    finish_value_product = finish_product.text
    print("Finish - Name Product " + str(input_number) + ": " + finish_value_product)

    finish_price_product = driver_g.find_element(By.XPATH, xpath_price_product)
    finish_value_price_product = finish_price_product.text
    finish_value_price_product = float(finish_value_price_product.replace('$', ''))
    print("Finish - Price Product " + str(input_number) + ": $" + str(finish_value_price_product))

    """Total price"""
    item_total = driver_g.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
    value_item_total = item_total.text
    value_item_total = float(value_item_total.replace('Item total: $', ''))
    print("Finish - Item total: $" + str(value_item_total))

    tax = driver_g.find_element(By.XPATH, "//div[@class='summary_tax_label']")
    value_tax = tax.text
    value_tax = float(value_tax.replace('Tax: $', ''))
    print("Finish - Tax: $" + str(value_tax))

    total_price = driver_g.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
    value_total_price = total_price.text
    value_total_price = float(value_total_price.replace('Total: $', ''))
    print("Finish - Total: $" + str(value_total_price))

    finish = driver_g.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print("Finish - Click on Finish")

    driver_g.close()

    """Tests"""
    print("============Tests============")
    """Проверка названия и цены товара в корзине"""
    if value_product == cart_value_product and value_price_product == cart_value_price_product:
        print("Cart - Product " + str(input_number) + " - Test Passed.")
    else:
        print("Cart - Product " + str(input_number) + " - Test Failed.")

    """Проверка названия и цены товара перед оплатой"""
    if value_product == finish_value_product and value_price_product == finish_value_price_product:
        print("Finish - Product " + str(input_number) + " - Test Passed.")
    else:
        print("Finish - Product " + str(input_number) + " - Test Failed.")

    """Проверка итоговой цены"""
    if finish_value_price_product == value_item_total:
        print("Finish - Item Total - Test Passed.")
    else:
        print("Finish - Item Total - Test Failed.")

    """Проверка итоговой цены с учетом налога"""
    tax_product = round((value_item_total + value_tax), 2)

    if tax_product == value_total_price:
        print("Finish - Total Price - Test Passed.")
    else:
        print("Finish - Total Price - Test Failed.")
    print("=============End==============")

    print("Дождитесь обновления программы")

while True:
    print("Введите номер товара от 1 до 6.")
    input_number = int(input())
    if input_number >= 1 and input_number <= 6:
        item(input_number)
    else:
        print("Неверный номер товара.")