from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            logging.error(f"Element not found: {locator}")
            raise e

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(f"screenshots/{filename}.png")