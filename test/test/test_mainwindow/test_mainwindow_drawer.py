import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from helpers import ImageUtils
from helpers import DriverUtils
from helpers import ShellUtils
import time

with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


with open('elements/mainwindow.json', 'r') as jsonFile:
        elements_mainwindow = json.load(jsonFile)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_drawer(drawer_driver: WebDriver, tmp_path: Path, language_index: int):
    ShellUtils.tap_element(drawer_driver, elements["surfaceView"])
    time.sleep(1)

    DriverUtils.change_language_from_main_to_main(drawer_driver, language_index)

    ShellUtils.tap_element(drawer_driver, elements_mainwindow["buttonMenu"])
    time.sleep(1)

    drawer_driver.save_screenshot(str(tmp_path / "drawer_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"drawer_result.png"),
                                               elements["tvDateTime"], elements["textViewBat"], elements["imageBattery"], elements["surfaceView"])
    # result.save("samples/mainwindow_drawer/drawer_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow_drawer/drawer_language_" + str(language_index) + ".png", result, 0.998)
