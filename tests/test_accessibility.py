import pytest
from pages.main_page import MainPage


class TestAccessibility:
    def test_accessibility_navigation(self, driver):
        """
        Test to navigate to the Accessibility page and verify that the page has loaded correctly.
        """
        main_page = MainPage(driver)
        access_page = main_page.navigate_to_accessibility()
        main_page.navigate_back()
        access_page.verify_page_loaded()

    def test_custom_view(self, driver):
        """
        Test to open a custom view in the Accessibility page and verify
        that the expected custom view elements are present.
        """
        main_page = MainPage(driver)
        access_page = main_page.navigate_to_accessibility()
        access_page.open_custom_view()
        assert access_page.verify_custom_view_elements(), "Custom view elements verification failed"
