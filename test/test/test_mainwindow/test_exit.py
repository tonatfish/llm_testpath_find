import pytest
import json
from pathlib import Path
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.applicationstate import ApplicationState
from helpers import ShellUtils
import time

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements = json.load(jsonFile)


def test_doExit(driver: WebDriver, tmp_path: Path):
    state = driver.query_app_state("tw.heroicfaith.fa3")
    assert state == ApplicationState.RUNNING_IN_FOREGROUND
    ShellUtils.tap_element(driver, elements["buttonExit"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements["exitDialogYes"])
    time.sleep(1)
    state = driver.query_app_state("tw.heroicfaith.fa3")
    assert state == ApplicationState.RUNNING_IN_BACKGROUND # since tested in ROG, it runs in background after exit
