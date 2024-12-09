import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from helpers import DriverUtils
from helpers import ShellUtils
from helpers import ImageUtils
import time


with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)

with open('elements/settings.json', 'r') as jsonFile:
    elements_setting = json.load(jsonFile)


# 'RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01',
@pytest.mark.parametrize("audioName", ['apnea_audio01', ])
def test_record_freeze(function_record_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str):
    # to setting & swipe down
    DriverUtils.main_to_setting(function_record_driver)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    time.sleep(0.5)

    # set appnea white time to avoid freeze white border
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]').click()
    time.sleep(0.5)

    function_record_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys("20")
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["dialogOK"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["buttonReturn"])
    time.sleep(0.5)

    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonMenu"])
    time.sleep(0.5)

    DriverUtils.load_audio(function_record_driver,
                           "audios/" + audioName + ".wav", 6)
    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonFreeze"])
    time.sleep(11)

    function_record_driver.save_screenshot(
        str(tmp_path / "buttonFreeze_record_before_result.png"))
    time.sleep(1)
    function_record_driver.save_screenshot(
        str(tmp_path / "buttonFreeze_record_after_result.png"))

    result_before = ImageUtils.mask_elements_in_image(str(tmp_path / "buttonFreeze_record_before_result.png"),
                                                      elements_mainwindow["tvAppTitle"], elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"], elements_mainwindow["viewRrInfo"], elements_mainwindow["offsetTextLine"])
    # result_before.save(tmp_path / "buttonFreeze_record_before_result.png")

    result_after = ImageUtils.mask_elements_in_image(str(tmp_path / "buttonFreeze_record_after_result.png"),
                                                     elements_mainwindow["tvAppTitle"], elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"], elements_mainwindow["viewRrInfo"], elements_mainwindow["offsetTextLine"])
    # result_after.save(tmp_path / "buttonFreeze_record_after_result.png")
    assert ImageUtils.compare_images_from_image(
        result_before, result_after, 0.998)
