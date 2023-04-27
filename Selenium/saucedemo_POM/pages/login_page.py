from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure


#  Класс авторизации пользователя на сайте
class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #  Locators
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"

    #  Getters
    def get_user_name(self):  # Выбор поля ввода login
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):  # Выбор поля ввода password
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):  # Выбор кнопки авторизации на сайте
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):  # Выбор слова "Products" для проверки после авторизации
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #  Actions
    def input_user_name(self, user_name):  # Ввод в поле логина ures_name
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):  # Ввод в поле пароля password
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):  # Клик на кнопку авторизации
        self.get_login_button().click()
        print("Click Login Button")

    #  Methods
    def authorization(self): # Осуществляет авторизацию и проверку авторизации пользователя на сайте.
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver_g.get(self.url)
            self.driver_g.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_word(self.get_main_word(), "Products")
            Logger.add_end_step(url=self.driver_g.current_url, method="authorization")