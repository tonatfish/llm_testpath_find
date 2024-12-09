import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from helpers import ImageUtils
from helpers import DriverUtils
from helpers import ShellUtils
import time

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)

# to avoid noise information including display and AI signal, first disable them
# in this test, mask of 450hz-1050hz is increased due to some peak signal that shows under 450hz


@pytest.mark.parametrize("language_index", [1, 2, ])
@pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
def test_record_soundsetting(function_record_no_ai_driver: WebDriver, tmp_path: Path, audioName: str, language_index: int):
    DriverUtils.change_language_from_main_to_main(function_record_no_ai_driver, language_index)

    # disable display
    ShellUtils.tap_element(function_record_no_ai_driver,
                           elements_mainwindow["buttonDisplay"])
    time.sleep(0.5)

    # enter dialog
    ShellUtils.tap_element(function_record_no_ai_driver,
                           elements_mainwindow["buttonSoundSetting"])
    time.sleep(0.5)

    # swipe upper limit & lower limit to 450hz-1050hz
    x_20hz = [960, 870, ]
    x_450hz = [1250, 1150, ]
    x_1050hz = [1630, 1545, ]
    x_1500hz = [1920, 1845, ]
    y_hzBar = 430
    duration = 0
    function_record_no_ai_driver.swipe(
        x_20hz[language_index - 1], y_hzBar, x_450hz[language_index - 1], y_hzBar, duration)
    function_record_no_ai_driver.swipe(
        x_1500hz[language_index - 1], y_hzBar, x_1050hz[language_index - 1], y_hzBar, duration)

    # confirm setting
    ShellUtils.tap_element(function_record_no_ai_driver,
                           elements_mainwindow["soundSettingDialog_buttonConfirm"][language_index - 1])
    time.sleep(0.5)

    # mainwindow to drawer
    ShellUtils.tap_element(function_record_no_ai_driver,
                           elements_mainwindow["buttonMenu"])
    time.sleep(0.5)

    DriverUtils.load_audio(function_record_no_ai_driver,
                           "audios/" + audioName + ".wav", 23)
    time.sleep(3)

    function_record_no_ai_driver.save_screenshot(
        str(tmp_path / ("buttonSoundSetting_record_" + audioName + "_result.png")))

    # test with windowed masked out 450-1050hz to see if it's blank
    result = ImageUtils.mask_elements_in_image(str(tmp_path / ("buttonSoundSetting_record_" + audioName + "_result.png")),
                                               elements_mainwindow["tvAppTitle"], elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"], elements_mainwindow["viewRrInfo"], elements_mainwindow["surfaceView_450hz_1050hz"])
    # result.save("samples/mainwindow/buttonSoundSetting_record_" + audioName + "_language" + str(language_index) + "_result.png")

    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_record_" + audioName + "_language" + str(language_index) + "_result.png", result, 0.998)
