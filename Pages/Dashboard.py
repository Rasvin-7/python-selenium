from selenium.webdriver.common.by import By

from Pages.PageBase import PageBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from Pages.Users import UsersPage


# driver1 = webdriver.Chrome()
# driver1.find_element_by_xpath()

class Dashboard(PageBase):

    admin_menu = "//b[contains(text(),'Admin')]"
    user_mgnt = "//a[@id='menu_admin_UserManagement']"
    users = "//a[@id='menu_admin_viewSystemUsers']"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_users(self):
        action = ActionChains(self.driver)

        admin = self.driver.find_element_by_xpath(self.admin_menu)
        umt = self.driver.find_element_by_xpath(self.user_mgnt)
        user = self.driver.find_element_by_xpath(self.users)

        action.move_to_element(admin).move_to_element(umt).perform()
        action.move_to_element(user).click().perform()
        return UsersPage(self.driver)
