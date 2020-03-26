from selenium.webdriver.support.ui import Select
from model.currency import Currency
from datetime import datetime


class CurrencyHelper:

    def __init__(self, app):
        self.app = app

    def set_date(self, date):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@type='button']").click()
        deadline = datetime.strptime(date, "%d/%m/%Y")
        day = str(deadline.day)
        month = str(deadline.month - 1)
        year = str(deadline.year)
        # в календаре выбираем год
        select_year = Select(wd.find_element_by_class_name("ui-datepicker-year"))
        select_year.select_by_value(year)
        # в календаре выбираем месяц
        select_month = Select(wd.find_element_by_class_name("ui-datepicker-month"))
        select_month.select_by_value(month)
        # в календаре выбираем день
        table = wd.find_element_by_xpath(".//*[@class='ui-datepicker-calendar']")
        table.find_element_by_xpath("//a[contains(text(),'%s')]" % day).click()

    def get_curr(self, date):
        wd = self.app.wd
        self.app.open_currencies_page()
        self.set_date(date)
        list = []
        table = wd.find_element_by_xpath(".//*[@class='table']/table/tbody")
        for row in table.find_elements_by_tag_name("tr")[1:]:
            cells = row.find_elements_by_tag_name("td")
            num_code = cells[0].text
            char_code = cells[1].text
            nominal = cells[2].text
            name = cells[3].text
            value = cells[4].text
            list.append(Currency(numCode=num_code, charCode=char_code, nominal=nominal, name=name, value=value))
        return list