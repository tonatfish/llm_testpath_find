# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from appium.webdriver.webelement import WebElement
# from appium.webdriver.common.appiumby import AppiumBy
# from helpers import TextUtils
# from helpers import DriverUtils
# from helpers import ShellUtils
# import time
# import base64
# import os
# import pyzipper


# with open('elements/mainwindow.json', 'r') as jsonFile:
#     elements_mainwindow = json.load(jsonFile)


# @pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
# def test_AI(function_record_drawer_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str):
#     DriverUtils.load_audio(function_record_drawer_driver,
#                            "audios/" + audioName + ".wav", 26)
#     DriverUtils.main_to_archive_public(function_record_drawer_driver)
#     # get file (maybe we can create a function?)
#     date = function_record_drawer_driver.find_element(AppiumBy.XPATH,
#                                                       '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text

#     listFilename = ShellUtils.listFile(
#         function_record_drawer_driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/')
#     targetFilename = listFilename.replace('\r', '').split('\n')[0]
#     targetZipPath = '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/'
#     zipFile_base64 = DriverUtils.pull_file(
#         function_record_drawer_driver, targetZipPath, targetFilename)
#     zipFile = base64.b64decode(zipFile_base64)
#     local_zip_path = os.path.join(tmp_path / targetFilename)
#     local_file_path = os.path.join(tmp_path)

#     with open(local_zip_path, "wb") as f:
#         f.write(zipFile)

#     # unzip data
#     try:
#         time.sleep(0.5)
#         # os.system('7z x -o{f} -pZxcv@1234 {z}'.format(f=local_file_path, z=local_zip_path))
#         with pyzipper.AESZipFile(local_zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
#             extracted_zip.extractall(
#                 path=local_file_path, pwd=str.encode(encryption_key))
#     except Exception as e:
#         print(e)

#     # get AI filename
#     fileDatetime = listFilename.split('.')[0]
#     filename = "airm_" + fileDatetime + "_AI.txt"
#     ai_file_path = os.path.join(tmp_path / filename)
#     AI_data = []

#     with open(ai_file_path, "r") as f:
#         AI_data = f.read().replace('.', ':').split('\n')
    
#     print(AI_data)

#     # data testing
#     # it seperate data into array and combine them again after modifing time related elements
#     filetime = filename.replace("_AI.txt", "").replace(
#         "airm_", "").split('_')  # [0]: date, [1]: time
#     for i in range(len(AI_data)):
#         AI_data[i] = AI_data[i].split(' ')
#     for i in range(1, len(AI_data) - 1):
#         for j in range(1, len(AI_data[i])):
#             AI_data[i][j] = TextUtils.time_minus(AI_data[i][j], filetime[1])
#     print(AI_data)

#     output = ''
#     for i in range(len(AI_data) - 1):
#         for j in range(len(AI_data[i])):
#             if (j != 0):
#                 output += ' '
#             output += AI_data[i][j]
#         output += '\n'
#     # sampling = open("samples/record/" + audioName + "_AI.txt", 'w').write(output)

#     golden_sample = open("samples/record/" + audioName + "_AI.txt", 'r').read()
#     golden_sample = golden_sample.split('\n')
#     print(golden_sample)
#     if len(AI_data) != len(golden_sample):
#         sampling = open("samples/record/" + audioName + "_AI.txt", 'w').write(output)
#         assert len(AI_data) == len(golden_sample)
#     assert len(AI_data) == len(golden_sample)
#     for i in range(len(golden_sample)):
#         golden_sample[i] = golden_sample[i].split(' ')
#     for i in range(len(golden_sample)):
#         if len(golden_sample[i]) > 0:
#             assert AI_data[i][0] == golden_sample[i][0]
#     assert output == golden_sample
