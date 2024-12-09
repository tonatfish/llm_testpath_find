# import base64
# import pytest
# import json
# from pathlib import Path
# from appium.webdriver.webdriver import WebDriver
# from appium.webdriver.webelement import WebElement
# from helpers import ImageUtils
# from helpers import DriverUtils
# from helpers import AIUtils
# from helpers import TextUtils
# from PIL import Image
# import cv2
# import time
# import datetime

# with open('elements/mainwindow.json', 'r') as jsonFile:
#     elements_mainwindow = json.load(jsonFile)


# # ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'pao_audio01', ])
# @pytest.mark.parametrize("audioName", ['RR_04_main01', 'RR_06_main01', 'RR_25_main01', 'RR_30_main01', 'RR_35_main01', 'pao_audio01', ])
# def test_rr_sign(function_drawer_driver: WebDriver, tmp_path: Path, audioName: str):
#     # process with time issue
#     deviceTime = function_drawer_driver.device_time
#     runnerTime = datetime.datetime.now()
#     deviceTime = datetime.datetime.strptime(deviceTime[0:19], "%Y-%m-%dT%H:%M:%S")
#     print(deviceTime)
#     print(runnerTime)
#     timeOffset = deviceTime - runnerTime - datetime.timedelta(0, 1.5)
#     print(timeOffset)

#     DriverUtils.load_audio_no_click(
#         function_drawer_driver, "audios/" + audioName + ".wav")
#     function_drawer_driver.start_recording_screen()
#     function_drawer_driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[3]').click()

#     time.sleep(17)
#     with open(str(tmp_path / "rr_sign.mp4"), 'wb') as record_video:
#         record_video.write(base64.b64decode(function_drawer_driver.stop_recording_screen()))
    

#     '''
#     # screenshot to get sign picture
#     # already got nearly 9.5 second delay on clicking due to hardware
#     timeRecord = []
#     time.sleep(7.5)
#     waitTime = 0.5
#     loopCount = 24
#     timeMid = datetime.datetime.now()
    
#     for i in range(loopCount):
#         function_drawer_driver.save_screenshot(
#             str(tmp_path / ("audio_red_light" + audioName + "_result_" + str(i) + ".png")))  # there's a +-0.04 seconds between each execution, typically 0.37
#         timeRecord.append(datetime.datetime.now() + timeOffset + 
#                           datetime.timedelta(0, 0.04))
#         if waitTime - (datetime.datetime.now() - timeMid).total_seconds() > 0:
#             time.sleep(waitTime - (datetime.datetime.now() -
#                        timeMid).total_seconds())
#         timeMid = datetime.datetime.now()
#     # feed picture to ai to get value
#     aiRecord = []
    
#     for i in range(loopCount):
#         result = ImageUtils.crop_elements_in_image(str(
#             tmp_path / ("audio_red_light" + audioName + "_result_" + str(i) + ".png")), elements_mainwindow["RRsign"])
#         result = ImageUtils.ai_preprocess_from_image(
#             result, (128, 203, 196))  # set image as black and white
#         # result.save("samples/rr_sign/audio_red_light_" + audioName + "_RRsign_" + str(i) + ".png")
#         if ImageUtils.compare_images("samples/rr_sign/rr_35_plus.png", result, 0.998):
#             aiRecord.append('35+')
#         elif ImageUtils.compare_images("samples/rr_sign/rr_not_found.png", result, 0.998):
#             aiRecord.append('--')
#         else:
#             result_1 = ImageUtils.ai_crop_image(result, 0, 35, 85, 140, 200)
#             result_2 = ImageUtils.ai_crop_image(result, 100, 35, 85, 140, 200)
#             result_1.save(str(tmp_path / ("audio_red_light" +
#                           audioName + "_result_" + str(i) + "_1.png")))
#             result_2.save(str(tmp_path / ("audio_red_light" +
#                           audioName + "_result_" + str(i) + "_2.png")))
#             test_output = 0
#             if (ImageUtils.test_color_in_image_from_image(result_1, (255, 255, 255))):
#                 test_output = AIUtils.predict_from_path(
#                     str(tmp_path / ("audio_red_light" + audioName + "_result_" + str(i) + "_1.png")))
#             test_output = test_output * 10 + AIUtils.predict_from_path(
#                 str(tmp_path / ("audio_red_light" + audioName + "_result_" + str(i) + "_2.png")))
#             aiRecord.append(str(test_output))
#     '''
#     # get file
#     DriverUtils.main_to_archive(function_drawer_driver)
#     date = function_drawer_driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text
#     function_drawer_driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]').click()
#     time.sleep(2)
#     filename: str = function_drawer_driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text
#     filenameList = filename.replace(".wav", "").split('_')
#     if len(filenameList) == 4:
#         filenameList.pop()
#     filename = "_".join(filenameList) + "_RR.txt"
#     RR_data = function_drawer_driver.pull_file(
#         '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/' + filename)
#     RR_data = base64.b64decode(RR_data).decode("utf-8").split('\n')

#     # data testing
#     filetime = filename.replace("_RR.txt", "").replace(
#         "airm_", "").split('_')  # [0]: date, [1]: time
#     for i in range(len(RR_data)):
#         RR_data[i] = RR_data[i].split(' ')
#     for i in range(1, len(RR_data) - 1):
#         RR_data[i][0] = TextUtils.time_minus_num(RR_data[i][0].replace(".", ":"), filetime[1])
#     rrCount = 1
#     timeCount = 0
#     falCount = 0
#     print(RR_data)
#     RR_data.pop(0)
#     RR_data.pop()
#     vc = cv2.VideoCapture(str(tmp_path / "rr_sign.mp4"))
#     time_offset = vc.get(cv2.CAP_PROP_FRAME_COUNT) / vc.get(cv2.CAP_PROP_FPS) - 26
#     assert vc.isOpened()
#     fault_ct = 0
#     for i in range(len(RR_data)):
#         print(RR_data[i])
#         vc.set(cv2.CAP_PROP_POS_MSEC, (RR_data[i][0] + time_offset) * 1000) # position(ms)
#         rval, video_frame = vc.read()
#         img_to_test = Image.fromarray(cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB))
#         img_to_test.resize((2400, 1080))
#         ai_result = ''

#         result = ImageUtils.crop_elements_with_image(img_to_test, elements_mainwindow["RRsign"])
#         # result.show()
#         result = ImageUtils.ai_preprocess_from_image(result, (131, 202, 199))  # set image as black and white
#         # result.show()
#         # result.save("samples/rr_sign/audio_red_light_" + audioName + "_RRsign_" + str(i) + ".png")
        
#         if ImageUtils.compare_images("samples/rr_sign/rr_35_plus.png", result, 0.96):
#             ai_result = '35+'
#         elif ImageUtils.compare_images("samples/rr_sign/rr_not_found.png", result, 0.998):
#             ai_result = '--'
#         elif ImageUtils.compare_images("samples/rr_sign/rr_27.png", result, 0.96):
#             ai_result = '27'
#         else:
#             result_1 = ImageUtils.ai_crop_image(result, 0, 35, 85, 140, 200)
#             result_2 = ImageUtils.ai_crop_image(result, 100, 35, 85, 140, 200)
#             result_1.save(str(tmp_path / ("audio_red_light" +
#                           audioName + "_result_" + str(i) + "_1.png")))
#             result_2.save(str(tmp_path / ("audio_red_light" +
#                           audioName + "_result_" + str(i) + "_2.png")))
#             test_output = 0
#             if (ImageUtils.test_color_in_image_from_image(result_1, (255, 255, 255))):
#                 test_output = AIUtils.predict_from_path(
#                     str(tmp_path / ("audio_red_light" + audioName + "_result_" + str(i) + "_1.png")))
#             test_output = test_output * 10 + AIUtils.predict_from_path(
#                 str(tmp_path / ("audio_red_light" + audioName + "_result_" + str(i) + "_2.png")))
#             ai_result = str(test_output)
#         if (ai_result != RR_data[i][2] and not(i > 0 and ai_result == RR_data[i - 1][2]) and not(i < len(RR_data) - 1 and ai_result == RR_data[i + 1][2])):
#             print(i)
#             print(ai_result)
#             result.save("samples/rr_sign/audio_red_light_" + audioName + "_RRsign_" + str(i) + ".png")
#             result_2.save("samples/rr_sign/audio_red_light_" + audioName + "_RRsign_" + str(i) + "_2.png")
#             fault_ct += 1
#     print(fault_ct)
#     assert fault_ct < len(RR_data) * 0.1
#     '''while rrCount < (len(RR_data) - 2) and timeCount < loopCount:
#         rrTime = datetime.datetime.strptime(
#             fileDate + " " + RR_data[rrCount + 1][0], "%Y%m%d %H:%M:%S.%f")
#         if (timeRecord[timeCount] < rrTime):
#             compareResult = (aiRecord[timeCount] == RR_data[rrCount + 1][2]) or (aiRecord[timeCount] == RR_data[rrCount][2])
#             if rrCount + 2 < len(RR_data) - 1:
#                 compareResult = compareResult or (aiRecord[timeCount] == RR_data[rrCount + 2][2])
#             if rrCount > 1:
#                 compareResult = compareResult or (aiRecord[timeCount] == RR_data[rrCount - 1][2])
#             if not(compareResult):
#                 print(str(aiRecord[timeCount]) + " " + str(RR_data[rrCount][2]) + " " + str(RR_data[rrCount + 1][2]) + " , " + str(timeRecord[timeCount]) + " " + str(RR_data[rrCount][0]) + " " + str(RR_data[rrCount + 1][0]))
#                 falCount += 1
#             timeCount += 1
#         else:
#             rrCount += 1
#     while timeCount < loopCount:
#         if not(aiRecord[timeCount] == RR_data[len(RR_data) - 2][2]):
#             print(str(aiRecord[timeCount]) + " " + str(RR_data[len(RR_data) - 2][2]) + " , " + str(timeRecord[timeCount]) + " " + str(RR_data[len(RR_data) - 2][0]))
#             falCount += 1
#         timeCount += 1
#     print(RR_data)
#     for i in range(len(timeRecord)):
#         print(str(timeRecord[i]) + " " + str(aiRecord[i]))
#     assert (falCount / loopCount) < 0.1'''


