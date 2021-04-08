from time import sleep
from selenium.webdriver.common.by import By
from site_page.base_page import Page
from selenium.webdriver.support.ui import Select

class ProductPage(Page):

    def open_select_product(self, alias):
        self.open_url('https://gettop.us/product/' + alias)

##m = Page
##m.click()