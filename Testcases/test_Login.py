from time import sleep

import pytest
from selenium import webdriver

from Configs.configs import Config
from Pages.Dashboard import Dashboard
from Pages.LoginPage import LoginPage
from Pages.Users import UsersPage
from Testcases.TestBase import *
import allure


class Test_Login(TestBase):
    @allure.severity(severity_level="Blocker")
    @allure.description("Login Test")
    def test_01_login(self):
        lp = LoginPage(self.driver)
        lp.login("Admin", "admin123")
        title = lp.get_page_title()
        assert title == "OrangeHRM", "Title Not Equal"

    @allure.severity(severity_level="Normal")
    @allure.description("Check Users Page")
    def test_02_check_users_page(self):

        Db = Dashboard(self.driver)
        user_ob = Db.navigate_to_users()
        user_ob.click_add_user()
        sleep(5)



