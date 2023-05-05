import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class SmartfonyIGadzhetyPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    url_smartfony = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"

    # Locators
    smartfony = "//a[@class='subcategory__item ui-link ui-link_blue'][1]//span[@class='subcategory__title']"

    #  Getters
    def get_smartfony(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartfony)))

    # Actions
    def click_smartfony(self):
        self.get_smartfony().click()
        print("Click on 'Смартфоны'")

    # Methods
    def select_smartfony(self):
        with allure.step("select smartfony"):
            Logger.add_start_step(method="select_smartfony")
            self.click_smartfony()
            self.get_current_url()
            self.assert_url(self.url_smartfony)
            Logger.add_end_step(url=self.driver_g.current_url, method="select_smartfony")
