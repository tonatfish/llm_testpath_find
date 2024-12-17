import pytest
import json
from pathlib import Path
from PIL import Image
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
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
    # about_language_setting(about_driver, language_index)

    ShellUtils.tap_element(about_driver, elements["buttonPolicy"])
    time.sleep(1)
    about_driver.save_screenshot(
        str(tmp_path/"buttonPolicy_unscrolled_result.png"))

    # result = Image.open(str(tmp_path / "buttonPolicy_unscrolled_result.png")).convert('RGB')
    # result.save("samples/about/buttonPolicy_unscrolled_language" + str(language_index) + ".png")
    
    about_driver.save_screenshot(
        str(tmp_path/"buttonPolicy_0.png"))
    result = Image.open(str(tmp_path / "buttonPolicy_0.png")).convert('RGB')
    result.save("tmp/buttonPolicy_0.png")
    action = TouchAction(about_driver)
    element = elements["textMessage"]
    swipe_x = element["x"] + element["width"] / 2 + 1
    swipe_start_y = element["y"] + element["height"] - 1
    swipe_end_y = element["y"] + 1

    start_time = time.time()

    for i in range(1, 7):
        # # original swipe with inertia (1.6sec):
        # DriverUtils.swipe_element_down(about_driver, elements["textMessage"], 200)
        # # swipe with little inertia (1.1sec):
        # touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        # actions = ActionChains(about_driver)
        # actions.w3c_actions = ActionBuilder(about_driver, mouse=touch_input)
        # actions.w3c_actions.pointer_action.move_to_location(swipe_x, swipe_start_y)
        # actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions = ActionBuilder(about_driver, mouse=touch_input, duration=200)
        # actions.w3c_actions.pointer_action.move_to_location(swipe_x, swipe_end_y)
        # actions.w3c_actions.pointer_action.release()
        # actions.w3c_actions.pointer_action.click_and_hold()
        # actions.perform()
        # swipe with no inertia (fully stable) (3 sec):
        action.press(x=swipe_x, y=swipe_start_y).move_to(x=swipe_x, y=swipe_end_y).release().perform()
        about_driver.save_screenshot(
            str(tmp_path/("buttonPolicy_" + str(i) + ".png")))
        result = Image.open(str(tmp_path / ("buttonPolicy_" + str(i) + ".png"))).convert('RGB')
        result.save("tmp/buttonPolicy_" + str(i) + ".png")
        print("--- %s seconds ---" % (time.time() - start_time))

    time.sleep(3)

    assert False

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
