from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    username_id = (By.ID, "login")
    password_id = (By.ID,"password")
    login_btn = (By.XPATH,"//*[contains(@type,'submit')]")
    user_dropdown =(By.XPATH, "//span[contains(text(),'test')]")
    log_outBTN =(By.XPATH, "//*[contains(text(),'Log out')]")
    error_message = (By.XPATH, "//p[contains(text(),'Wrong login/password')]")

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password):
        self.do_send_keys(self.username_id,username)
        self.do_send_keys(self.password_id, password)
        self.do_click(self.login_btn)
    
    def log_out(self):
        self.do_click(self.user_dropdown)
        self.do_click(self.log_outBTN)
    
    def assert_correct_error(self, element_name):
        self.get_element_text(self.error_message, element_name)