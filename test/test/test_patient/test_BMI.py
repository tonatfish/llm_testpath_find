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
import base64

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


def enter_setting(patient_driver: WebDriver, xpath: str):
    setting: WebElement = patient_driver.find_element(AppiumBy.XPATH, xpath)
    setting.click()


def leave_setting(patient_driver: WebDriver):
    okButton: WebElement = patient_driver.find_element(AppiumBy.ID,
        "android:id/button1")
    okButton.click()


def input_setting(patient_driver: WebDriver, xpath: str, text: str):
    enter_setting(patient_driver, xpath)
    inputElement: WebElement = patient_driver.find_element(AppiumBy.ID,
        "android:id/edit")
    inputElement.clear()
    inputElement.send_keys(text)
    leave_setting(patient_driver)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_BMI(patient_driver: WebDriver, tmp_path: Path, language_index: int):
    patient_language_setting(patient_driver, language_index)

    # since scroll may not be very stable, xpath is needed to get element
    baseSettingXpathStart = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
    baseSettingXpathEnd = ']/android.widget.RelativeLayout'
    time.sleep(2)
    DriverUtils.swipe_element_down(
        patient_driver, elements["recyclerView"], 5000)
    DriverUtils.swipe_part_element_down(
        patient_driver, elements["recyclerView"], 5000, 0.7)
    time.sleep(1)
    input_setting(patient_driver, baseSettingXpathStart +
                  '2' + baseSettingXpathEnd, '200')
    input_setting(patient_driver, baseSettingXpathStart +
                  '3' + baseSettingXpathEnd, '80')
    enter_setting(patient_driver, baseSettingXpathStart +
                  '4' + baseSettingXpathEnd)
    bmiElement: WebElement = patient_driver.find_element(AppiumBy.ID,
        "android:id/edit")
    bmiResult = bmiElement.text
    assert bmiResult == '20.0'
    bmiElement.clear()
    bmiElement.send_keys('15.0')
    leave_setting(patient_driver)
    time.sleep(2)
    patient_driver.save_screenshot(
        str(tmp_path / "patientBMI_result.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"patientBMI_result.png"), elements["systemControl"])
    assert ImageUtils.test_color_in_image(
        str(tmp_path/"patientBMI_result.png"), (255, 0, 0))
