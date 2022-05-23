from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class OrderPage(BasePage):
    order_type_dropdown =(By.XPATH, "//*/select[@name='order_type_id']")
    agent_dropdown_txt = (By.XPATH, "//*/div[@name='partner_id']//*[@class='o_input ui-autocomplete-input']")
    customer_dropdown_txt = (By.XPATH, "//*/div[@name='customer_id']//*[@class='o_input ui-autocomplete-input']")
    product_dropdown_txt = (By.XPATH, "//*/div[@name='product_id']//*[@class='o_input ui-autocomplete-input']")
    invoive_dropdown_txt = (By.XPATH, "//*/div[@name='partner_invoice_id']//*[@class='o_input ui-autocomplete-input']")
    delivery_Address_txt = (By.XPATH, "//*/div[@name='partner_shipping_id']//*[@class='o_input ui-autocomplete-input']")
    pricelist_dropdown_txt = (By.XPATH, "//*/div[@name='pricelist_id']//*[@class='o_input ui-autocomplete-input']")
    add_item = (By.XPATH, "//*[@class='tab-pane active']//a[contains(text(),'Add an item')]")
    save_button = (By.XPATH, "//button[contains(text(),'Save')]")
    error_notification = (By.XPATH, "//*[@class='o_notification_title']")


    def __init__(self, driver):
        super().__init__(driver)
    
    def click_order_dropdown(self):
         self.do_click(self.order_type_dropdown)
    
    def assert_error_nofication(self, error_message):
        self.get_element_text(self.error_notification,error_message)

    def select_order_type(self):
        self.select_element(self.order_type_dropdown, "7")
    
    def click_agent_dropdown(self, agent):
        self.do_send_keys(self.agent_dropdown_txt, agent)
        sleep(2)
        self.return_keys(self.agent_dropdown_txt)

    def select_customer(self,customer):
         self.do_send_keys(self.customer_dropdown_txt,customer)
         sleep(2)
         self.return_keys(self.customer_dropdown_txt)
         
    def select_invoice_address(self,invoice):
         self.do_send_keys(self.invoive_dropdown_txt,invoice)
    
    def select_delivery_address(self,delivery):
         self.do_send_keys(self.delivery_Address_txt,delivery)
    
    def select_priceList(self,pricelist):
         self.do_send_keys(self.pricelist_dropdown_txt,pricelist)

    def click_add_item(self):
        self.do_click(self.add_item)

    def select_product(self,product):
         self.do_send_keys(self.product_dropdown_txt,product)
         sleep(2)
         self.return_keys(self.product_dropdown_txt)
    
    def click_save(self):
        self.do_click(self.save_button)

