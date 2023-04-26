from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Users():

    def authorization(self, list_login, all_password):
        self.list_login = list_login
        self.all_password = all_password

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('') # Указать путь к драйверу
        driver_g = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver_g.get(base_url)
        driver_g.delete_all_cookies()
        driver_g.maximize_window()

        print("============Tests============")

        for user in self.list_login:

            try:
                """Authorization"""
                user_name = WebDriverWait(driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
                user_name.send_keys(user)
                print("Login Page - Input Login: " + str(user) + ".")

                password = WebDriverWait(driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
                password.send_keys(all_password)
                print("Login Page - Input Password: " + str(all_password) + ".")

                button_login = WebDriverWait(driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
                button_login.click()
                print("Login Page - Click on Login Button.")

                """Test"""
                success_test = WebDriverWait(driver_g, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
                value_success_test = success_test.text
                assert value_success_test == "Products"
                print("Authorization - Test Passed.")

                """Log Out"""
                burger_menu = WebDriverWait(driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
                burger_menu.click()
                print("Select - Open Burger Menu.")

                logout = WebDriverWait(driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
                logout.click()
                print("Select - Logout.")
            except:
                """Login Error"""
                error_login = WebDriverWait(driver_g, 1).until(
                    EC.element_to_be_clickable((By.XPATH, "//h3[@data-test='error']")))
                value_error_login = error_login.text
                print("Authorization - Test Failed. Error: '" + value_error_login + "'.")

                """Delete field"""
                user_name.send_keys(Keys.CONTROL + "a")
                user_name.send_keys(Keys.DELETE)
                password.send_keys(Keys.CONTROL + "a")
                password.send_keys(Keys.DELETE)


        driver_g.close()
        print("=============End==============")

print("=====Users_and_Password=====")
list_login = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
password = "secret_sauce"
print("Login list: " + str(list_login) + '.')
print("Password: " + str(password) + '.')

test_authorization = Users()
test_authorization.authorization(list_login, password)