from selenium.webdriver.common.by import By
from tests.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    ERROR_TEXT=(By.XPATH,"//*[contains(text(),'Your email or password is incorrect!')]")

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self.get_text_val(self.ERROR_TEXT)