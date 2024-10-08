import argparse
import os, shutil
import time
import json

from appium import webdriver
from appium.options.android import UiAutomator2Options

from ollama_qa import get_process_answer

# E:/class/grad/project/llm_testpath_find/input/app-debug.apk
# E:/class/grad/project/llm_testpath_find/input/test_step.json

tmp_path = 'tmp/'
appium_url = 'http://127.0.0.1:4723/wd/hub'

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

    # test step construction
    test_steps = []
    with open(test_path) as json_file:
        test_steps = json.load(json_file)
    print(test_steps)

    step_count = 0
    for step in test_steps:
        time.sleep(0.3)
        driver.save_screenshot(str(f"{tmp_path}/step{step_count}.png"))
        print(step)
        print(driver.get_window_size())
        if step['type'] == 'process':
            # get object on screen
            # try use screen size & image only to get coordinate
            print('process')
            get_process_answer(step['description'], str(driver.get_window_size()), f"{tmp_path}/step{step_count}.png")
        if step['type'] == 'assert':
            print('assert')
        step_count += 1

    driver.quit()




def main():
    # setup environment & variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apk", help="apk path", dest="apk_path", default="D:/classes/grad/project/llm_testpath_find/input/app-debug.apk")
    parser.add_argument("-t", "--test", help="test step file", dest="test_path", default="D:/classes/grad/project/llm_testpath_find/input/test_step.json")
    args = parser.parse_args()
    apk_path = args.apk_path
    test_path = args.test_path
    print("apk path:", apk_path)
    print("test path:", test_path)

    # setup tmp folder for screenshots
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
    os.mkdir(tmp_path)
    
    print("start process")
    testpath_find(apk_path, test_path)

if __name__ == '__main__':
    main()