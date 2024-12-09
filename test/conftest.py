import pytest
import sys
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ShellUtils
import json
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

# example: pytest -v --appPath=C://Users//david//OneDrive//Desktop//work//heroic_medic//codes//airmod_android11_official//app//build//outputs//apk//debug//AIRMOD_RELEASE.apk -k "test_red_light"

def pytest_addoption(parser):
    parser.addoption("--appPath", action="store",
                     default="app-debug.apk", help="Application absolute path")
    parser.addoption("--appiumUrl", action="store",
                     default="http://localhost:4723/wd/hub", help="Remote URL of Appium server")
    parser.addoption("--deviceName", action="store",
                     default="", help="Appium device name")


@pytest.fixture(scope='module')
def config(request):
    return request.config


@pytest.fixture(scope='module')
def app_path(config):
    return config.getoption("--appPath")


@pytest.fixture(scope='module')
def appium_url(config):
    return config.getoption("--appiumUrl")


@pytest.fixture(scope='module')
def device_name(config):
    return config.getoption("--deviceName")


@pytest.fixture(scope='module')
def encryption_key():
    return "ABcd1234!"


@pytest.fixture(scope='module')
def base_driver(app_path, appium_url, device_name):
    desiredCaps = dict(
        platformName='Android',
        platformVersion='14',
        automationName='uiautomator2',
        deviceName=device_name,
        autoGrantPermissions=True,
        app=app_path,
        newCommandTimeout=70,
        adbExecTimeout=70000,
        resetKeyboard=True,  # keyboard desire used to avoid keyboard appear to influence testing
        unicodeKeyboard=True,
    )
    driver = webdriver.Remote(appium_url, desiredCaps)
    driver.implicitly_wait(70)
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def before_password_driver(base_driver: WebDriver):
    try:
        if (int(base_driver.get_performance_data('tw.heroicfaith.fa3', 'batteryinfo')[1][0]) <= 30):
            time.sleep(1)
            with open('elements/mainwindow.json', 'r') as jsonFile:
                elements_mainwindow = json.load(jsonFile)
            ShellUtils.tap_element(
                base_driver, elements_mainwindow['lowBattery_confirm'])
        element: WebElement = base_driver.find_element(AppiumBy.ID,
                                                       "android:id/button2")
        element.click()
        time.sleep(1)
        # element: WebElement = base_driver.find_element(AppiumBy.ID,
        #                                                "android:id/button2")
        # element.click()
        # time.sleep(1)
        return base_driver
    except NoSuchElementException:
        # The permission window may have not appeared, so we skip clicking on it
        return base_driver


@pytest.fixture(scope='module')
def driver(before_password_driver: WebDriver, encryption_key):
    try:
        element: WebElement = before_password_driver.find_element(AppiumBy.ID,
                                                                  "tw.heroicfaith.fa3:id/dialog_input")
        element.clear()
        element.send_keys(encryption_key)
        element: WebElement = before_password_driver.find_element(AppiumBy.ID,
                                                                  "android:id/button1")
        element.click()
        time.sleep(0.5)

        element: WebElement = before_password_driver.find_element(AppiumBy.ID,
                                                                  "tw.heroicfaith.fa3:id/dialog_input")
        element.clear()
        element.send_keys(encryption_key)
        element: WebElement = before_password_driver.find_element(AppiumBy.ID,
                                                                  "android:id/button1")
        element.click()
        time.sleep(1)
        return before_password_driver
    except NoSuchElementException:
        # The permission window may have not appeared, so we skip clicking on it
        return before_password_driver


@pytest.fixture(scope='module')
def drawer_driver(driver: WebDriver):
    with open('elements/mainwindow.json', 'r') as jsonFile:
        elements_mainwindow = json.load(jsonFile)
    ShellUtils.tap_element(driver, elements_mainwindow["buttonMenu"])
    time.sleep(1)
    return driver


@pytest.fixture(scope='module')
def about_driver(drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(drawer_driver, elements_drawer["buttonAbout"])
    time.sleep(1)
    return drawer_driver


@pytest.fixture(scope='module')
def archive_driver(drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(drawer_driver, elements_drawer["buttonArchive"])
    time.sleep(1)
    return drawer_driver


@pytest.fixture(scope='module')
def settings_driver(drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(drawer_driver, elements_drawer["buttonSettings"])
    time.sleep(1)
    return drawer_driver


@pytest.fixture(scope='module')
def patient_driver(drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(drawer_driver, elements_drawer["buttonPatient"])
    time.sleep(1)
    return drawer_driver


@pytest.fixture(scope='module')
def trendview_driver(drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(drawer_driver, elements_drawer["buttonTrendView"])
    time.sleep(1)
    return drawer_driver


@pytest.fixture(scope='function')
def function_base_driver(app_path, appium_url, device_name):
    desiredCaps = dict(
        platformName='Android',
        platformVersion='14',
        automationName='uiautomator2',
        deviceName=device_name,
        autoGrantPermissions=True,
        app=app_path,
        newCommandTimeout=70,
        adbExecTimeout=70000,
        resetKeyboard=True,  # keyboard desire used to avoid keyboard appear to influence testing
        unicodeKeyboard=True,
    )
    driver = webdriver.Remote(appium_url, desiredCaps)
    driver.implicitly_wait(50)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def function_before_password_driver(function_base_driver: WebDriver):
    try:
        if (int(function_base_driver.get_performance_data('tw.heroicfaith.fa3', 'batteryinfo')[1][0]) <= 30):
            time.sleep(1)
            with open('elements/mainwindow.json', 'r') as jsonFile:
                elements_mainwindow = json.load(jsonFile)
            ShellUtils.tap_element(
                function_base_driver, elements_mainwindow['lowBattery_confirm'])
        element: WebElement = function_base_driver.find_element(AppiumBy.ID,
                                                                "android:id/button2")
        element.click()
        time.sleep(1)
        # element: WebElement = function_base_driver.find_element(AppiumBy.ID,
        #                                                         "android:id/button2")
        # element.click()
        # time.sleep(1)
        return function_base_driver
    except NoSuchElementException:
        # The permission window may have not appeared, so we skip clicking on it
        return function_base_driver


@pytest.fixture(scope='function')
def function_driver(function_before_password_driver: WebDriver, encryption_key):
    try:
        element: WebElement = function_before_password_driver.find_element(AppiumBy.ID,
                                                                  "tw.heroicfaith.fa3:id/dialog_input")
        element.clear()
        element.send_keys(encryption_key)
        element: WebElement = function_before_password_driver.find_element(AppiumBy.ID,
                                                                  "android:id/button1")
        element.click()
        time.sleep(0.5)

        element: WebElement = function_before_password_driver.find_element(AppiumBy.ID,
                                                                  "tw.heroicfaith.fa3:id/dialog_input")
        element.clear()
        element.send_keys(encryption_key)
        element: WebElement = function_before_password_driver.find_element(AppiumBy.ID,
                                                                  "android:id/button1")
        element.click()
        time.sleep(1)
        return function_before_password_driver
    except NoSuchElementException:
        # The permission window may have not appeared, so we skip clicking on it
        return function_before_password_driver


@pytest.fixture(scope='function')
def function_drawer_driver(function_driver: WebDriver):
    with open('elements/mainwindow.json', 'r') as jsonFile:
        elements_mainwindow = json.load(jsonFile)
    ShellUtils.tap_element(function_driver, elements_mainwindow["buttonMenu"])
    time.sleep(1)
    return function_driver


@pytest.fixture(scope='function')
def function_archive_driver(function_drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(function_drawer_driver, elements_drawer["buttonArchive"])
    time.sleep(1)
    return function_drawer_driver


# setting XPATH:
# Record ON/OFF: /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]
# AI ON/OFF: /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]
# read all channel: /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]


@pytest.fixture(scope='function')
def function_settings_driver(function_drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(function_drawer_driver,
                           elements_drawer["buttonSettings"])
    time.sleep(1)

    return function_drawer_driver


@pytest.fixture(scope='function')
def function_record_driver(function_settings_driver: WebDriver):
    # enable record
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    with open('elements/settings.json', 'r') as jsonFile:
        elements_setting = json.load(jsonFile)
    ShellUtils.tap_element(function_settings_driver,
                           elements_setting["buttonReturn"])
    time.sleep(1)

    return function_settings_driver


@pytest.fixture(scope='function')
def function_record_all_channel_driver(function_settings_driver: WebDriver):

    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()
    time.sleep(1)

    return function_settings_driver


@pytest.fixture(scope='function')
def function_record_no_ai_driver(function_settings_driver: WebDriver):

    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    function_settings_driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]').click()
    time.sleep(1)
    with open('elements/settings.json', 'r') as jsonFile:
        elements_setting = json.load(jsonFile)
    ShellUtils.tap_element(function_settings_driver,
                           elements_setting["buttonReturn"])
    time.sleep(1)

    return function_settings_driver


@pytest.fixture(scope='function')
def function_record_drawer_driver(function_record_driver: WebDriver):
    # mainwindow to drawer
    with open('elements/mainwindow.json', 'r') as jsonFile:
        elements_mainwindow = json.load(jsonFile)
    ShellUtils.tap_element(function_record_driver,
                           elements_mainwindow["buttonMenu"])
    time.sleep(1)
    return function_record_driver


@pytest.fixture(scope='function')
def audio_patient_driver(function_record_drawer_driver: WebDriver):
    with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
        elements_drawer = json.load(jsonFile)
    ShellUtils.tap_element(function_record_drawer_driver,
                           elements_drawer["buttonPatient"])
    time.sleep(5)
    return function_record_drawer_driver
