import pytest
import json
from pathlib import Path
from PIL import Image
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from helpers import ImageUtils
from helpers import ShellUtils
from helpers import DriverUtils
from helpers import LlmUtils
import time

with open('elements/about.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


def about_language_setting(driver: WebDriver, language_index: int):
    ShellUtils.tap_element(driver, elements["buttonReturn"])
    time.sleep(1)
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    DriverUtils.main_to_about(driver)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_about(about_driver: WebDriver, tmp_path: Path, language_index: int):
    about_language_setting(about_driver, language_index)

    about_driver.save_screenshot(str(tmp_path / "about_result.png"))

    # result = Image.open(str(tmp_path / "about_result.png")).convert('RGB')
    # result.save("samples/about/about_language" + str(language_index) + ".png")

    assert ImageUtils.compare_images_from_file("samples/about/about_language" + str(language_index) + ".png", str(tmp_path / "about_result.png"), 0.998)


@pytest.mark.parametrize("language_index", [1, ])
def test_buttonPolicy(about_driver: WebDriver, tmp_path: Path, language_index: int):
    expected = True
    about_language_setting(about_driver, language_index)

    ShellUtils.tap_element(about_driver, elements["buttonPolicy"])
    time.sleep(1)
    about_driver.save_screenshot(
        str(tmp_path/"buttonPolicy_unscrolled_result.png"))

    # result = Image.open(str(tmp_path / "buttonPolicy_unscrolled_result.png")).convert('RGB')
    # result.save("samples/about/buttonPolicy_unscrolled_language" + str(language_index) + ".png")

    expected = expected and ImageUtils.compare_images_from_file(
        "samples/about/buttonPolicy_unscrolled_language" + str(language_index) + ".png", str(tmp_path / "buttonPolicy_unscrolled_result.png"), 0.998)

    LlmUtils.scroll_until_exist("Disclaimer", about_driver, tmp_path, elements["textMessage"])
    
    LlmUtils.scroll_until_exist("Personal Information", about_driver, tmp_path, elements["textMessage"])
    
    about_driver.save_screenshot(
        str(tmp_path/"buttonPolicy_scrolled_result.png"))
    
    # result = Image.open(str(tmp_path / "buttonPolicy_scrolled_result.png")).convert('RGB')
    # result.save("samples/about/buttonPolicy_scrolled_language" + str(language_index) + ".png")

    expected = expected and ImageUtils.compare_images_from_file(
        "samples/about/buttonPolicy_scrolled_language" + str(language_index) + ".png", str(tmp_path/"buttonPolicy_scrolled_result.png"), 0.998)

    ShellUtils.tap_element(about_driver, elements["btnMessageOK"])
    time.sleep(1)
    about_driver.save_screenshot(
        str(tmp_path/"buttonPolicy_normal_result.png"))
    
    # result = Image.open(str(tmp_path / "buttonPolicy_normal_result.png")).convert('RGB')
    # result.save("samples/about/buttonPolicy_normal_language" + str(language_index) + ".png")

    expected = expected and ImageUtils.compare_images_from_file(
        "samples/about/buttonPolicy_normal_language" + str(language_index) + ".png", str(tmp_path/"buttonPolicy_normal_result.png"), 0.998)
    
    assert expected


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_buttonUseTerm(about_driver: WebDriver, tmp_path: Path, language_index: int):
    expected = True
    about_language_setting(about_driver, language_index)

    ShellUtils.tap_element(about_driver, elements["buttonUseTerm"])
    time.sleep(1)
    about_driver.save_screenshot(
        str(tmp_path/"buttonUseTerm_unscrolled_result.png"))
    
    # result = Image.open(str(tmp_path / "buttonUseTerm_unscrolled_result.png")).convert('RGB')
    # result.save("samples/about/buttonUseTerm_unscrolled_language" + str(language_index) + ".png")

    expected = expected and ImageUtils.compare_images_from_file(
        "samples/about/buttonUseTerm_unscrolled_language" + str(language_index) + ".png", str(tmp_path / "buttonUseTerm_unscrolled_result.png"), 0.998)

    DriverUtils.swipe_element_down(about_driver, elements["textMessage"], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(about_driver, elements["textMessage"], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(about_driver, elements["textMessage"], 200)
    time.sleep(1)
    about_driver.save_screenshot(
        str(tmp_path/"buttonUseTerm_scrolled_result.png"))
    
    # result = Image.open(str(tmp_path / "buttonUseTerm_scrolled_result.png")).convert('RGB')
    # result.save("samples/about/buttonUseTerm_scrolled_language" + str(language_index) + ".png")
    
    expected = expected and ImageUtils.compare_images_from_file(
        "samples/about/buttonUseTerm_scrolled_language" + str(language_index) + ".png", str(tmp_path/"buttonUseTerm_scrolled_result.png"), 0.998)

    ShellUtils.tap_element(about_driver, elements["btnMessageOK"])
    time.sleep(1)
    about_driver.save_screenshot(
        str(tmp_path/"buttonUseTerm_normal_result.png"))
    
    # result = Image.open(str(tmp_path / "buttonUseTerm_normal_result.png")).convert('RGB')
    # result.save("samples/about/buttonUseTerm_normal_language" + str(language_index) + ".png")

    expected = expected and ImageUtils.compare_images_from_file(
        "samples/about/buttonUseTerm_normal_language" + str(language_index) + ".png", str(tmp_path/"buttonUseTerm_normal_result.png"), 0.998)

    assert expected
