from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


class PreferencesPage(BasePage):
    # Locators
    PREF_DEPENDENCIES = (AppiumBy.ACCESSIBILITY_ID, '3. Preference dependencies')
    WIFI_CHECKBOX = (AppiumBy.ID, 'android:id/checkbox')
    WIFI_SETTINGS = (AppiumBy.XPATH, '//*[@text="WiFi settings"]')
    WIFI_INPUT = (AppiumBy.ID, 'android:id/edit')
    OK_BUTTON = (AppiumBy.ID, 'android:id/button1')
    TITLE = (AppiumBy.XPATH, '//*[@text="Preference"]')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self):
        assert self.get_text(self.TITLE) == "Preference"

    def open_preference_dependencies(self):
        self.click_element(self.PREF_DEPENDENCIES)
        return self

    def toggle_wifi_checkbox(self):
        checkbox = self.find_element(self.WIFI_CHECKBOX)
        initial_state = checkbox.get_attribute('checked') == 'true'
        checkbox.click()
        return not initial_state

    def open_wifi_settings(self):
        self.click_element(self.WIFI_SETTINGS)
        return self

    def set_wifi_name(self, name):
        self.send_keys(self.WIFI_INPUT, name)
        self.click_element(self.OK_BUTTON)
        return self

    def get_wifi_name(self):
        self.click_element(self.WIFI_SETTINGS)
        name = self.get_text(self.WIFI_INPUT)
        self.click_element(self.OK_BUTTON)
        return name