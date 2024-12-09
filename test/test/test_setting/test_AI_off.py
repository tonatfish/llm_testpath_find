import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from helpers import DriverUtils
from helpers import ShellUtils
import time
import os


with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)


@pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
def test_AI_off(function_record_no_ai_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str):
    # mainwindow to drawer
    ShellUtils.tap_element(function_record_no_ai_driver,
                           elements_mainwindow["buttonMenu"])

    DriverUtils.load_audio(function_record_no_ai_driver,
                           "audios/" + audioName + ".wav", 33)
    DriverUtils.main_to_archive_private(function_record_no_ai_driver)

    # get file
    date = function_record_no_ai_driver.find_element(AppiumBy.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text

    listFilename = ShellUtils.listFile(
        function_record_no_ai_driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/')
    targetFilename = listFilename.replace('\r', '').split('\n')[0]
    targetZipPath = '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/'
    zipFile_base64 = DriverUtils.pull_file(
        function_record_no_ai_driver, targetZipPath, targetFilename)
    local_zip_path = os.path.join(tmp_path / targetFilename)
    local_file_path = os.path.join(tmp_path)

    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, encryption_key)

    assert (len(unzip_result) == 0)

    # check filenames with no rr file
    for file_path in os.listdir(local_file_path):
        if file_path.endswith('RR.txt'):
            assert False

    assert True
