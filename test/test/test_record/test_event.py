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


@pytest.mark.parametrize("language_index", [1, 2, ])
@pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
def test_event(function_record_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str, language_index: int):
    DriverUtils.change_language_from_main_to_main(function_record_driver, language_index)

    # add event at 0 sec
    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonEvent"])
    time.sleep(0.5)

    # check all event
    for i in range(6):
        function_record_driver.find_element(
            AppiumBy.ID, "tw.heroicfaith.fa3:id/checkbox_" + str(i)).click()
        time.sleep(0.5)

    # add custom event
    function_record_driver.find_element(
        AppiumBy.ID, "tw.heroicfaith.fa3:id/edit_note").send_keys("custom")
    time.sleep(0.5)
    # save event
    function_record_driver.find_element(
        AppiumBy.ID, "tw.heroicfaith.fa3:id/button_save").click()
    time.sleep(0.5)

    # mainwindow to drawer
    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonMenu"])
    time.sleep(0.5)

    DriverUtils.load_audio(function_record_driver,
                           "audios/" + audioName + ".wav", 26)
    DriverUtils.main_to_archive_private(function_record_driver)
    # get file (maybe we can create a function?)
    date = function_record_driver.find_element(AppiumBy.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text

    listFilename = ShellUtils.listFile(
        function_record_driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/')
    targetFilename = listFilename.replace('\r', '').split('\n')[0]
    targetZipPath = '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/'
    zipFile_base64 = DriverUtils.pull_file(
        function_record_driver, targetZipPath, targetFilename)
    local_zip_path = os.path.join(tmp_path / targetFilename)
    local_file_path = os.path.join(tmp_path)

    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, encryption_key)
    
    assert (len(unzip_result) == 0) 

    # get filename
    fileDatetime = listFilename.split('.')[0]
    filename = "airm_" + fileDatetime + "_1.json"
    json_file_path = os.path.join(tmp_path / filename)

    with open(json_file_path, "r", encoding="utf-8") as f:
        userData = f.read()

    # data testing part
    # sampling = open("samples/mainwindow/event_record_language" + str(language_index) + ".json", 'w', encoding="utf-8").write(userData)
    golden_sample = open("samples/mainwindow/event_record_language" + str(language_index) + ".json", 'r', encoding="utf-8").read()
    userData = json.loads(userData)
    golden_sample = json.loads(golden_sample)

    assert golden_sample["recordEvent"] == userData["recordEvent"]
