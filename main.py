import argparse
import os, shutil
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

# E:/class/grad/project/llm_testpath_find/input/app-debug.apk

tmp_path = 'tmp/'
appium_url = 'http://localhost:4723/wd/hub'

def testpath_find(apk_path: str, test_path: str):
    # build appium driver
    desiredCaps = dict(
        platformName='Android',
        platformVersion='14',
        automationName='uiautomator2',
        deviceName='',
        autoGrantPermissions=True,
        app=apk_path,
        newCommandTimeout=86400,
        adbExecTimeout=70000,
        resetKeyboard=True,  # keyboard desire used to avoid keyboard appear to influence testing
        unicodeKeyboard=True,
    )
    capabilities_options = UiAutomator2Options().load_capabilities(desiredCaps)
    driver = webdriver.Remote(appium_url, options=capabilities_options)
    driver.implicitly_wait(70)

    time.sleep(10)
    print(0)
    driver.quit()




def main():
    # setup environment & variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apk", help="apk path", dest="apk_path", default="default")
    parser.add_argument("-t", "--test", help="test step file", dest="test_path", default="default")
    args = parser.parse_args()
    apk_path = args.apk_path
    test_path = args.test_path

    # setup tmp folder for screenshots
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
    os.mkdir(tmp_path)
    
    testpath_find(apk_path, test_path)

if __name__ == '__main__':
    main()