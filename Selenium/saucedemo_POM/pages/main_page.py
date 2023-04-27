import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

# Класс основной страницы сайта
class Main_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #  Locators
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    select_product_4 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    select_product_5 = "//button[@id='add-to-cart-sauce-labs-onesie']"
    select_product_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    #  Getters
    def get_product_1(self):  # Выбор продукта 1
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_2(self):  # Выбор продукта 2
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_product_3(self):  # Выбор продукта 3
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_product_4(self):  # Выбор продукта 4
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_4)))

    def get_product_5(self):  # Выбор продукта 5
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_5)))

    def get_product_6(self):  # Выбор продукта 6
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_6)))

    def get_cart(self):  # Выбор корзины
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):  # Выбор меню навигации
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):  # Выбор пункта Link about
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    #  Actions
    def click_select_product_1(self):  # Добавление товара в корзину
        self.get_product_1().click()
        print("Select Product 1")

    def click_select_product_2(self):  # Добавление товара в корзину
        self.get_product_2().click()
        print("Select Product 2")

    def click_select_product_3(self):  # Добавление товара в корзину
        self.get_product_3().click()
        print("Select Product 3")

    def click_select_product_4(self):  # Добавление товара в корзину
        self.get_product_4().click()
        print("Select Product 4")

    def click_select_product_5(self):  # Добавление товара в корзину
        self.get_product_5().click()
        print("Select Product 5")

    def click_select_product_6(self):  # Добавление товара в корзину
        self.get_product_6().click()
        print("Select Product 6")

    def click_cart(self):  # Переход в корзину товаров
        self.get_cart().click()
        print("Click on cart")

    def click_menu(self):  # Открытие меню-навигации
        self.get_menu().click()
        print("Click on menu")

    def click_link_about(self):  # Переход по ссылки Link about
        self.get_link_about().click()
        print("Click on link about")

    #  Methods
    #  Методы добавляют выбраный товар в корзину.
    def select_products_1(self):
        with allure.step("Select Products 1"):
            Logger.add_start_step(method="select_products_1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_products_1")


    def select_products_2(self):
        with allure.step("Select Products 2"):
            Logger.add_start_step(method="select_products_2")
            self.get_current_url()
            self.click_select_product_2()
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_products_2")


    def select_products_3(self):
        with allure.step("Select Products 3"):
            Logger.add_start_step(method="select_products_3")
            self.get_current_url()
            self.click_select_product_3()
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_products_3")


    def select_products_4(self):
        with allure.step("Select Products 4"):
            Logger.add_start_step(method="select_products_4")
            self.get_current_url()
            self.click_select_product_4()
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_products_4")


    def select_products_5(self):
        with allure.step("Select Products 5"):
            Logger.add_start_step(method="select_products_5")
            self.get_current_url()
            self.click_select_product_5()
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_products_5")


    def select_products_6(self):
        with allure.step("Select Products 6"):
            Logger.add_start_step(method="select_products_6")
            self.get_current_url()
            self.click_select_product_6()
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_products_6")

    #  Метод осуществляет переход по ссылке Link about и проверку открытой страницы.
    def select_menu_about(self):
        with allure.step("Select Menu About"):
            Logger.add_start_step(method="select_menu_about")
            self.get_current_url()
            self.click_menu()
            self.click_link_about()
            self.assert_url('https://saucelabs.com/')
            Logger.add_end_step(url=self.driver_g.current_url, method="select_menu_about")
