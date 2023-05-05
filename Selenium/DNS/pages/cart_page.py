import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class CartPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    url_checkout_main = "https://www.dns-shop.ru/checkout-main/"

    # Locators
    buy_btn_main = "//button[@id='buy-btn-main']"

    #  Getters
    def get_buy_btn_main(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_btn_main)))

    # Actions
    def click_buy_btn_main(self):
        self.get_buy_btn_main().click()
        print("Click on 'Перейти к оформлению'")

    # Methods
    def select_buy_btn_main(self):
        with allure.step("select buy btn main"):
            Logger.add_start_step(method="select_buy_btn_main")
            self.click_buy_btn_main()
            time.sleep(3)
            self.get_current_url()
            self.assert_url(self.url_checkout_main)
            Logger.add_end_step(url=self.driver_g.current_url, method="select_buy_btn_main")
