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


def test_reset_settings(function_settings_driver: WebDriver, tmp_path: Path, encryption_key):
    # set record to a non-default state
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    time.sleep(1)

    function_settings_driver.save_screenshot(
        str(tmp_path / "settings_reset_before.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"settings_reset_before.png"), elements["systemControl"])
    # result.save("samples/settings/settings_reset_before.png")
    assert ImageUtils.compare_images(
        "samples/settings/settings_reset_before.png", result, 0.998)

    # reset settings
    DriverUtils.swipe_element_down(
        function_settings_driver, elements['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements['mainContent'], 200)
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]').click()
    time.sleep(1)
    function_settings_driver.save_screenshot(
        str(tmp_path / "settings_reset_dialog.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"settings_reset_dialog.png"), elements["systemControl"])
    # result.save("samples/settings/settings_reset_dialog.png")
    assert ImageUtils.compare_images(
        "samples/settings/settings_reset_dialog.png", result, 0.998)
    
    ShellUtils.tap_element(function_settings_driver, elements["buttonResetOK"])

    # from initial to setting
    if (int(function_settings_driver.get_performance_data('tw.heroicfaith.fa3', 'batteryinfo')[1][0]) <= 30):
        time.sleep(1)
        with open('elements/mainwindow.json', 'r') as jsonFile:
            elements_mainwindow = json.load(jsonFile)
        ShellUtils.tap_element(
            function_settings_driver, elements_mainwindow['lowBattery_confirm'])

    element: WebElement = function_settings_driver.find_element(
        AppiumBy.ID, "android:id/button2")
    element.click()

    element: WebElement = function_settings_driver.find_element(AppiumBy.ID,
                                                                  "tw.heroicfaith.fa3:id/dialog_input")
    element.clear()
    element.send_keys(encryption_key)
    element: WebElement = function_settings_driver.find_element(AppiumBy.ID,
                                                                "android:id/button1")
    element.click()
    time.sleep(0.5)

    element: WebElement = function_settings_driver.find_element(AppiumBy.ID,
                                                                "tw.heroicfaith.fa3:id/dialog_input")
    element.clear()
    element.send_keys(encryption_key)
    element: WebElement = function_settings_driver.find_element(AppiumBy.ID,
                                                                "android:id/button1")
    element.click()

    DriverUtils.main_to_setting(function_settings_driver)
    time.sleep(0.5)

    function_settings_driver.save_screenshot(
        str(tmp_path / "settings_reset_result.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"settings_reset_result.png"), elements["systemControl"])
    # result.save("samples/settings/settings_reset_result.png")
    assert ImageUtils.compare_images(
        "samples/settings/settings_reset_result.png", result, 0.998)