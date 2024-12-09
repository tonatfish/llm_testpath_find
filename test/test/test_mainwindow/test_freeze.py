from appium.webdriver.extensions.android.power import Power
from appium.webdriver.webelement import WebElement
import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import ShellUtils
from helpers import DriverUtils
import time

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements = json.load(jsonFile)

@pytest.mark.parametrize("language_index", [1, 2, ])
def test_buttonFreeze(function_driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(function_driver, language_index)

    ShellUtils.tap_element(function_driver, elements["buttonFreeze"])
    time.sleep(0.5)
    function_driver.save_screenshot(str(tmp_path/"buttonFreeze_freeze_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonFreeze_freeze_result.png"),
                                               elements["tvDateTime"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonFreeze_freeze_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonFreeze_freeze_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(function_driver, elements["buttonFreeze"])
    time.sleep(0.5)
    function_driver.save_screenshot(str(tmp_path/"buttonFreeze_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonFreeze_normal_result.png"),
                                               elements["tvDateTime"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonFreeze_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonFreeze_normal_language_" + str(language_index) + ".png", result, 0.998)
