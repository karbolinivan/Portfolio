import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class SmartfonyIFototexnikaPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    url_smartfony_i_gadzhety = 'https://www.dns-shop.ru/catalog/af47fe7c3bae7fd7/smartfony-i-gadzhety/'

    # Locators
    smartfony_i_gadzhety = "//a[@class='subcategory__item ui-link ui-link_blue'][1]//span[@class='subcategory__title'][1]"

    #  Getters
    def get_smartfony_i_gadzhety(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartfony_i_gadzhety)))

    # Actions
    def click_smartfony_i_gadzhety(self):
        self.get_smartfony_i_gadzhety().click()
        print("Click on 'Смартфоны и гаджеты'")

    # Methods
    def select_smartfony_i_gadzhety(self):
        with allure.step("select smartfony i gadzhety"):
            Logger.add_start_step(method="select_smartfony_i_gadzhety")
            self.click_smartfony_i_gadzhety()
            self.get_current_url()
            self.assert_url(self.url_smartfony_i_gadzhety)
            Logger.add_end_step(url=self.driver_g.current_url, method="select_smartfony_i_gadzhety")
