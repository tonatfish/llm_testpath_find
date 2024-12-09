import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ShellUtils
from helpers import TextUtils
import time

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


def test_doPermission(base_driver: WebDriver, tmp_path: Path):
    element: WebElement = base_driver.find_element(AppiumBy.ID,
        "android:id/button1")
    element.click()
    time.sleep(5)
    assert TextUtils.compare_driverPackage(
        base_driver.current_package, "com.android.settings")
