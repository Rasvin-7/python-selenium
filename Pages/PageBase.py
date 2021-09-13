from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PageBase:
    # driver = webdriver.Chrome()

    # driver.find_element_by_xpath().send_keys()

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        elem = self.driver.find_element_by_xpath(locator)
        elem.clear()
        elem.send_keys(text)

    def click_on(self, locator):
        elem = self.driver.find_element_by_xpath(locator)
        elem.click()

    def get_page_title(self):
        return self.driver.title

    def select_dropdown(self, locator, text):
        elem = self.driver.find_element_by_xpath(locator)
        select = Select(elem)
        select.select_by_visible_text(text)
