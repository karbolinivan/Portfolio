from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
from base.base_class import Base
from base.link import webdriver_path
from pages.cart_page import CartPage
from pages.checkout_main_page import CheckoutMainPage
from pages.main_page import MainPage
from pages.product_page import IphoneSortedHighLowPage
from pages.smartfony_i_fototexnika_page import SmartfonyIFototexnikaPage
from pages.smartfony_i_gadzhety_page import SmartfonyIGadzhetyPage
from pages.smartfony_page import SmartfonyPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@allure.description("Test Buy Iphone Sorted by High to Low")
def test_buy_phone(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path=webdriver_path)
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"
    driver_g = webdriver.Chrome(options=options, service=g, desired_capabilities=capabilities)
    driver_g.maximize_window()

    print("Start Test 1")

    mp = MainPage(driver_g)
    mp.select_smartfony_i_fototexnika()

    sifp = SmartfonyIFototexnikaPage(driver_g)
    sifp.select_smartfony_i_gadzhety()

    sigp = SmartfonyIGadzhetyPage(driver_g)
    sigp.select_smartfony()

    sp = SmartfonyPage(driver_g)
    sp.select_filter_order_today()
    sp.select_filter_order_tomorrow()
    sp.select_filter_order_later()
    sp.select_filter_by_apple()
    sp.select_filters_submit()
    sp.select_top_filter_by_high_low()
    sp.select_iphone_sorted_high_low()

    ishl = IphoneSortedHighLowPage(driver_g)
    ishl.select_button_buy()
    ishl.select_button_cart()

    cp = CartPage(driver_g)
    cp.select_buy_btn_main()

    cmp = CheckoutMainPage(driver_g)
    cmp.input_phone_number_email()
    cmp.select_confirm()

    screen = Base(driver_g)
    screen.get_screenshot()

    driver_g.close()
    print("Finish Test 1")
