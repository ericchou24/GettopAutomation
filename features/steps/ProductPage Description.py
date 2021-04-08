from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from site_page.main_products import ProductPage


DESCRIPTION = (By.XPATH, "//a[@href='#tab-description']")


@given('Open {item} Gettop product page')
def open_item_page(context, item):
    context.app.main_products.open_select_product(item)