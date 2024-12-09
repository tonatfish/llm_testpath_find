import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import DriverUtils
from helpers import ShellUtils
from helpers import TextUtils
import time

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)

with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
    elements_drawer = json.load(jsonFile)

with open('elements/archive.json', 'r') as jsonFile:
    elements_archive = json.load(jsonFile)

with open('elements/trendview.json', 'r') as jsonFile:
    elements_trendview = json.load(jsonFile)

with open('samples/trendview/trendview_file.json', 'r') as jsonFile:
    file_trendview = json.load(jsonFile)


@pytest.mark.parametrize("audioName", ['RR_04_main01', ])
def test_trendview_time(function_drawer_driver: WebDriver, tmp_path: Path, audioName: str):
    # load file
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/",
                          file_trendview[audioName]["ai"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/",
                          file_trendview[audioName]["rr"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/",
                          file_trendview[audioName]["alarm"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/",
                          file_trendview[audioName]["json"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    time.sleep(1)

    ShellUtils.tap_element(function_drawer_driver,
                           elements_drawer["buttonTrendView"])
    time.sleep(1)
    ShellUtils.tap_element(function_drawer_driver,
                           elements_archive["publicSelect"])
    function_drawer_driver.find_element(AppiumBy.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]').click()
    time.sleep(5)

    element: WebElement = function_drawer_driver.find_element(AppiumBy.ID,
                                                              "tw.heroicfaith.fa3:id/trendDateTime")
    # xpath: /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]
    before = element.text
    compare = function_drawer_driver.get_device_time()
    assert TextUtils.compare_time(before, compare, 3)

    time.sleep(5)
    after = element.text
    compare = function_drawer_driver.get_device_time()
    assert TextUtils.compare_time(after, compare, 3)
