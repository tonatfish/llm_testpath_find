# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from appium.webdriver.webelement import WebElement
# from helpers import TextUtils
# import time

# with open('elements/archive.json', 'r') as jsonFile:
#     elements = json.load(jsonFile)


# def test_recorded_folder(recorded_driver: WebDriver):
#     element: WebElement = recorded_driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]")
#     before = element.text
#     compare = recorded_driver.get_device_time()
#     assert TextUtils.compare_day(before, compare, 2)
