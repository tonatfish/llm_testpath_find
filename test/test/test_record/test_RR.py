# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from appium.webdriver.webelement import WebElement
# from appium.webdriver.common.appiumby import AppiumBy
# from helpers import DriverUtils
# from helpers import TextUtils
# from helpers import ShellUtils
# import time
# import base64
# import os
# import pyzipper

# with open('elements/mainwindow.json', 'r') as jsonFile:
#     elements_mainwindow = json.load(jsonFile)


# # ("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'apnea_audio01', 'pao_audio01', ])
# @pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_25_main01', 'RR_30_main01', 'apnea_audio01', ])# ['RR_04_main01', 'RR_25_main01', 'RR_30_main01', 'apnea_audio01', ])
# def test_RR(function_record_drawer_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str):
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
#     local_file_path = os.path.join(tmp_path / audioName)

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
#     # get RR filename
#     fileDatetime = listFilename.split('.')[0]
#     filename = "airm_" + fileDatetime + "_RR.txt"
#     rr_file_path = os.path.join(tmp_path / filename)
#     RR_data = []

#     with open(rr_file_path, "r") as f:
#         RR_data = f.read().split('\n')

#     # data testing
#     # it seperate data into array and combine them again after modifing time related elements
#     filetime = filename.replace("_RR.txt", "").replace(
#         "airm_", "").split('_')  # [0]: date, [1]: time
#     # RR_data = RR_data.pop()
#     for i in range(len(RR_data)):
#         RR_data[i] = RR_data[i].split(' ')
#     for i in range(1, len(RR_data) - 1):
#         RR_data[i][0] = TextUtils.time_minus(
#             RR_data[i][0].replace(".", ":"), filetime[1])

#     # # set data as golden sample
#     # output = ''
#     # for i in range(len(RR_data) - 1):
#     #     for j in range(len(RR_data[i])):
#     #         if (j != 0):
#     #             output += ' '
#     #         output += RR_data[i][j]
#     #     output += '\n'
#     # sampling = open("samples/record/" + audioName + "_RR.txt", 'w').write(output)

#     # read golden sample and compare rr
#     golden_sample = open("samples/record/" + audioName +
#                          "_RR.txt", 'r').read().split('\n')
#     for i in range(len(golden_sample)):
#         golden_sample[i] = golden_sample[i].split(' ')
#     old_sample = golden_sample[1][0]
#     old_data = RR_data[1][0]
#     RR_data[1][0] = golden_sample[1][0]
#     for i in range(2, len(golden_sample) - 1):
#         print(i, ':')
#         assert TextUtils.compare_minus(
#             golden_sample[i][0], RR_data[i][0], old_sample, old_data)
#         old_sample = golden_sample[i][0]
#         old_data = RR_data[i][0]
#         RR_data[i][0] = golden_sample[i][0]

#     for i in range(1, len(RR_data) - 1):
#         rrValue = RR_data[i][1]
#         golden_rrValue = golden_sample[i][1]
#         rrUI = RR_data[i][2]
#         golden_rrUI = golden_sample[i][2]
#         if (rrUI == '35+'):
#             rrUI = '35'
#         if (golden_rrUI == '35+'):
#             golden_rrUI = '35'
#         assert (float(rrValue) < 0 and float(golden_rrValue) < 0) or (float(rrValue) <= float(
#             golden_rrValue) + 2 and float(rrValue) >= float(golden_rrValue) - 2)
#         assert (rrUI == golden_rrUI) or (float(rrUI) <= float(
#             golden_rrUI) + 2 and float(rrUI) >= float(golden_rrUI) - 2)
#         RR_data[i][1] = golden_sample[i][1]
#         RR_data[i][2] = golden_sample[i][2]

#     # delete download file
#     """time.sleep(1)
#     if os.path.exists(zipDir):
#         shutil.rmtree(zipDir, ignore_errors=True)"""

#     assert RR_data == golden_sample
