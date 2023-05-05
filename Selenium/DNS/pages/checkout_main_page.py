import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class CheckoutMainPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.action = ActionChains(self.driver_g)

    value_phone_number = "1234567890"
    value_email = "test@gmail.com"

    # Locators
    phone_number = "//input[@type='tel']"
    email = "//input[@type='text']"
    confirm = "//div[@class='checkout-container__apply_BrK']//button[1]"

    #  Getters
    def get_phone_number(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_email(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_confirm(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm)))

    # Actions
    def input_phone_number(self, value_phone):
        self.get_phone_number().send_keys(value_phone)
        print("Введен номер: " + value_phone)

    def input_email(self, value_mail):
        self.get_email().send_keys(value_mail)
        print("Введен email: " + value_mail)

    def move_to_confirm(self):
        self.action.move_to_element(self.get_confirm()).perform()
        print("Move to 'Подтвердить заказ'")

    def click_confirm(self):
        self.get_confirm().click()
        print("Click on 'Подтвердить заказ'")

    # Methods
    def input_phone_number_email(self):
        with allure.step("input phone number email"):
            Logger.add_start_step(method="input_phone_number_email")
            time.sleep(1)
            self.input_phone_number(self.value_phone_number)
            self.input_email(self.value_email)
            Logger.add_end_step(url=self.driver_g.current_url, method="input_phone_number_email")

    def select_confirm(self):
        with allure.step("select confirm"):
            Logger.add_start_step(method="select_confirm")
            self.move_to_confirm()
            self.click_confirm()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_confirm")
