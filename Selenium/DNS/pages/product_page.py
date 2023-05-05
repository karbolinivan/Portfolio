import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class IphoneSortedHighLowPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # url
    url_cart = "https://www.dns-shop.ru/cart/"

    # Locators
    button_buy = "//div[@class='product-buy product-buy_one-line']/button[2]"
    button_cart = "//span[@class='cart-link-counter__badge']"

    #  Getters
    def get_button_buy(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_cart(self):
        return WebDriverWait(self.driver_g, 10).until(EC.visibility_of_element_located((By.XPATH, self.button_cart)))

    # Actions
    def click_button_buy(self):
        self.get_button_buy().click()
        print("Click on 'Купить'")

    def click_button_cart(self):
        self.get_button_cart().click()
        print("Click on 'Корзина'")

    # Methods
    def select_button_buy(self):
        with allure.step("select button buy"):
            Logger.add_start_step(method="select_button_buy")
            time.sleep(1)
            self.click_button_buy()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_button_buy")

    def select_button_cart(self):
        with allure.step("select button cart"):
            Logger.add_start_step(method="select_button_cart")
            self.click_button_cart()
            time.sleep(1)
            self.get_current_url()
            self.assert_url(self.url_cart)
            Logger.add_end_step(url=self.driver_g.current_url, method="select_button_cart")
