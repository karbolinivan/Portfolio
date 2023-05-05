import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from base.link import website_url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class MainPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # url
    url_smartfony_i_fototexnika = 'https://www.dns-shop.ru/catalog/17a890dc16404e77/smartfony-i-fototexnika/'

    # Locators
    smartfony_i_fototexnika = "//div[@class='catalog-menu__root-item'][3]//a[@class='catalog-menu__root-item-info catalog-menu__root-item-title'][1]"

    # Getters
    def get_smartfony_i_fototexnika(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartfony_i_fototexnika)))

    # Actions
    def click_smartfony_i_fototexnika(self):
        self.get_smartfony_i_fototexnika().click()
        print("Click on 'Смартфоны и фототехника'")

    # Methods
    def select_smartfony_i_fototexnika(self):
        with allure.step("select smartfony i fototexnika"):
            Logger.add_start_step(method="select_smartfony_i_fototexnika")
            self.driver_g.get(website_url)
            self.get_smartfony_i_fototexnika()
            self.click_smartfony_i_fototexnika()
            self.get_current_url()
            self.assert_url(self.url_smartfony_i_fototexnika)
            Logger.add_end_step(url=self.driver_g.current_url, method="select_smartfony_i_fototexnika")
