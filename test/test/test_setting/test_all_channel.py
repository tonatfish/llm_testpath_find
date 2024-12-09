import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import DriverUtils
from helpers import ShellUtils
import time
import os


with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)


with open('elements/settings.json', 'r') as jsonFile:
    elements_setting = json.load(jsonFile)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_all_channel(function_record_all_channel_driver: WebDriver, encryption_key: str, tmp_path: Path, language_index: int):
    DriverUtils.setting_language_setting(function_record_all_channel_driver, language_index)

    ShellUtils.tap_element(function_record_all_channel_driver, elements_setting["buttonReturn"])
    time.sleep(1)

    function_record_all_channel_driver.save_screenshot(
        str(tmp_path/"all_channel_mainwindow_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"all_channel_mainwindow_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/all_channel_mainwindow_result_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/all_channel_mainwindow_result_language" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel"])
    time.sleep(1)
    function_record_all_channel_driver.save_screenshot(
        str(tmp_path/"all_channel_spinner_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"all_channel_spinner_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/all_channel_spinner_result_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/all_channel_spinner_result_language" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel_ch4"])
    time.sleep(1)
    function_record_all_channel_driver.save_screenshot(
        str(tmp_path/"all_channel_spinner_ch4_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"all_channel_spinner_ch4_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/all_channel_spinner_ch4_result_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/all_channel_spinner_ch4_result_language" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel_ch3"])
    time.sleep(1)
    function_record_all_channel_driver.save_screenshot(
        str(tmp_path/"all_channel_spinner_ch3_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"all_channel_spinner_ch3_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/all_channel_spinner_ch3_result_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/all_channel_spinner_ch3_result_language" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel_ch2"])
    time.sleep(1)
    function_record_all_channel_driver.save_screenshot(
        str(tmp_path/"all_channel_spinner_ch2_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"all_channel_spinner_ch2_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/all_channel_spinner_ch2_result_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/all_channel_spinner_ch3_result_language" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["spinnerChannel_ch1"])
    time.sleep(1)
    function_record_all_channel_driver.save_screenshot(
        str(tmp_path/"all_channel_spinner_ch1_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"all_channel_spinner_ch1_result.png"),
                                               elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
    # result.save("samples/settings/all_channel_spinner_ch1_result_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/settings/all_channel_spinner_ch1_result_language" + str(language_index) + ".png", result, 0.998)

    time.sleep(3)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["buttonRtInfer"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["buttonSkipKeyIn"])
    time.sleep(15)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["buttonRtInfer"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_all_channel_driver,
                           elements_mainwindow["buttonRecordSaving"])

    time.sleep(2)
    DriverUtils.main_to_archive_private(function_record_all_channel_driver)

    # get file
    date = function_record_all_channel_driver.find_element(AppiumBy.XPATH,
                                                           '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text

    listFilename = ShellUtils.listFile(
        function_record_all_channel_driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/')
    targetFilename = listFilename.replace('\r', '').split('\n')[0]
    targetZipPath = '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/'
    zipFile_base64 = DriverUtils.pull_file(
        function_record_all_channel_driver, targetZipPath, targetFilename)
    local_zip_path = os.path.join(tmp_path / targetFilename)
    local_file_path = os.path.join(tmp_path)

    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, encryption_key)

    assert (len(unzip_result) == 0)

    # check file list
    # NOTICE: since no relay board connection, it's same with original file list
    RR_exist = False
    AI_exist = False
    json_exist = False
    wav_exist = False
    notify_exist = False
    checksum_exist = False
    for file_path in os.listdir(local_file_path):
        if file_path.endswith('RR.txt'):
            RR_exist = True
        elif file_path.endswith('AI.txt'):
            AI_exist = True
        elif file_path.endswith('.wav'):
            wav_exist = True
        elif file_path.endswith('.json'):
            json_exist = True
        elif file_path.endswith('Notify.txt'):
            notify_exist = True
        elif file_path.endswith('checksum.txt'):
            checksum_exist = True

    assert RR_exist
    assert AI_exist
    assert json_exist
    assert wav_exist
    assert notify_exist
    assert checksum_exist
