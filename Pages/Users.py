from selenium.webdriver.common.by import By

from Pages.PageBase import PageBase


class UsersPage(PageBase):
    add_user_button = "//input[@id='btnAdd']"

    def __init__(self, driver):
        self.driver = driver

    def click_add_user(self):
        pb = PageBase(self.driver)
        pb.click_on(self.add_user_button)
