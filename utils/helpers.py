from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

def swipe(driver, start_x, start_y, end_x, end_y, duration=800):
    """Perform swipe action using ActionChains"""
    action = ActionChains(driver)
    # Start the swipe action at the initial point (press)
    action.move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x - start_x, end_y - start_y).release().perform()

def scroll_to_text(driver, text, max_swipes=5):
    """Scroll to element with specific text"""
    for _ in range(max_swipes):
        try:
            # Attempt to find the element using Android's UIAutomator
            return driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))')
        except:
            # Perform a swipe if the element is not found
            size = driver.get_window_size()
            swipe(driver,
                 size['width']/2, size['height']*0.8,
                 size['width']/2, size['height']*0.2)
    raise Exception(f"Element with text '{text}' not found after {max_swipes} swipes")
