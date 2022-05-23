import pytest

from Pages.HomePage import HomePage
from config import TestData
from time import sleep
from Pages.LoginPage import LoginPage
from Pages.OrderPage import OrderPage

@pytest.mark.usefixtures("init_driver")
class TestOrderCreation:

   def test_login(self):
        login = LoginPage(self.driver)
        login.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(1)

   def test_nav_SalesPage(self):
        homePage = HomePage(self.driver)
        homePage.click_sales()
        sleep(1)

   def test_nav_OrderPage(self):
        homePage = HomePage(self.driver)
        homePage.click_order()
        sleep(2)

   def test_newSalesDraftPage(self):
        homePage = HomePage(self.driver)
        homePage.click_draft_order()
        homePage.assert_page("Draft Orders")
        homePage.click_createBTN()

   def test_field_validations(self):
        orderpage = OrderPage(self.driver)
        orderpage.select_order_type()
        orderpage.click_save()
        orderpage.assert_error_nofication("The following fields are invalid:")

   def test_fillOrder(self):
        orderpage = OrderPage(self.driver)
        orderpage.select_order_type()
        sleep(2)
        orderpage.click_agent_dropdown(TestData.Agent)
        orderpage.select_customer(TestData.customer)
        orderpage.click_add_item()
        orderpage.select_product(TestData.product)
        orderpage.click_save()
        sleep(5)

