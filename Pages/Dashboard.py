from time import sleep

from selenium.webdriver.common.by import By

from Pages.PageBase import PageBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

from Pages.Users import UsersPage


# driver1 = webdriver.Chrome()
# driver1.find_element_by_xpath()

class Dashboard(PageBase):
    welcome_link = "//a[@id='welcome']"
    logout_link = "div:nth-child(1) div.panelContainer:nth-child(15) ul:nth-child(1) li:nth-child(3) > a:nth-child(1)"

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

    def logout(self):
        wel = self.driver.find_element_by_xpath(self.welcome_link)
        wel.click()

        # logout = self.driver.find_element_by_xpath(self.logout_link)
        # logout.click()
        Log = self.driver.find_element_by_css_selector(self.logout_link)
        action = ActionChains(self.driver)
        action.move_to_element(wel).perform()
        sleep(2)
        action.move_to_element(Log).perform()
        Log.click()

    def check_welcome(self):
        pb = PageBase(self.driver)
        return pb.check_elem(self.welcome_link)

