# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from appium.webdriver.webelement import WebElement
# from helpers import ImageUtils
# from helpers import DriverUtils
# import time

# with open('elements/mainwindow.json', 'r') as jsonFile:
#     elements_mainwindow = json.load(jsonFile)


# @pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
# def test_spectrum(function_drawer_driver: WebDriver, tmp_path: Path, audioName: str):
#     DriverUtils.load_audio(function_drawer_driver,
#                            "audios/" + audioName + ".wav", 25)
#     time.sleep(2)
#     function_drawer_driver.save_screenshot(
#         str(tmp_path / ("audio_loaded" + audioName + "_result.png")))
#     result = ImageUtils.mask_elements_in_image(
#         str(tmp_path / ("audio_loaded" + audioName + "_result.png")), elements_mainwindow["tvDateTime"], elements_mainwindow["textViewBat"], elements_mainwindow["imageBattery"], elements_mainwindow["imgRelayBoard"])
#     # result.save("samples/record/" + audioName + "_audio_loaded.png")
#     assert ImageUtils.compare_images(
#         "samples/record/" + audioName + "_audio_loaded.png", result, 0.99)
