import pytest
from selenium import webdriver
from config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    yield
    web_driver.close()
