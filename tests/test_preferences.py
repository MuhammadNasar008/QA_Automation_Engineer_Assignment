import pytest
from pages.main_page import MainPage


class TestPreferences:
    def test_wifi_preferences(self, driver):
        """
        Test to navigate to the Preferences page, open Preference dependencies,
        toggle the WiFi checkbox, and verify that it is enabled.
        """
        main_page = MainPage(driver)
        pref_page = main_page.navigate_to_preferences()
        pref_page.open_preference_dependencies()
        new_state = pref_page.toggle_wifi_checkbox()
        assert new_state is True, "WiFi checkbox is not enabled after toggling"

    def test_wifi_settings(self, driver):
        """
        Test to verify that the WiFi settings allow setting a new SSID.
        """
        test_ssid = "TestWiFiNetwork"
        main_page = MainPage(driver)
        pref_page = main_page.navigate_to_preferences()
        pref_page.open_preference_dependencies() \
            .open_wifi_settings() \
            .set_wifi_name(test_ssid)

        assert pref_page.get_wifi_name() == test_ssid, "WiFi SSID does not match the expected value"
