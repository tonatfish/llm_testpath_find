# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from helpers import DriverUtils
# from helpers import ShellUtils
# from helpers import ImageUtils
# import time


# with open('elements/mainwindow.json', 'r') as jsonFile:
#     elements_mainwindow = json.load(jsonFile)


# @pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
# def test_record_display(function_record_drawer_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str):
#     DriverUtils.load_audio(function_record_drawer_driver,
#                            "audios/" + audioName + ".wav", 26)
#     ShellUtils.tap_element(function_record_drawer_driver,
#                            elements_mainwindow["buttonFreeze"])

#     function_record_drawer_driver.save_screenshot(
#         str(tmp_path/"buttonDisplay_record_before_result.png"))
#     time.sleep(1)
#     ShellUtils.tap_element(function_record_drawer_driver,
#                            elements_mainwindow["buttonDisplay"])
#     function_record_drawer_driver.save_screenshot(
#         str(tmp_path/"buttonDisplay_record_after_result.png"))

#     result_before = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonDisplay_record_before_result.png"),
#                                                       elements_mainwindow["tvAppTitle"], elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"], elements_mainwindow["viewRrInfo"], elements_mainwindow["offsetTextLine"], elements_mainwindow["buttonDisplay"])
#     # result_before.save(tmp_path/"buttonDisplay_record_before_result.png")

#     result_after = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonDisplay_record_after_result.png"),
#                                                      elements_mainwindow["tvAppTitle"], elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"], elements_mainwindow["viewRrInfo"], elements_mainwindow["offsetTextLine"], elements_mainwindow["buttonDisplay"])
#     # result_after.save(tmp_path/"buttonDisplay_record_after_result.png")
#     # count difference between 0.994 +- 0.0015
#     assert ImageUtils.compare_images_from_image_display(
#         result_before, result_after, 0.994, 0.0015)
