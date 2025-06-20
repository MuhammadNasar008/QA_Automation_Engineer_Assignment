from appium.webdriver.common.appiumby import AppiumBy

from .accessibility_page import AccessibilityPage
from .base_page import BasePage
from .preferences_page import PreferencesPage
from .views_page import ViewsPage


class MainPage(BasePage):
    # Locators
    VIEWS_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'Views')
    PREFERENCES_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'Preference')
    ACCESSIBILITY_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'Accessibility')

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_views(self):
        self.click_element(self.VIEWS_OPTION)
        return ViewsPage(self.driver)

    def navigate_to_preferences(self):
        self.click_element(self.PREFERENCES_OPTION)
        return PreferencesPage(self.driver)

    def navigate_to_accessibility(self):
        self.click_element(self.ACCESSIBILITY_OPTION)
        return AccessibilityPage(self.driver)

    def navigate_back(self):
        """Navigate back to the previous screen"""
        self.driver.back()