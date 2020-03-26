from selenium import webdriver
from fixture.currency import CurrencyHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.set_window_size(800, 600)
        self.wd.implicitly_wait(3)
        self.currency = CurrencyHelper(self)

    def open_currencies_page(self):
        wd = self.wd
        wd.get('http://cbr.ru/currency_base/daily/')

    def destroy(self):
        self.wd.quit()

