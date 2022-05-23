import pytest

from Pages.LoginPage import LoginPage
from config import TestData
from time import sleep

@pytest.mark.usefixtures("init_driver")
class Testlogin:

    def test_wrong_Username(self):
        login = LoginPage(self.driver)
        login.do_login(TestData.wrong_UserName, TestData.PASSWORD)
        login.assert_correct_error("Wrong login/password")
        sleep(5)
    
    def test_wrong_Password(self):
        login = LoginPage(self.driver)
        login.do_login(TestData.USER_NAME, TestData.wrong_Password)
        login.assert_correct_error("Wrong login/password")
        sleep(5)

    def test_login(self):
        login = LoginPage(self.driver)
        login.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(5)
        login.log_out()
    



