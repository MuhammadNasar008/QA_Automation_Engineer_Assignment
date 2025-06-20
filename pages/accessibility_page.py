from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


class AccessibilityPage(BasePage):
    # Locators
    NODE_PROVIDER = (AppiumBy.ACCESSIBILITY_ID, 'Accessibility Node Provider')
    CUSTOM_VIEW = (AppiumBy.ACCESSIBILITY_ID, 'Custom View')
    TITLE = (AppiumBy.XPATH, '//*[@text="Accessibility"]')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self):
        assert self.get_text(self.TITLE) == "Accessibility"

    def open_node_provider(self):
        self.click_element(self.NODE_PROVIDER)
        return self

    def open_custom_view(self):
        self.click_element(self.CUSTOM_VIEW)
        return self

    def verify_custom_view_elements(self):
        assert self.find_element((AppiumBy.XPATH, '(//android.view.View[@text="Off"])[1]'))
        assert self.find_element((AppiumBy.XPATH, '(//android.view.View[@text="Off"])[2]'))
        return True