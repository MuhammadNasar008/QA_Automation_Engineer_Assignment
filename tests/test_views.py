import pytest
from pages.main_page import MainPage


class TestViews:
    def test_navigate_to_views(self, driver):
        """
        Test to navigate to the Views page and verify that the page has loaded.
        """
        main_page = MainPage(driver)
        views_page = main_page.navigate_to_views()
        main_page.navigate_back()
        views_page.verify_page_loaded()

    def test_gallery_functionality(self, driver):
        """
        Test to verify the gallery functionality by opening the gallery,
        accessing the photos, and asserting that there are photos present.
        """
        main_page = MainPage(driver)
        views_page = main_page.navigate_to_views()
        views_page.open_gallery().open_photos()
        assert views_page.count_photos() > 0, "No photos found in gallery"

    def test_scroll_visibility(self, driver):
        """
        Test to verify the scroll functionality and ensure that the element
        at the bottom of the page becomes visible after scrolling.
        """
        main_page = MainPage(driver)
        views_page = main_page.navigate_to_views()

        assert views_page.scroll_to_bottom(), "Scroll to bottom failed"
        assert views_page.is_bottom_element_visible(), "Bottom element is not visible after scrolling"
