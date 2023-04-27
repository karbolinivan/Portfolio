import datetime


  #  Базовый класс, который описывает общие методы для классов-потомков
class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""
    def get_screenshot(self):
       now_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
       name_screenshot = 'screenshot' + now_data + ".png"
       self.driver_g.save_screenshot("screen\\" + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print('Good value URL')


