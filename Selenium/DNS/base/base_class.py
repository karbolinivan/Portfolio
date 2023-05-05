import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver_g):
        self.driver_g = driver_g

    def wait_load_page(self):
        return WebDriverWait(self.driver_g, 10).until(EC.presence_of_element_located((By.TAG_NAME, "HTML")))

    def reload_page(self):
        return self.driver_g.refresh()

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("Current url: " + get_url)

    def get_screenshot(self):
        now_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f"screenshot_{now_data}.png"
        self.driver_g.save_screenshot("screen\\" + name_screenshot)

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print("Good value URL")
