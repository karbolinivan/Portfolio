from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('') # Задать путь к драйверу
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()


login_standard_user = "standard_user"
password_all = "secret_sauce"


user_name = driver_g.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Login Page - Input Login")

password = driver_g.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Login Page - Input Passowrd")

button_login = driver_g.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Login Page - Click on Login Button")


"""Info First Product"""
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print("Select - Name First Product: " + value_product_1)

price_product_1 = driver_g.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text
value_price_product_1 = float(value_price_product_1.replace('$', ''))
print("Select - Price First Product: $" + str(value_price_product_1))

select_product_1 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select - Add First Product")


"""Info Second Product"""
product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_2 = product_2.text
print("Select - Name Second Product: " + value_product_2)

price_product_2 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
value_price_product_2 = float(value_price_product_2.replace('$', ''))
print("Select - Price Second Product: $" + str(value_price_product_2))

select_product_2 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_2.click()
print("Select - Add Second Product")


"""Info Cart"""
"""First Product"""
cart = driver_g.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Select - Enter Cart")

cart_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
cart_value_product_1 = cart_product_1.text
print("Cart - Name First Product: " + cart_value_product_1)

cart_price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_value_price_product_1 = cart_price_product_1.text
cart_value_price_product_1 = float(cart_value_price_product_1.replace('$', ''))
print("Cart - Price First Product: $" + str(cart_value_price_product_1))


"""Second Product"""
cart_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
cart_value_product_2 = cart_product_2.text
print("Cart - Name Second Product: " + cart_value_product_2)

cart_price_product_2 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
cart_value_price_product_2 = cart_price_product_2.text
cart_value_price_product_2 = float(cart_value_price_product_2.replace('$', ''))
print("Cart - Price Second Product: $" + str(cart_value_price_product_2))

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
"""First Product"""
finish_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
finish_value_product_1 = finish_product_1.text
print("Finish - Name First Product: " + finish_value_product_1)

finish_price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
finish_value_price_product_1 = finish_price_product_1.text
finish_value_price_product_1 = float(finish_value_price_product_1.replace('$', ''))
print("Finish - Price First Product: $" + str(finish_value_price_product_1))

"""Second Product"""
finish_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
finish_value_product_2 = finish_product_2.text
print("Finish - Name First Product: " + finish_value_product_2)

finish_price_product_2 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
finish_value_price_product_2 = finish_price_product_2.text
finish_value_price_product_2 = float(finish_value_price_product_2.replace('$', ''))
print("Finish - Price First Product: $" + str(finish_value_price_product_2))


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

"""Tests"""
print("============Tests============")
"""Товар №1. Проверка названия и цены товара в корзине"""
if value_product_1 == cart_value_product_1 and value_price_product_1 == cart_value_price_product_1:
    print("Cart - Product 1 - Test Passed.")
else:
    print("Cart - Product 1 - Test Failed.")

"""Товар №2. Проверка названия и цены товара в корзине"""
if value_product_2 == cart_value_product_2 and value_price_product_2 == cart_value_price_product_2:
    print("Cart - Product 2 - Test Passed.")
else:
    print("Cart - Product 2 - Test Failed.")

"""Товар №1. Проверка названия и цены товара перед оплатой"""
if value_product_1 == finish_value_product_1 and value_price_product_1 == finish_value_price_product_1:
    print("Finish - Product 1 - Test Passed.")
else:
    print("Finish - Product 1 - Test Failed.")

"""Товар №2. Проверка названия и цены товара перед оплатой"""
if value_product_2 == finish_value_product_2 and value_price_product_2 == finish_value_price_product_2:
    print("Finish - Product 2 - Test Passed.")
else:
    print("Finish - Product 2 - Test Failed.")

"""Проверка итоговой суммы"""
summ_products = finish_value_price_product_1 + finish_value_price_product_2
if summ_products == value_item_total:
    print("Finish - Item Total - Test Passed.")
else:
    print("Finish - Item Total - Test Failed.")

"""Проверка итоговой суммы с учетом налога"""
tax_summ_products = summ_products + value_tax
if tax_summ_products == value_total_price:
    print("Finish - Total Price - Test Passed.")
else:
    print("Finish - Total Price - Test Failed.")
print("=============End==============")
driver_g.close()
