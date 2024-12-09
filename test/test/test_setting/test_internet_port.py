import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from helpers import DriverUtils
from helpers import ShellUtils
from helpers import ImageUtils
import time
import os

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)

with open('elements/settings.json', 'r') as jsonFile:
    elements_setting = json.load(jsonFile)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_internet_port_on_off(function_settings_driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.setting_language_setting(function_settings_driver, language_index)

    # turn on internet port
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
    time.sleep(1)
    ShellUtils.tap_element(function_settings_driver, elements_setting["buttonReturn"])

    time.sleep(1)
    function_settings_driver.save_screenshot(str(tmp_path/"buttonInternet_on_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonInternet_on_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/buttonInternet_on_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/buttonInternet_on_language_" + str(language_index) + ".png", result, 0.998)
    
    # turn off internet port
    time.sleep(1)
    DriverUtils.main_to_setting(function_settings_driver)

    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
    time.sleep(1)
    ShellUtils.tap_element(function_settings_driver, elements_setting["buttonReturn"])

    time.sleep(1)
    function_settings_driver.save_screenshot(str(tmp_path/"buttonInternet_off_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonInternet_off_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/buttonInternet_off_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/buttonInternet_off_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_internet_port_link(function_settings_driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.setting_language_setting(function_settings_driver, language_index)

    # turn on internet port
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(0.5)
    DriverUtils.swipe_element_down(
        function_settings_driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
    
    # set internet ip
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    internet_ip = '35.229.144.42'
    function_settings_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys(internet_ip)
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.ID, "android:id/button1").click()
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()
    time.sleep(1)
    api_token = '' # please contact to get api token
    function_settings_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys(api_token)
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.ID, "android:id/button1").click()
    time.sleep(1)
    ShellUtils.tap_element(function_settings_driver, elements_setting["buttonReturn"])

    # start record & wait 10 seconds for internet link
    time.sleep(1)
    ShellUtils.tap_element(function_settings_driver, elements_mainwindow["buttonRtInfer"])
    time.sleep(10)
    function_settings_driver.save_screenshot(str(tmp_path/"buttonInternet_link_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonInternet_link_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["surfaceView"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/buttonInternet_link_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/buttonInternet_link_language_" + str(language_index) + ".png", result, 0.998)
