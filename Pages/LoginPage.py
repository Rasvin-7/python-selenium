from Pages.PageBase import PageBase


class LoginPage(PageBase):
    username_xpath = "//input[@id='txtUsername']"
    password_xpath = "//input[@id='txtPassword']"
    loginbtn_xpath = "//input[@id='btnLogin']"

    invalid_text = "//span[@id='spanMessage']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        base = PageBase(self.driver)
        base.enter_text(self.username_xpath, username)
        base.enter_text(self.password_xpath, password)
        base.click_on(self.loginbtn_xpath)

    def check_reason(self):
        base = PageBase(self.driver)
        base.check_elem(self.invalid_text)
        text = base.get_text()
        return text



