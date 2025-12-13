import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, value):
        self.driver.find_element(*by_locator).clear()
        self.driver.find_element(*by_locator).send_keys(value)

    def get_text(self, by_locator):
        return self.driver.find_element(*by_locator).text

    def is_displayed(self, by_locator):
        return self.driver.find_element(*by_locator).is_displayed()
    def select_val(self,by_locator,value):
        element=Select(self.driver.find_element(*by_locator))
        element.select_by_value(value)
    def get_text_val(self, by_locator):
        try:
            error = self.driver.find_element(*by_locator).text
            return False
        except:
            return True
    def move_to_ele(self,by_locator):
        time.sleep(10)
        action = ActionChains(self.driver)

        # Wait until element is visible and ready
        ele = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )

        # Hover over the element
        action.move_to_element(ele).click().perform()


