# utils/driver_setup.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import pytest
from datetime import datetime


def create_driver():
    """Creates and configures the Appium driver"""
    options = UiAutomator2Options()

    # Required capabilities
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = 'emulator-5554'  # Update with your device/emulator
    options.app = os.path.join(os.getcwd(), 'drivers', 'ApiDemos-debug.apk')

    # Performance optimizations
    options.new_command_timeout = 300
    options.set_capability('autoGrantPermissions', True)
    options.set_capability('unicodeKeyboard', True)
    options.set_capability('resetKeyboard', True)

    # Initialize driver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    return driver


@pytest.fixture(scope="function")
def appium_driver():
    """Pytest fixture that handles driver lifecycle"""
    driver = None
    try:
        driver = create_driver()
        yield driver
    finally:
        if driver:
            # Capture screenshot on failure
            if hasattr(pytest, 'test_failed') and pytest.test_failed:
                take_screenshot(driver, pytest.current_test_name)
            driver.quit()


def take_screenshot(driver, test_name):
    """Helper function to capture screenshots"""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(
        screenshot_dir,
        f"{test_name}_{timestamp}.png"
    )
    driver.save_screenshot(screenshot_path)
    return screenshot_path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture test status"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Store test name and failure status for screenshot handling
        pytest.current_test_name = item.nodeid.split('::')[-1]
        pytest.test_failed = report.failed