import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

# Класс страницы оплаты
class Payment_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #  Locators
    finish_button = "//button[@id='finish']"

    #  Getters
    def get_finish_button(self):  # Выбор кнопки finish
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    #  Actions
    def click_finish_button(self):  # Клик на кнопку finish
        self.get_finish_button().click()
        print("Click on finish button")

    #  Methods
    #  Осуществляет подтверждение заказа
    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            self.get_current_url()
            self.click_finish_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="payment")
