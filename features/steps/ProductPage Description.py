from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
##from site_page.main_products import ProductPage


DESCRIPTION = (By.XPATH, "//a[@href='#tab-description']")


@given('Open {item} Gettop product page')
def open_item_page(context, item):
    context.app.main_page.open_select_product(item)

@then('Verify description is available')
def verify_description_tab(context):
    context.app.main_page.verify_description_tab(DESCRIPTION)
    ##tab = context.driver.find_element(DESCRIPTION)
    ##print(tab)
    ##context.app.main_page.