from selenium.webdriver.common.by import By
from tests.base_page import BasePage
class CartPage(BasePage):
    CHECKOUT_BTN = (By.CLASS_NAME, "check_out")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)