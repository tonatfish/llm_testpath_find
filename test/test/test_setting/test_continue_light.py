import base64
import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import DriverUtils
from helpers import ShellUtils
import cv2
import time
import datetime
import os.path

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)

with open('elements/settings.json', 'r') as jsonFile:
    elements_setting = json.load(jsonFile)


# ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'pao_audio01', 'apnea_audio01', ])
@pytest.mark.parametrize("audioName", ['apnea_audio01', 'pao_audio01', ])
def test_continue_light(function_record_driver: WebDriver, tmp_path: Path, audioName: str):
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
        function_record_driver, elements_setting["adjustView"], 3000)
    
    # set longer appnea white time
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]').click()

    function_record_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys("30")
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["dialogOK"])
    
    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)
    # set longer appnea red time
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()

    function_record_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys("30")
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["dialogOK"])

    DriverUtils.swipe_element_down(
        function_record_driver, elements_setting['mainContent'], 3000)

    # set continue count & ratio
    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()
    time.sleep(0.5)

    function_record_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys("1")
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["dialogOK"])
    time.sleep(0.5)

    function_record_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]').click()
    time.sleep(0.5)

    function_record_driver.find_element(
        AppiumBy.ID, "android:id/edit").clear().send_keys("0.1")
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["dialogOK"])
    time.sleep(0.5)
    ShellUtils.tap_element(function_record_driver,
                           elements_setting["buttonReturn"])
    time.sleep(0.5)

    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonMenu"])
    time.sleep(0.5)
    DriverUtils.load_audio_no_click(
        function_record_driver, "audios/" + audioName + ".wav")
    timeStart = datetime.datetime.now()
    function_record_driver.start_recording_screen()
    function_record_driver.find_element(AppiumBy.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[3]').click()

    time.sleep(1)
    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["screenRecord_keep"])
    time.sleep(24)
    continueDetected = 0
    continue_light_mp4 = base64.b64decode(
        function_record_driver.stop_recording_screen())
    with open(str(tmp_path / "continue_light.mp4"), 'wb') as record_video:
        record_video.write(continue_light_mp4)

    screenShotCount = 55
    start_time = 10 - 0.07
    frame_interval = 4
    frame_count = 0
    time_ctrl = 0
    assert os.path.isfile(str(tmp_path / "continue_light.mp4"))

    vc = cv2.VideoCapture(str(tmp_path / "continue_light.mp4"))
    assert vc.isOpened()
    vc.set(cv2.CAP_PROP_POS_MSEC, (start_time) * 1000)  # position(ms)
    rval, video_frame = vc.read()
    while rval and frame_count < screenShotCount:
        time_ctrl += 1
        if (time_ctrl % frame_interval == 0):
            cv2.imwrite(str(tmp_path / ("audio_continue_light_" + audioName +
                        "_result_" + str(frame_count) + ".png")), video_frame)
            frame_count += 1
        rval, video_frame = vc.read()
    vc.release()

    for i in range(frame_count):
        print(i)
        result = ImageUtils.crop_element_with_path(str(
            tmp_path / ("audio_continue_light_" + audioName + "_result_" + str(i) + ".png")), elements_mainwindow["surfaceView_upperBorder"])
        # result.save(str("samples/tmp/" + ("audio_continue_light_" + audioName + "_result_" + str(i) + ".png")))
        if ImageUtils.test_color_in_image_from_image(result, (234, 0, 245)) or ImageUtils.test_color_in_image_from_image(result, (254, 0, 255)):
            continueDetected += 1
    print(continueDetected)
    print(frame_count)
    if continueDetected == 0:
        result_list = []
        for i in range(frame_count):
            result_list.append(ImageUtils.mask_elements_in_image(tmp_path / ("audio_continue_light_" + audioName + "_result_" + str(i) + ".png"), elements_mainwindow["tvDateTime"]))
        ImageUtils.save_and_report_result_with_video(result_list, continue_light_mp4)
    assert continueDetected > 0
