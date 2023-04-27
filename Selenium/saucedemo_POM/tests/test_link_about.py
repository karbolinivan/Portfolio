import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.path import webdriver_path
from pages.login_page import Login_page
from pages.main_page import Main_page


@allure.description("Test Link About")
def test_link_about(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(webdriver_path)
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_menu_about()

    time.sleep(2)
    driver_g.close()
