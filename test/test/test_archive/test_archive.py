import pytest
import json
from pathlib import Path
from PIL import Image
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from helpers import ImageUtils
from helpers import ShellUtils
from helpers import DriverUtils
import time

with open('elements/archive.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


def archive_language_setting(driver: WebDriver, language_index: int):
    ShellUtils.tap_element(driver, elements["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements["privateSelect"])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements["buttonReturn"])
    time.sleep(0.5)
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    DriverUtils.main_to_archive(driver)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_archive(function_archive_driver: WebDriver, tmp_path: Path, language_index: int):
    time.sleep(1)
    archive_language_setting(function_archive_driver, language_index)
    ShellUtils.tap_element(function_archive_driver, elements["buttonArchive"])
    time.sleep(1)

    function_archive_driver.save_screenshot(str(tmp_path / "archive_result.png"))
    result = ImageUtils.crop_element_with_path(
        str(tmp_path/"archive_result.png"), elements["archiveSection"])
    # result.save("samples/archive/archive_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/archive/archive_language" + str(language_index) + ".png", result, 0.99)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_archive_before_select(function_archive_driver: WebDriver, tmp_path: Path, language_index: int):
    time.sleep(1)
    archive_language_setting(function_archive_driver, language_index)
    time.sleep(0.5)

    function_archive_driver.save_screenshot(str(tmp_path / "archive_before_select_result.png"))
    result = ImageUtils.crop_element_with_path(
        str(tmp_path/"archive_before_select_result.png"), elements["selectDialog"])
    # result.save("samples/archive/archive_before_select_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/archive/archive_before_select_language" + str(language_index) + ".png", result, 0.99)