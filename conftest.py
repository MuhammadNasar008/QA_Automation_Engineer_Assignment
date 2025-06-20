import pytest
import os
import shutil
from datetime import datetime


# Clear old reports before test session starts
@pytest.fixture(scope="session", autouse=True)
def cleanup_reports():
    """Clears previous test artifacts before all tests run"""
    folders = ['screenshots', 'logs']
    for folder in folders:
        try:
            if os.path.exists(folder):
                shutil.rmtree(folder)
            os.makedirs(folder)
        except Exception as e:
            print(f"⚠️ Couldn't clear {folder}: {e}")


# Main test setup
@pytest.fixture
def driver(request):
    """Starts fresh app session before each test"""
    from utils.driver_setup import create_driver
    driver = None

    try:
        # Start new session
        driver = create_driver()

        # Make driver available for screenshots
        request.node.driver = driver

        yield driver

    finally:
        # Capture screenshot if test failed
        if driver and hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = request.node.name.replace(":", "_")
            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")

        # Quit driver after test
        if driver:
            driver.quit()


# Test result tracking
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    item.rep_call = outcome.get_result()