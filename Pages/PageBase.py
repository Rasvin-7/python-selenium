from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageBase:
    # driver = webdriver.Chrome()
    #
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

    def check_elem(self, locator):
        wait = WebDriverWait(self.driver, 5)
        elem = self.driver.find_element_by_xpath(locator)
        elem1 = wait.until(ec.visibility_of_element_located(elem))
        if elem1:
            return True
        else:
            return False

    def get_text(self, locator):
        text = self.driver.find_element_by_xpath(locator).text
        return text
