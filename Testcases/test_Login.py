import sys
from contextlib import suppress
from random import random
from time import sleep

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Configs.configs import Config
from Pages.Dashboard import Dashboard
from Pages.LoginPage import LoginPage
from Pages.Users import UsersPage
from Testcases.TestBase import *
import allure

from Utils.TestUtils import TestUtils


# tu = TestUtils()
# creds = tu.getData()

class Test_Login(TestBase):
    tu = TestUtils()
    creds = tu.getData()

    @allure.severity(severity_level="Blocker")
    @allure.description("Login Test")
    @pytest.mark.parametrize("admin,password", argvalues=creds)
    def test_01_login(self, admin, password):

        lp = LoginPage(self.driver)
        Db = Dashboard(self.driver)
        lp.login(admin, password)
        sleep(5)
        try:
            title = lp.get_page_title()
            assert title == "OrangeHRM", "Title Not Equal"
            Db.logout()
            sleep(5)
        except Exception:
            pass

    # @allure.severity(severity_level="Normal")
    # @allure.description("Check Users Page")
    # def test_02_check_users_page(self):
    #     lp = LoginPage(self.driver)
    #     Db = Dashboard(self.driver)
    #     lp.login("Admin", "admin123")
    #     user_ob = Db.navigate_to_users()
    #     user_ob.click_add_user()
    #     sleep(5)
