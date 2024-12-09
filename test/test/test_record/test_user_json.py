import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import ShellUtils
from helpers import DriverUtils
import time
import os

with open('elements/patient.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)


with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
    elements_drawer = json.load(jsonFile)

def patient_language_setting(driver: WebDriver, language_index: int):
    ShellUtils.tap_element(driver, elements["buttonReturn"])
    time.sleep(1)
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    DriverUtils.main_to_patient(driver)


def screenshot_compare(audio_patient_driver: WebDriver, tmp_path: Path, fileName: str, language_index: int):
    audio_patient_driver.save_screenshot(
        str(tmp_path / (fileName + "_result.png")))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path / (fileName + "_result.png")), elements["systemControl"])
    # result.save("samples/patient/" + fileName + "_language" + str(language_index) + ".png")
    return ImageUtils.compare_images(
        "samples/patient/" + fileName + "_language" + str(language_index) + ".png", result, 0.998)


def enter_setting(audio_patient_driver: WebDriver, xpath: str, tmp_path: Path):
    try:
        setting: WebElement = audio_patient_driver.find_element(
            AppiumBy.XPATH, xpath)
        setting.click()
    except:
        assert False
    time.sleep(1)


def leave_setting(audio_patient_driver: WebDriver):
    okButton: WebElement = audio_patient_driver.find_element(AppiumBy.ID,
                                                             "android:id/button1")
    okButton.click()
    time.sleep(0.5)


def input_setting(audio_patient_driver: WebDriver, xpath: str, text: str, tmp_path: Path):
    enter_setting(audio_patient_driver, xpath, tmp_path)
    inputElement: WebElement = audio_patient_driver.find_element(AppiumBy.ID,
                                                                 "android:id/edit")
    inputElement.clear()
    inputElement.send_keys(text)
    time.sleep(1)
    leave_setting(audio_patient_driver)


# this test also test UI change after input
# part are seperated by screen scroll
@pytest.mark.parametrize("language_index", [1, 2, ])
@pytest.mark.parametrize("audioName", ['RR_04_main01.wav', 'RR_06_main01.wav', 'RR_25_main01.wav', 'RR_30_main01.wav', 'RR_35_main01.wav', 'apnea_audio01.wav', 'pao_audio01.wav', ])
def test_user_json(audio_patient_driver: WebDriver, encryption_key: str, tmp_path: Path, audioName: str, language_index: int):
    patient_language_setting(audio_patient_driver, language_index)

    # since scroll may not be very stable, xpath is needed to get element
    baseSettingXpathStart = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
    baseSettingXpathEnd = ']/android.widget.RelativeLayout'

    # 1st part (setting 1-3)
    print('part1')
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '2' + baseSettingXpathEnd, 'testID', tmp_path)
    enter_setting(audio_patient_driver, baseSettingXpathStart +
                  '3' + baseSettingXpathEnd, tmp_path)
    ShellUtils.tap_element(audio_patient_driver, elements["btnDateSet"])
    time.sleep(0.5)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, 'test Hospital', tmp_path)
    time.sleep(1)
    assert screenshot_compare(audio_patient_driver,
                              tmp_path, "patient_screen_1", language_index)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 5000)
    time.sleep(1)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["adjustView"], 3000)
    time.sleep(1)

    # 2nd part (setting 4-7)
    print('part2')
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '1' + baseSettingXpathEnd, 'testOperator', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '3' + baseSettingXpathEnd, 'testName', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '4' + baseSettingXpathEnd, 'testBed', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, '20', tmp_path)
    time.sleep(1)
    # assert screenshot_compare(audio_patient_driver,
    #                          tmp_path, "patient_screen_2", language_index)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 3000)
    time.sleep(1)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["adjustView"], 3000)
    time.sleep(1)

    # 3rd part (setting 8-12)
    print('part3')
    enter_setting(audio_patient_driver, baseSettingXpathStart +
                  '1' + baseSettingXpathEnd, tmp_path)
    time.sleep(1)
    ShellUtils.tap_element(audio_patient_driver, elements["selectMale"])
    time.sleep(0.5)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '2' + baseSettingXpathEnd, '160', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '3' + baseSettingXpathEnd, '70.5', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, 'testDiagnose', tmp_path)
    time.sleep(1)
    # assert screenshot_compare(audio_patient_driver,
    #                          tmp_path, "patient_screen_3", language_index)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 5000)
    time.sleep(1)

    # 4th part (setting 13-17)
    print('part4')
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '2' + baseSettingXpathEnd, 'testHistory', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '3' + baseSettingXpathEnd, 'testTreatment', tmp_path)
    enter_setting(audio_patient_driver, baseSettingXpathStart +
                  '4' + baseSettingXpathEnd, tmp_path)
    audio_patient_driver.find_element(AppiumBy.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText').clear().send_keys('8')
    time.sleep(0.5)
    audio_patient_driver.find_element(AppiumBy.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText').clear().send_keys('9')
    time.sleep(0.5)
    leave_setting(audio_patient_driver)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, '60', tmp_path)
    
    time.sleep(1)
    # assert screenshot_compare(audio_patient_driver,
    #                          tmp_path, "patient_screen_4", language_index)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 5000)
    time.sleep(1)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["adjustView"], 3000)
    time.sleep(1)

    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '1' + baseSettingXpathEnd, '50', tmp_path)

    # 5th part (setting 18-20)
    print('part5')
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '2' + baseSettingXpathEnd, '40', tmp_path)
    enter_setting(audio_patient_driver, baseSettingXpathStart +
                  '4' + baseSettingXpathEnd, tmp_path)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_1"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_2"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_3"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_4"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_5"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_6"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectVentilation_7"])
    time.sleep(0.5)
    audio_patient_driver.find_element(AppiumBy.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.EditText').clear().send_keys('testVentilation')
    time.sleep(0.5)
    leave_setting(audio_patient_driver)
    enter_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, tmp_path)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_1"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_2"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_3"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_4"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_5"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_6"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_7"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_8"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_9"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["selectBodyPosition_10"])
    time.sleep(0.5)
    audio_patient_driver.find_element(AppiumBy.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.EditText').clear().send_keys('testBodyPosition')
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements["bodyPositionDialog_ok"])
    time.sleep(1)
    # assert screenshot_compare(audio_patient_driver,
    #                          tmp_path, "patient_screen_5", language_index)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 5000)
    time.sleep(1)

    # 6th part (setting 21-23)
    print('part6')
    enter_setting(audio_patient_driver, baseSettingXpathStart +
                  '3' + baseSettingXpathEnd, tmp_path)
    ShellUtils.tap_element(audio_patient_driver, elements["selectPrelabel_1"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver, elements["selectPrelabel_2"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver, elements["selectPrelabel_3"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver, elements["selectPrelabel_4"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver, elements["selectPrelabel_5"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver, elements["selectPrelabel_6"])
    time.sleep(0.5)
    leave_setting(audio_patient_driver)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '4' + baseSettingXpathEnd, 'testFeedback', tmp_path)
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, 'testComment', tmp_path)
    time.sleep(2)
    # assert screenshot_compare(audio_patient_driver,
    #                          tmp_path, "patient_screen_6", language_index)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 200)
    time.sleep(1)

    # 7th part (setting 24)
    print('part7')
    input_setting(audio_patient_driver, baseSettingXpathStart +
                  '5' + baseSettingXpathEnd, 'testNote', tmp_path)
    DriverUtils.swipe_element_down(
        audio_patient_driver, elements["recyclerView"], 200)
    time.sleep(1)
    assert screenshot_compare(audio_patient_driver,
                              tmp_path, "patient_screen_7", language_index)

    # record part
    ShellUtils.tap_element(audio_patient_driver, elements["buttonReturn"])
    time.sleep(0.5)
    ShellUtils.tap_element(audio_patient_driver,
                           elements_mainwindow["buttonMenu"])
    time.sleep(0.5)
    DriverUtils.load_audio(audio_patient_driver, "audios/" + audioName, 26)
    DriverUtils.main_to_archive_private(audio_patient_driver)
    time.sleep(1)

    # get file
    date = audio_patient_driver.find_element(AppiumBy.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').text

    listFilename = ShellUtils.listFile(
        audio_patient_driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/')
    targetFilename: str = listFilename.split('\n')[0].replace('\r', '')
    targetZipPath = '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/' + date + '/'
    zipFile_base64 = DriverUtils.pull_file(
        audio_patient_driver, targetZipPath, targetFilename)
    local_zip_path = os.path.join(tmp_path / targetFilename)
    local_file_path = os.path.join(tmp_path)

    unzip_result = DriverUtils.unzip_base64(
        zipFile_base64, local_zip_path, local_file_path, encryption_key)
    
    assert (len(unzip_result) == 0) 

    # get filename
    fileDatetime = listFilename.split('.')[0]
    filename = "airm_" + fileDatetime + "_1.json"
    json_file_path = os.path.join(tmp_path / filename)

    with open(json_file_path, "r", encoding="utf-8") as f:
        userData = f.read()

    # data testing part
    # sampling = open("samples/patient/patient_record_language" + str(language_index) + ".json", 'w', encoding="utf-8").write(userData)
    golden_sample = open("samples/patient/patient_record_language" + str(language_index) + ".json", 'r', encoding="utf-8").read()
    userData = json.loads(userData)
    golden_sample = json.loads(golden_sample)

    # ignore unique elements
    golden_sample["caseUUID"] = userData["caseUUID"]
    golden_sample["clipUUID"] = userData["clipUUID"]
    golden_sample["fileName"] = userData["fileName"]
    golden_sample["hardwareSerialNumber"] = userData["hardwareSerialNumber"]
    golden_sample["recordDuration"] = userData["recordDuration"]
    assert userData["fileName"] == filename.replace(".json", ".wav")
    golden_sample["recordDateTime"] = userData["recordDateTime"]
    assert filename.replace(".json", "").replace(
        "airm_", "").find(userData["recordDateTime"]) != -1  # -1 if didn't find time in filename
    audio_size = os.path.getsize(
        tmp_path / ("airm_" + fileDatetime + "_1.wav"))
    # 4000: sample rate, 32: 32bit float, 1: sound track, 8: bit to Byte
    audio_time = int(audio_size / 4000.0 / 32 / 1 * 8)
    # by directly measure time value, should ignore what's in old json sample
    assert int(userData["recordDuration"]) <= audio_time + \
        2 and int(userData["recordDuration"]) >= audio_time - 2
    time.sleep(1)
    assert golden_sample == userData


'''
In JSON file, not sure if we need to ignore things below:
hardwareModelName -> hardware
hardwareSerialNumber -> hardware
recordDuration -> +- 1-2 sec
recordMicrophone
recordEvent
preAndPostClipUUID

how to get element in screen:
/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout

to edit text:
android:id/edit

to press OK in most setting (position may not be same):
android:id/button1

to press SET in setting 2:
tw.heroicfaith.fa3:id/date_time_set [384,848][1959,972]

to select in setting 8:
[516,391][1827,535] Male
[516,535][1827,679] Female

to edit text in muti-line setting (15 & 19):
/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText

all of patient setting type: (int text float can use same way to input data)
ID&Birth
1.  text
2.  date
Recorder Info
3.  text
4.  text
Patient Info
5.  text
6.  text
7.  int
8.  select(gender)
9.  float
10. float
11. float(semi-auto)
12. text
13. text
14. text
15. int*2
16. int
17. int
18. int
Other Info
19. check
20. check
21. check
22. text
23. text
24. text
'''
