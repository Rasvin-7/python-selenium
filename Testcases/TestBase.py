import pytest
from pytest import *
from selenium import webdriver

from Configs import configs
from Configs.configs import Config


# driver = webdriver.Chrome()


@pytest.fixture(scope="class")
def init_driver(request):
    global driver1
    driver1 = webdriver.Chrome(executable_path=Config.chrome_path)
    driver1.get(Config.URL)

    request.cls.driver = driver1

    yield
    driver1.quit()



@pytest.mark.usefixtures("init_driver")
class TestBase:

    pass



