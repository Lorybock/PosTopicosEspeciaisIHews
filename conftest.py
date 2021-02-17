import pytest
from appium import webdriver

@pytest.fixture(scope='class')
def setup():
    desire_caps  = {
        "platformName":"Android",
        "deviceName":"emulator-5554",
        "app":"/Users/Lory1/Downloads/Hews_for_Hacker_News.apk",
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
    yield driver
    driver.quit()