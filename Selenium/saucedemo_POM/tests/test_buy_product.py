import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.path import webdriver_path
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


# @pytest.mark.run(order=3)
@allure.description("Test Buy Product 1")
def test_buy_product_1(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test 1")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_products_1()

    cp = Cart_page(driver_g)
    cp.product_confirmation()

    ci = Client_information_page(driver_g)
    ci.input_information()

    fb = Payment_page(driver_g)
    fb.payment()

    f = Finish_page(driver_g)
    f.finish()

    print("Finish Test 1")
    time.sleep(1)
    driver_g.close()


@allure.description("Test Buy Product 2")
# @pytest.mark.run(order=1)
def test_buy_product_2(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test 2")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_products_2()

    cp = Cart_page(driver_g)
    cp.product_confirmation()

    ci = Client_information_page(driver_g)
    ci.input_information()

    fb = Payment_page(driver_g)
    fb.payment()

    f = Finish_page(driver_g)
    f.finish()

    print("Finish Test 2")
    time.sleep(1)
    driver_g.close()


@allure.description("Test Buy Product 3")
# @pytest.mark.run(order=2)
def test_buy_product_3(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test 3")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_products_3()

    cp = Cart_page(driver_g)
    cp.product_confirmation()

    ci = Client_information_page(driver_g)
    ci.input_information()

    fb = Payment_page(driver_g)
    fb.payment()

    f = Finish_page(driver_g)
    f.finish()

    print("Finish Test 3")
    time.sleep(1)
    driver_g.close()


@allure.description("Test Buy Product 4")
def test_buy_product_4(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test 4")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_products_4()

    cp = Cart_page(driver_g)
    cp.product_confirmation()

    ci = Client_information_page(driver_g)
    ci.input_information()

    fb = Payment_page(driver_g)
    fb.payment()

    f = Finish_page(driver_g)
    f.finish()

    print("Finish Test 4")
    time.sleep(1)
    driver_g.close()


@allure.description("Test Buy Product 5")
def test_buy_product_5(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test 5")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_products_5()

    cp = Cart_page(driver_g)
    cp.product_confirmation()

    ci = Client_information_page(driver_g)
    ci.input_information()

    fb = Payment_page(driver_g)
    fb.payment()

    f = Finish_page(driver_g)
    f.finish()

    print("Finish Test 5")
    time.sleep(1)
    driver_g.close()


@allure.description("Test Buy Product 6")
def test_buy_product_6(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test 6")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_products_6()

    cp = Cart_page(driver_g)
    cp.product_confirmation()

    ci = Client_information_page(driver_g)
    ci.input_information()

    fb = Payment_page(driver_g)
    fb.payment()

    f = Finish_page(driver_g)
    f.finish()

    print("Finish Test 6")
    time.sleep(1)
    driver_g.close()




