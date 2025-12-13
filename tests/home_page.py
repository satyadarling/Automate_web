from selenium.webdriver.common.by import By
from tests.base_page import BasePage

class HomePage(BasePage):
    LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")
    PRODUCT=(By.XPATH,"//a[contains(text(), 'Products')]")
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def search_product(self, product_name):
        self.click(self.PRODUCT)
        self.enter_text(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BTN)

    def logout(self):
        self.click(self.LOGOUT_LINK)