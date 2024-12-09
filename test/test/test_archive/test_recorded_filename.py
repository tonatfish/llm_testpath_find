# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from appium.webdriver.webelement import WebElement
# from appium.webdriver.common.appiumby import AppiumBy
# from helpers import TextUtils
# from helpers import ShellUtils
# import time

# with open('elements/archive.json', 'r') as jsonFile:
#     elements = json.load(jsonFile)


# def test_recorded_filename(recorded_driver: WebDriver):
#     ShellUtils.tap_element(recorded_driver, elements["firstOption"])
#     element: WebElement = recorded_driver.find_element(AppiumBy.XPATH,
#         "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]")
#     before = element.text
#     before = before[5:9] + "-" + before[9:11] + "-" + before[11:13] + " " + \
#         before[14:16] + ":" + before[16:18] + ":" + \
#         before[18:20]  # format for compare_time
#     compare = recorded_driver.get_device_time()
#     # it takes about 10 seconds for building a record
#     assert TextUtils.compare_time(before, compare, 10)
