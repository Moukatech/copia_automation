from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):
    sales_link = (By.XPATH, "//div[contains(text(),'Sales')]")
    order_link = (By.XPATH, "/html/body/nav/div/ul[1]/li[1]/a")
    draft_order = (By.XPATH, "//span[contains(text(),'Draft Orders')]")
    draftPage = (By.XPATH, "//li[contains(text(),'Draft Orders')]")
    create_BTN= (By.XPATH, "//button[contains(text(),'Create')]")
    order_type_dropdown =(By.NAME, "order_type_id")
    select_Normal_order = (By.XPATH, " //*[@name='order_type_id']/option[contains(text(),'Normal Order')]")


    def __init__(self, driver):
        super().__init__(driver)

    def click_sales(self):
        self.do_click(self.sales_link)

    def click_order(self):
        self.do_click(self.order_link)

    def click_draft_order(self):
        self.do_click(self.draft_order)

    def click_createBTN(self):
        self.do_click(self.create_BTN)

    def click_order_type(self):
        self.do_click(self.order_type_dropdown)
    
    def assert_page(self, element_name):
        self.get_element_text(self.draftPage, element_name)



