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

with open('elements/settings.json', 'r') as jsonFile:
    elements_setting = json.load(jsonFile)

with open('elements/archive.json', 'r') as jsonFile:
    elements_archive = json.load(jsonFile)


@pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
def test_rezip_file(function_record_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str):
    new_encryption_key = '1234Abcd?'

    # mainwindow to drawer & load file
    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonMenu"])

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
    print(listFilename)

    # test if it can only unzip successfully through correct encryption key
    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, new_encryption_key)

    assert (len(unzip_result) > 0)

    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, encryption_key)

    assert (len(unzip_result) == 0)

    oldUnzipFileList = os.listdir(local_file_path)

    # remove old zip file
    ShellUtils.remove_file(function_record_driver, targetZipPath + targetFilename)

    # back to mainwindow
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]').click()

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
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['adjustView'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['adjustView'], 3000)
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['adjustView'], 3000)

    # set new encryption key
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]').click()
    time.sleep(0.5)
    function_record_driver.find_element(
        AppiumBy.ID, 'android:id/edit').clear().send_keys(new_encryption_key)
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["buttonEncryptOk"])
    time.sleep(0.5)
    function_record_driver.find_element(
        AppiumBy.ID, "tw.heroicfaith.fa3:id/dialog_input").clear().send_keys(new_encryption_key)
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["buttonEncryptOk"])
    time.sleep(0.5)

    ShellUtils.tap_element(function_record_driver,
                           elements_setting["buttonReturn"])
    time.sleep(1)
    
    # to archive & enter rezip
    DriverUtils.main_to_archive(function_record_driver)
    ShellUtils.tap_element(function_record_driver,
                           elements_archive["buttonZip"])
    time.sleep(0.5)

    # rezip file
    ShellUtils.tap_element(function_record_driver,
                           elements_archive["privateSelect"])
    time.sleep(0.5)
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]').click()
    time.sleep(0.5)
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]').click()
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["buttonSaveOldRecord"])
    time.sleep(8)

    listFilename = ShellUtils.listFile(
        function_record_driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/')
    print(listFilename)

    # get file
    targetZipPath = '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/'
    zipFile_base64 = DriverUtils.pull_file(
        function_record_driver, targetZipPath, targetFilename)
    local_zip_path = os.path.join(tmp_path / targetFilename)
    local_file_path = os.path.join(tmp_path)

    # test if it can only unzip successfully through correct encryption key
    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, encryption_key)

    assert (len(unzip_result) > 0)

    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, new_encryption_key)

    assert (len(unzip_result) == 0)

    newUnzipFileList = os.listdir(local_file_path)

    print(oldUnzipFileList)
    print(newUnzipFileList)
    assert oldUnzipFileList == newUnzipFileList


# change key: 3, zip: 4
# key edit: android:id/edit
# /hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]
# /hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]
