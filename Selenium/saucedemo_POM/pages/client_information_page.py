import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

#  Класс страницы ввода информации о пользователе
class Client_information_page(Base):

    url = 'https://www.saucedemo.com/checkout-step-one.html'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #  Locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    #  Getters
    def get_first_name(self):  # Выбор поля ввода Имени
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):   # Выбор поля ввода Фамилии
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):  # Выбор поля ввода индекса
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):   # Выбор кнопки продолжения
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    #  Actions
    def input_first_name(self, first_name):  # В поле ввода имени передается first_mane
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):  # В поле ввода имени передается last_mane
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):  # В поле ввода имени передается postal_code
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue_button(self):  # Клик на кнопку продолжения
        self.get_continue_button().click()
        print("Click on continue button")

    #  Methods
    def input_information(self):  # Осуществляет ввод данных пользователя и преход на следующую страницу
        with allure.step("Input Information"):
            Logger.add_start_step(method="input_information")
            self.driver_g.get(self.url)
            self.input_first_name("Ivan")
            self.input_last_name("Ivanov")
            self.input_postal_code("1234")
            self.click_continue_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="input_information")
