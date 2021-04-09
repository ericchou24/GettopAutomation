from site_page.main_products import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = ProductPage(self.driver)

