from Pages.PageBase import PageBase


class LoginPage(PageBase):
    username_xpath = "//input[@id='txtUsername']"
    password_xpath = "//input[@id='txtPassword']"
    loginbtn_xpath = "//input[@id='btnLogin']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        base = PageBase(self.driver)
        base.enter_text(self.username_xpath, username)
        base.enter_text(self.password_xpath, password)
        base.click_on(self.loginbtn_xpath)


