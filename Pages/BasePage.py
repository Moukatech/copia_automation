from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        # self.driver.find_element(by_locator).click()
        ele=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", ele)

    def do_send_keys(self, by_locator, text):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ele.clear()
        ele.send_keys(text)

    def return_keys(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ele.send_keys(Keys.TAB)

    def get_element_text(self, by_locator, text):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        print (ele)
        assert text == ele

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(ele)
    
    def select_element(self,by_locator,text):
        select=Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        select.select_by_value(text)