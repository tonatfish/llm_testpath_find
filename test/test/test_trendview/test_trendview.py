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


@pytest.mark.parametrize("language_index", [1, 2, ])
@pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_25_main01', 'RR_30_main01', 'apnea_audio01', ])
def test_trendview(function_drawer_driver: WebDriver, tmp_path: Path, audioName: str, language_index: int):
    ShellUtils.tap_element(function_drawer_driver, elements_drawer["surfaceView"])
    time.sleep(1)

    DriverUtils.change_language_from_main_to_main(function_drawer_driver, language_index)

    ShellUtils.tap_element(function_drawer_driver, elements_mainwindow["buttonMenu"])
    time.sleep(1)

    # load file
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/", file_trendview[audioName]["ai"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/", file_trendview[audioName]["rr"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/", file_trendview[audioName]["alarm"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    DriverUtils.push_file(function_drawer_driver, "samples/trendview/" + audioName + "/", file_trendview[audioName]["json"], '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/')
    time.sleep(1)

    ShellUtils.tap_element(function_drawer_driver, elements_drawer["buttonTrendView"])
    time.sleep(1)
    ShellUtils.tap_element(function_drawer_driver, elements_archive["publicSelect"])
    time.sleep(1)
    function_drawer_driver.find_element(AppiumBy.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]').click()
    time.sleep(5)

    # test loaded image
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_loaded_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_loaded_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_loaded_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_loaded_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)
    
    # test freeze image
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["buttonFreeze"])
    time.sleep(0.5)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_freeze_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_freeze_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_freeze_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_freeze_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)
    
    # test unfreeze image
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["buttonFreeze"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_unfreeze_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_unfreeze_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_unfreeze_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_unfreeze_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

    # test time scale
    # 12hr
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["timeScaler_720"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_720_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_720_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_720_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_720_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

    # 6hr
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["timeScaler_360"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_360_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_360_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_360_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_360_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

    # 2hr
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["timeScaler_120"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_120_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_120_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_120_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_120_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

    # 1hr
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["timeScaler_60"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_60_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_60_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_60_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_60_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

    # 30min
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["timeScaler_30"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_30_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_30_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_30_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_30_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

    # 10min
    ShellUtils.tap_element(function_drawer_driver, elements_trendview["timeScaler_10"])
    time.sleep(1)
    function_drawer_driver.save_screenshot(
        str(tmp_path / ("trendview_10_" + audioName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / ("trendview_10_" + audioName + "_result.png")), elements_trendview["trendDateTime"])
    # result.save("samples/trendview/" + audioName + "/trendview_10_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/trendview/" + audioName + "/trendview_10_language" + str(language_index) + ".png", result, 0.99)
    time.sleep(1)

