import time

from selenium.webdriver.common.by import By
from tests.base_page import BasePage

class ProductPage(BasePage):
    FIRST_PRODUCT_ADD = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    ADD_CART=(By.XPATH,"(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[4]")
    CONTINUE_BTN = (By.XPATH, "//button[text()='Continue Shopping']")
    VIEW_CART = (By.XPATH, "//a[@href='/view_cart']")

    def add_first_product_to_cart(self):
        self.move_to_ele(self.FIRST_PRODUCT_ADD)
        time.sleep(10)
        #self.click(self.ADD_CART)
        self.click(self.CONTINUE_BTN)
        self.click(self.VIEW_CART)

