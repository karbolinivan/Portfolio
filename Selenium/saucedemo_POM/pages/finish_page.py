import allure

from base.base_class import Base
from utilities.logger import Logger


# Класс финальной страницы подтверждения заказа
class Finish_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #  Methods
    def finish(self):  # Осуществляет проверку url страницы подтверждения заказа и скриншот страницы
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver_g.current_url, method="finish")
