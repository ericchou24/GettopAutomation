from time import sleep
from selenium.webdriver.common.by import By
from site_page.base_page import Page
from selenium.webdriver.support.ui import Select

class ProductPage(Page):

    DESCRIPTION = (By.XPATH, "//a[@href='#tab-description']")

    def open_select_product(self, alias):
        self.open_url('https://gettop.us/product/' + alias)

    def verify_description_tab(self, description):
        locator = self.driver.find_elements(*self.DESCRIPTION)
        assert len(locator) == 1, f'Could not find the Description tab element'
##        print(type(locator))
##        assert locator.size() != 0
