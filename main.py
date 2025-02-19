import argparse
import os, shutil
import time
import json

from appium import webdriver
from appium.options.android import UiAutomator2Options

from openai_qa import get_process_answer, get_process_answer_omniparser, check_picture_result
from process_operator import operate_process

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
    assert_answer = True
    for step in test_steps:
        time.sleep(0.3)
        driver.save_screenshot(str(f"{tmp_path}/step{step_count}.png"))
        print(step)
        print(driver.get_window_size())
        if step['type'] == 'process':
            # get object on screen
            # try use screen size & image only to get coordinate
            print('process')
            process_answer, parsed_content_list = get_process_answer_omniparser(step['description'], f"{tmp_path}/step{step_count}.png")
            operate_process(driver, process_answer, parsed_content_list)
        if step['type'] == 'assert':
            print('assert')
            assert_result = check_picture_result(step['description'], f"{tmp_path}/step{step_count}.png")
            if (assert_result < 0.7):
                assert_answer = False
                print("assert false")
                break
        step_count += 1
    
    print("Final Assert Result:", assert_answer)
    driver.quit()




def main():
    # setup environment & variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apk", help="apk path", dest="apk_path", default="E:/class/grad/project/llm_testpath_find/input/app-debug.apk")
    parser.add_argument("-t", "--test", help="test step file", dest="test_path", default="E:/class/grad/project/llm_testpath_find/input/test_step.json")
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