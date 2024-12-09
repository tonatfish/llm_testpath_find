import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import DriverUtils
from helpers import ShellUtils
import time

with open('elements/settings.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_settings(settings_driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.setting_language_setting(settings_driver, language_index)
    settings_driver.save_screenshot(str(tmp_path / "settings_result.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"settings_result.png"), elements["systemControl"])
    # result.save("samples/settings/settings_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/settings_language" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, ])
@pytest.mark.parametrize("restart_time", ["5", "10", "20", "60", ])
def test_alarm_auto_restart(settings_driver: WebDriver, tmp_path: Path, restart_time, language_index: int):
    DriverUtils.setting_language_setting(settings_driver, language_index)

    # slide down slowly for stable test
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements["adjustView"], 3000)

    # set appnea auto restart time
    settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()

    print(restart_time)
    time.sleep(0.5)
    settings_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys(restart_time)
    ShellUtils.tap_element(settings_driver, elements["dialogOK"])
    time.sleep(0.5)
    ShellUtils.tap_element(settings_driver, elements["buttonReturn"])

    time.sleep(1)
    with open('elements/mainwindow.json', 'r') as jsonFile:
        elements_mainwindow = json.load(jsonFile)
    ShellUtils.tap_element(settings_driver, elements_mainwindow["buttonAlarm"])
    time.sleep(1)
    settings_driver.save_screenshot(
        str(tmp_path / "alarm_auto_restart_before.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"alarm_auto_restart_before.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["surfaceView"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/alarm_auto_restart_before_language" + str(language_index) + ".png")
    test_result = ImageUtils.compare_images(
        "samples/settings/alarm_auto_restart_before_language" + str(language_index) + ".png", result, 0.998)

    # wait and test if auto restart
    time.sleep(int(restart_time) + 0.5)
    settings_driver.save_screenshot(
        str(tmp_path / "alarm_auto_restart_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"alarm_auto_restart_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["surfaceView"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/alarm_auto_restart_result_language" + str(language_index) + ".png")
    test_result = test_result and ImageUtils.compare_images(
        "samples/settings/alarm_auto_restart_result_language" + str(language_index) + ".png", result, 0.998)

    # return to setting page
    ShellUtils.tap_element(settings_driver, elements_mainwindow["buttonMenu"])
    time.sleep(0.5)
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(settings_driver, elements_drawer["buttonSettings"])
    time.sleep(0.5)

    assert test_result


@pytest.mark.parametrize("language_index", [1, 2, ])
@pytest.mark.parametrize("screen_time", ["30", "50", "100", "15", ])
def test_screen_time(settings_driver: WebDriver, tmp_path: Path, screen_time, language_index: int):
    DriverUtils.setting_language_setting(settings_driver, language_index)

    # slide down slowly for stable test
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        settings_driver, elements['mainContent'], 2800)

    # set appnea auto restart time
    settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()

    print(screen_time)
    settings_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys(screen_time)
    ShellUtils.tap_element(settings_driver, elements["dialogOK"])
    time.sleep(0.5)
    ShellUtils.tap_element(settings_driver, elements["buttonReturn"])
    time.sleep(2)

    with open('elements/mainwindow.json', 'r') as jsonFile:
        elements_mainwindow = json.load(jsonFile)
    settings_driver.save_screenshot(
        str(tmp_path / ("screen_time_result_" + screen_time + ".png")))
    result = ImageUtils.mask_elements_in_image(str(tmp_path / ("screen_time_result_" + screen_time + ".png")),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/screen_time_result_" + screen_time + "_language" + str(language_index) + ".png")
    test_result = ImageUtils.compare_images(
        "samples/settings/screen_time_result_" + screen_time + "_language" + str(language_index) + ".png", result, 0.998)

    # return to setting page
    ShellUtils.tap_element(settings_driver, elements_mainwindow["buttonMenu"])
    time.sleep(0.5)
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(settings_driver, elements_drawer["buttonSettings"])
    time.sleep(0.5)
    assert test_result
