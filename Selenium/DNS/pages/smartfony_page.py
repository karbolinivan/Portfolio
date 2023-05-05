import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class SmartfonyPage(Base):
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.scroll_to_end = None
        self.driver_g = driver_g
        self.action = ActionChains(self.driver_g)

    # url
    url_iphone_sorted_high_low = 'https://www.dns-shop.ru/product/61340adf6bbbed20/67-smartfon-apple-iphone-14-pro-max-1000-gb-fioletovyj/'

    # Locators
    body = "body"
    filter_order_today = "//span[contains(text(), 'Под заказ: сегодня')]"
    filter_order_tomorrow = "//span[contains(text(), 'Под заказ: завтра')]"
    filter_order_later = "//span[contains(text(), 'Под заказ: позже')]"
    filter_productor = "//div[@data-id='brand']"
    filter_by_apple = "//span[contains(text(), 'Apple')]"
    filters_submit = "//button[@data-role='filters-submit']"
    top_filter_selected = "//span[@class='top-filter__label']"
    top_filter_by_high_low = "//span[contains(text(), 'Сначала дорогие')]"
    iphone_sorted_high_low = "//div[@class='catalog-products view-simple'][1]//div[@data-id='product'][1]/a[1]//span[1]"

    #  Getters
    def get_filter_order_today(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_order_today)))

    def get_filter_order_tomorrow(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_order_tomorrow)))

    def get_filter_order_later(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_order_later)))

    def get_productor(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_productor)))

    def get_filter_by_apple(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_by_apple)))

    def get_filters_submit(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.filters_submit)))

    def get_top_filter_selected(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.top_filter_selected)))

    def get_top_filter_by_high_low(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.top_filter_by_high_low)))

    def get_iphone_sorted_high_low(self):
        time.sleep(1)
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.iphone_sorted_high_low)))

    # Actions
    def click_filter_order_today(self):
        self.get_filter_order_today().click()
        print("Click on 'Под заказ: сегодня'")

    def click_filter_order_tomorrow(self):
        self.get_filter_order_tomorrow().click()
        print("Click on 'Под заказ: завтра'")

    def click_filter_order_later(self):
        self.get_filter_order_later().click()
        print("Click on 'Под заказ: позже'")

    def move_to_productor(self):
        self.action.move_to_element(self.get_productor()).perform()
        print("Move to 'Производитель'")

    def click_filter_by_apple(self):
        self.get_filter_by_apple().click()
        print("Click on 'Apple'")

    def move_to_filters_submit(self):
        self.action.move_to_element(self.get_filters_submit()).perform()
        print("Move to 'Применить")

    def click_filters_submit(self):
        self.get_filters_submit().click()
        print("Click on 'Применить'")

    def move_to_top_filter_selected(self):
        self.action.move_to_element(self.get_top_filter_selected()).perform()
        print("Move to 'Сортировка'")

    def click_top_filter_selected(self):
        self.get_top_filter_selected().click()
        print("Click on 'Сортировка'")

    def click_top_filter_by_high_low(self):
        self.get_top_filter_by_high_low().click()
        print("Click on 'Сначала дорогие'")

    def click_iphone_sorted_high_low(self):
        self.get_iphone_sorted_high_low().click()
        print("Click on 'Сначала дорогие'")

    # Methods
    def select_filter_by_apple(self):
        with allure.step("select filter by apple"):
            Logger.add_start_step(method="select_filter_by_apple")
            self.wait_load_page()
            self.move_to_productor()
            self.click_filter_by_apple()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_filter_by_apple")

    def select_filters_submit(self):
        with allure.step("select filters submit"):
            Logger.add_start_step(method="select_filters_submit")
            self.move_to_filters_submit()
            self.click_filters_submit()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_filters_submit")

    def select_top_filter_by_high_low(self):
        with allure.step("select top filter by high low"):
            Logger.add_start_step(method="select_top_filter_by_high_low")
            self.move_to_top_filter_selected()
            self.click_top_filter_selected()
            time.sleep(1)
            self.click_top_filter_by_high_low()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_top_filter_by_high_low")

    def select_iphone_sorted_high_low(self):
        with allure.step("select iphone sorted high low"):
            Logger.add_start_step(method="select_iphone_sorted_high_low")
            self.click_iphone_sorted_high_low()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_iphone_sorted_high_low")

    def select_filter_order_today(self):
        with allure.step("select filter order today"):
            Logger.add_start_step(method="select_filter_order_today")
            self.click_filter_order_today()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_filter_order_today")

    def select_filter_order_tomorrow(self):
        with allure.step("select filter order tomorrow"):
            Logger.add_start_step(method="select_filter_order_tomorrow")
            self.click_filter_order_tomorrow()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_filter_order_tomorrow")

    def select_filter_order_later(self):
        with allure.step("select filter order later"):
            Logger.add_start_step(method="select_filter_order_later")
            self.click_filter_order_later()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_filter_order_later")
