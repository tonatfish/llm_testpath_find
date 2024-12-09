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

with open('elements/patient.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


def patient_language_setting(driver: WebDriver, language_index: int):
    ShellUtils.tap_element(driver, elements["buttonReturn"])
    time.sleep(1)
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    DriverUtils.main_to_patient(driver)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_patient(patient_driver: WebDriver, tmp_path: Path, language_index: int):
    patient_language_setting(patient_driver, language_index)

    patient_driver.save_screenshot(str(tmp_path / "patient_result.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"patient_result.png"), elements["systemControl"])
    # result.save("samples/patient/patient_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/patient/patient_language" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_patientIDButton(patient_driver: WebDriver, tmp_path: Path, language_index: int):
    patient_language_setting(patient_driver, language_index)

    testKey: str = "test"
    ShellUtils.tap_element(patient_driver, elements["btnPatientID"])

    element: WebElement = patient_driver.find_element( AppiumBy.ID,
        "android:id/edit")
    element.clear()
    element.send_keys(testKey)
    ShellUtils.tap_element(patient_driver, elements["patientInputDialog_ok"])
    time.sleep(1)

    patient_driver.save_screenshot(
        str(tmp_path / "patientIDButton_result.png"))
    result = ImageUtils.mask_elements_in_image(
        str(tmp_path/"patientIDButton_result.png"), elements["systemControl"])
    # result.save("samples/patient/patientIDButton_language" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/patient/patientIDButton_language" + str(language_index) + ".png", result, 0.998)
