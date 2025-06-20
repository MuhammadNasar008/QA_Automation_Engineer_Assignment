from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


class ViewsPage(BasePage):
    # Locators
    LISTS_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'Lists')
    GALLERY_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'Gallery')
    PHOTOS_OPTION = (AppiumBy.ACCESSIBILITY_ID, '1. Photos')
    TITLE = (AppiumBy.XPATH, '//*[@text="Views"]')
    TEXT_FIELDS = (AppiumBy.ACCESSIBILITY_ID, 'TextFields')
    WEB_VIEW = (AppiumBy.ACCESSIBILITY_ID, 'WebView')
    BOTTOM_ELEMENT = (AppiumBy.ACCESSIBILITY_ID, 'LastElement')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self):
        assert self.get_text(self.TITLE) == "Views"

    def open_lists(self):
        self.click_element(self.LISTS_OPTION)
        return self

    def open_gallery(self):
        self.click_element(self.GALLERY_OPTION)
        return self

    def open_photos(self):
        self.click_element(self.PHOTOS_OPTION)
        return self

    def count_photos(self):
        photos = self.driver.find_elements(
            AppiumBy.XPATH, '//android.widget.Gallery/android.widget.ImageView')
        return len(photos)

    def scroll_to_bottom(self):
        self.driver.swipe(500, 1800, 500, 200, 1000)
        return True

    def is_bottom_element_visible(self):
        return self.is_displayed(self.BOTTOM_ELEMENT)