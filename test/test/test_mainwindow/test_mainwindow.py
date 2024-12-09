from appium.webdriver.extensions.android.power import Power
from appium.webdriver.webelement import WebElement
import pytest
import json
from pathlib import Path
from PIL import Image
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ImageUtils
from helpers import ShellUtils
from helpers import TextUtils
from helpers import DriverUtils
import time

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements = json.load(jsonFile)

# in initial state, there should be permission dialog above encryption dialog


def test_initial(base_driver: WebDriver, tmp_path: Path):
    time.sleep(1)
    base_driver.save_screenshot(str(tmp_path/"mainwindowInitial_result.png"))
    result = ImageUtils.crop_element_with_path(
        str(tmp_path/"mainwindowInitial_result.png"), elements["encryptionDialog"])

    # result.save("samples/mainwindow/mainwindowIntial.png")

    if (int(base_driver.get_performance_data('tw.heroicfaith.fa3', 'batteryinfo')[1][0]) <= 30):
        assert ImageUtils.compare_images(
            "samples/mainwindow/mainwindowIntial_lowBattery.png", result, 0.998)
    else:
        assert ImageUtils.compare_images(
            "samples/mainwindow/mainwindowIntial.png", result, 0.998)

# after permission state, there should be encryption dialog


def test_noPermission(before_password_driver: WebDriver, tmp_path: Path):
    time.sleep(1)

    before_password_driver.save_screenshot(
        str(tmp_path/"mainwindowNoPermission_result.png"))
    result = ImageUtils.crop_element_with_path(
        str(tmp_path/"mainwindowNoPermission_result.png"), elements["encryptionDialog"])
    # result.save("samples/mainwindow/mainwindowNoPermission.png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/mainwindowNoPermission.png", result, 0.998)

# after permission state, there should be mainwindow


def test_encrypted(driver: WebDriver, tmp_path: Path):
    driver.save_screenshot(str(tmp_path/"mainwindowEncrypted_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"mainwindowEncrypted_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/mainwindowEncrypted.png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/mainwindowEncrypted.png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_buttonSilent(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    ShellUtils.tap_element(driver, elements["buttonSilent"])
    time.sleep(0.5)
    driver.save_screenshot(str(tmp_path/"buttonSilent_silent_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonSilent_silent_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonSilent_silent_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSilent_silent_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["buttonSilent"])
    time.sleep(0.5)
    driver.save_screenshot(str(tmp_path/"buttonSilent_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonSilent_normal_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonSilent_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSilent_normal_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_buttonAlarm(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    ShellUtils.tap_element(driver, elements["buttonAlarm"])
    driver.save_screenshot(str(tmp_path/"buttonAlarm_silent_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonAlarm_silent_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonAlarm_silent_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonAlarm_silent_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["buttonAlarm"])
    driver.save_screenshot(str(tmp_path/"buttonAlarm_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonAlarm_normal_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonAlarm_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonAlarm_normal_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_buttonDisplay(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    ShellUtils.tap_element(driver, elements["buttonDisplay"])
    driver.save_screenshot(str(tmp_path/"buttonDisplay_display_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonDisplay_display_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonDisplay_display_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonDisplay_display_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["buttonDisplay"])
    driver.save_screenshot(str(tmp_path/"buttonDisplay_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonDisplay_normal_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonDisplay_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonDisplay_normal_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_buttonEvent(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    ShellUtils.tap_element(driver, elements["buttonEvent"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"buttonEvent_show_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonEvent_show_result.png"),
                                               elements["tvDateTime"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonEvent_show_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonEvent_show_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["buttonEvent"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"buttonEvent_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonEvent_normal_result.png"),
                                               elements["tvDateTime"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonEvent_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonEvent_normal_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_spinnerNoiseCancel(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    ShellUtils.tap_element(driver, elements["spinnerNoiseCancel"][language_index - 1])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"spinnerNoiseCancel_spinner_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerNoiseCancel_spinner_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerNoiseCancel_spinner_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerNoiseCancel_spinner_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["spinnerNoiseCancel_normal"][language_index - 1])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"spinnerNoiseCancel_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerNoiseCancel_normal_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerNoiseCancel_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerNoiseCancel_normal_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["spinnerNoiseCancel"][language_index - 1])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements["spinnerNoiseCancel_newDual"][language_index - 1])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"spinnerNoiseCancel_newDual_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerNoiseCancel_newDual_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerNoiseCancel_newDual_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerNoiseCancel_newDual_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, 3, 4, 5, ])
def test_spinnerOutputMode(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    ShellUtils.tap_element(driver, elements["spinnerOutputMode"])
    time.sleep(0.5)
    driver.save_screenshot(
        str(tmp_path/"spinnerOutputMode_spinner_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerOutputMode_spinner_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerOutputMode_spinner_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerOutputMode_spinner_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["spinnerOutputMode_silent"])
    time.sleep(0.5)
    driver.save_screenshot(
        str(tmp_path/"spinnerOutputMode_silent_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerOutputMode_silent_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerOutputMode_silent_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerOutputMode_silent_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["spinnerOutputMode"])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements["spinnerOutputMode_auto"])
    time.sleep(0.5)
    driver.save_screenshot(
        str(tmp_path/"spinnerOutputMode_auto_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerOutputMode_auto_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerOutputMode_auto_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerOutputMode_auto_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["spinnerOutputMode"])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements["spinnerOutputMode_spk"])
    time.sleep(0.5)
    driver.save_screenshot(
        str(tmp_path/"spinnerOutputMode_spk_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"spinnerOutputMode_spk_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/spinnerOutputMode_spk_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/spinnerOutputMode_spk_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_buttonSoundSetting(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    # enter dialog
    ShellUtils.tap_element(driver, elements["buttonSoundSetting"])
    time.sleep(1)
    driver.find_element(
        AppiumBy.ID, 'android:id/content').screenshot(str(tmp_path / "buttonSoundSetting_dialog_result.png"))
    result = Image.open(str(tmp_path / "buttonSoundSetting_dialog_result.png")).convert('RGB')
    # result.save("samples/mainwindow/buttonSoundSetting_dialog_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_dialog_language_" + str(language_index) + ".png", result, 0.998)

    # change bwe setting
    ShellUtils.tap_element(driver, elements["soundSettingDialog_spinnerBwe"][language_index - 1])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"buttonSoundSetting_spinner_result.png"))
    result = ImageUtils.crop_element_with_path(str(
        tmp_path/"buttonSoundSetting_spinner_result.png"), elements["soundSettingDialog_spinner"])
    # result.save("samples/mainwindow/buttonSoundSetting_spinner_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_spinner_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(
        driver, elements["soundSettingDialog_spinnerBwe_normal"][language_index - 1])
    time.sleep(1)
    driver.find_element(
        AppiumBy.ID, 'android:id/content').screenshot(str(tmp_path / "buttonSoundSetting_normal_result.png"))
    result = Image.open(str(tmp_path / "buttonSoundSetting_normal_result.png")).convert('RGB')
    # result.save("samples/mainwindow/buttonSoundSetting_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_normal_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(driver, elements["soundSettingDialog_spinnerBwe"][language_index - 1])
    time.sleep(1)
    ShellUtils.tap_element(
        driver, elements["soundSettingDialog_spinnerBwe_shift"][language_index - 1])
    time.sleep(1)
    driver.find_element(
        AppiumBy.ID, 'android:id/content').screenshot(str(tmp_path / "buttonSoundSetting_shift_result.png"))
    result = Image.open(str(tmp_path / "buttonSoundSetting_shift_result.png")).convert('RGB')
    # result.save("samples/mainwindow/buttonSoundSetting_shift_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_shift_language_" + str(language_index) + ".png", result, 0.998)

    # test confirm and reset
    ShellUtils.tap_element(driver, elements["soundSettingDialog_spinnerBwe"][language_index - 1])
    time.sleep(1)
    ShellUtils.tap_element(
        driver, elements["soundSettingDialog_spinnerBwe_normal"][language_index - 1])
    time.sleep(1)
    ShellUtils.tap_element(
        driver, elements["soundSettingDialog_buttonConfirm"][language_index - 1])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements["buttonSoundSetting"])
    time.sleep(1)
    driver.find_element(
        AppiumBy.ID, 'android:id/content').screenshot(str(tmp_path / "buttonSoundSetting_confirm_result.png"))
    result = Image.open(str(tmp_path / "buttonSoundSetting_confirm_result.png")).convert('RGB')
    # result.save("samples/mainwindow/buttonSoundSetting_confirm_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_confirm_language_" + str(language_index) + ".png", result, 0.998)

    ShellUtils.tap_element(
        driver, elements["soundSettingDialog_buttonDefault"][language_index - 1])
    time.sleep(1)
    driver.find_element(
        AppiumBy.ID, 'android:id/content').screenshot(str(tmp_path / "buttonSoundSetting_reset_result.png"))
    result = Image.open(str(tmp_path / "buttonSoundSetting_reset_result.png")).convert('RGB')
    # result.save("samples/mainwindow/buttonSoundSetting_reset_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonSoundSetting_reset_language_" + str(language_index) + ".png", result, 0.998)
    ShellUtils.tap_element(
        driver, elements["soundSettingDialog_buttonConfirm"][language_index - 1])


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_btnScreenLock(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)

    # lock screen
    ShellUtils.tap_element(driver, elements["btnScreenLock"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"btnScreenLock_locked_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"btnScreenLock_locked_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/btnScreenLock_locked_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/btnScreenLock_locked_language_" + str(language_index) + ".png", result, 0.998)

    # test all button except alarm & silent
    ShellUtils.tap_element(driver, elements["buttonMenu"])
    ShellUtils.tap_element(driver, elements["buttonExit"])
    ShellUtils.tap_element(driver, elements["buttonRtInfer"])
    ShellUtils.tap_element(driver, elements["spinnerOutputMode"])
    ShellUtils.tap_element(driver, elements["buttonSoundSetting"])
    ShellUtils.tap_element(driver, elements["buttonFreeze"])
    ShellUtils.tap_element(driver, elements["buttonDisplay"])
    ShellUtils.tap_element(driver, elements["spinnerNoiseCancel"][language_index - 1])
    ShellUtils.tap_element(driver, elements["buttonEvent"])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"btnScreenLock_locked_other_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"btnScreenLock_locked_other_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/btnScreenLock_locked_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/btnScreenLock_locked_language_" + str(language_index) + ".png", result, 0.998)

    # test lock and silent
    ShellUtils.tap_element(driver, elements["buttonSilent"])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"btnScreenLock_locked_silent_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"btnScreenLock_locked_silent_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/btnScreenLock_locked_silent_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/btnScreenLock_locked_silent_language_" + str(language_index) + ".png", result, 0.998)
    ShellUtils.tap_element(driver, elements["buttonSilent"])

    # test lock and alarm
    time.sleep(1)
    ShellUtils.tap_element(driver, elements["buttonAlarm"])
    time.sleep(1)
    driver.save_screenshot(
        str(tmp_path/"btnScreenLock_locked_alarm_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"btnScreenLock_locked_alarm_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/btnScreenLock_locked_alarm_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/btnScreenLock_locked_alarm_language_" + str(language_index) + ".png", result, 0.998)
    ShellUtils.tap_element(driver, elements["buttonAlarm"])

    # test cancel lock
    time.sleep(1)
    ShellUtils.tap_element(driver, elements["btnScreenLock"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"btnScreenLock_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"btnScreenLock_normal_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/btnScreenLock_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/btnScreenLock_normal_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_buttonExit(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)

    ShellUtils.tap_element(driver, elements["buttonExit"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"buttonExit_clicked_result.png"))
    result = ImageUtils.crop_element_with_path(
        str(tmp_path/"buttonExit_clicked_result.png"), elements["exitDialog"])
    # result.save("samples/mainwindow/buttonExit_clicked_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonExit_clicked_language_" + str(language_index) + ".png", result, 0.998)

    # buttonAlarm is just somewhere outside the dialog and control panel
    ShellUtils.tap_element(driver, elements["buttonAlarm"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"buttonExit_normal_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"buttonExit_normal_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/buttonExit_normal_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/buttonExit_normal_language_" + str(language_index) + ".png", result, 0.998)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_noExit(driver: WebDriver, tmp_path: Path, language_index: int):
    DriverUtils.change_language_from_main_to_main(driver, language_index)

    ShellUtils.tap_element(driver, elements["buttonExit"])
    time.sleep(1)

    ShellUtils.tap_element(driver, elements["exitDialogNo"])
    time.sleep(1)
    driver.save_screenshot(str(tmp_path/"dialogExit_no_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"dialogExit_no_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imageBattery"], elements["imgRelayBoard"])
    # result.save("samples/mainwindow/dialogExit_no_language_" + str(language_index) + ".png")
    assert ImageUtils.compare_images(
        "samples/mainwindow/dialogExit_no_language_" + str(language_index) + ".png", result, 0.998)


def test_textBattery(driver: WebDriver):
    element: WebElement = driver.find_element(AppiumBy.ID,
                                              "tw.heroicfaith.fa3:id/textViewBat")
    batteryTxt = element.text
    compareTxt = driver.get_performance_data('tw.heroicfaith.fa3', 'batteryinfo')[
        1][0]  # example returned batterydata: [['battery'],['100']]
    assert TextUtils.compare_battery(batteryTxt, compareTxt)


def test_textTime(driver: WebDriver):
    element: WebElement = driver.find_element(AppiumBy.ID,
                                              "tw.heroicfaith.fa3:id/tvDateTime")
    before = element.text
    compare = driver.get_device_time()
    assert TextUtils.compare_time(before, compare, 3)

    time.sleep(5)
    after = element.text
    compare = driver.get_device_time()
    assert TextUtils.compare_time(after, compare, 3)


@pytest.mark.parametrize("language_index", [1, 2, ])
def test_imageBattery(driver: WebDriver, tmp_path: Path, language_index: int):
    time.sleep(1)
    DriverUtils.change_language_from_main_to_main(driver, language_index)
    # example returned batterydata: [['battery'],['100']]
    batteryInfo = driver.execute_script("mobile:batteryInfo")
    print(batteryInfo)
    chargingLevel = int(batteryInfo['level'] * 100)
    batteryIsCharging = int(batteryInfo['state']) == 2 or int(
        batteryInfo['state']) == 14
    driver.save_screenshot(str(tmp_path/"imageBattery_result.png"))
    result = ImageUtils.mask_elements_in_image(str(tmp_path/"imageBattery_result.png"),
                                               elements["tvDateTime"], elements["surfaceView"], elements["textViewBat"], elements["imgRelayBoard"])

    if (chargingLevel < 20):
        if (batteryIsCharging):
            # result.save("samples/mainwindow/imageBattery_20_isCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_20_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        else:
            # result.save("samples/mainwindow/imageBattery_20_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_20_noCharge_language_" + str(language_index) + ".png", result, 0.998)
    elif (chargingLevel < 30):
        if (batteryIsCharging):
            # result.save("samples/mainwindow/imageBattery_30_isCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_30_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        else:
            # result.save("samples/mainwindow/imageBattery_30_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_30_noCharge_language_" + str(language_index) + ".png", result, 0.998)
    elif (chargingLevel < 50):
        if (batteryIsCharging):
            # result.save("samples/mainwindow/imageBattery_50_isCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_50_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        else:
            # result.save("samples/mainwindow/imageBattery_50_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_50_noCharge_language_" + str(language_index) + ".png", result, 0.998)
    elif (chargingLevel < 60):
        if (batteryIsCharging):
            # result.save("samples/mainwindow/imageBattery_60_isCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_60_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        else:
            # result.save("samples/mainwindow/imageBattery_60_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_60_noCharge_language_" + str(language_index) + ".png", result, 0.998)
    elif (chargingLevel < 80):
        if (batteryIsCharging):
            # result.save("samples/mainwindow/imageBattery_80_isCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_80_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        else:
            # result.save("samples/mainwindow/imageBattery_80_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_80_noCharge_language_" + str(language_index) + ".png", result, 0.998)
    elif (chargingLevel < 99):
        if (batteryIsCharging):
            # result.save("samples/mainwindow/imageBattery_90_isCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_90_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        else:
            # result.save("samples/mainwindow/imageBattery_90_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_90_noCharge_language_" + str(language_index) + ".png", result, 0.998)
    else:
        # if (batteryIsCharging):
        #     result.save("samples/mainwindow/imageBattery_full_isCharge_language_" + str(language_index) + ".png")
        #     assert ImageUtils.compare_images(
        #         "samples/mainwindow/imageBattery_full_isCharge_language_" + str(language_index) + ".png", result, 0.998)
        # else:
            # result.save("samples/mainwindow/imageBattery_full_noCharge_language_" + str(language_index) + ".png")
            assert ImageUtils.compare_images(
                "samples/mainwindow/imageBattery_full_noCharge_language_" + str(language_index) + ".png", result, 0.998)
