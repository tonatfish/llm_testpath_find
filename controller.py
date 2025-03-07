import time
import json
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options

from openai_qa import get_process_answer, get_process_answer_omniparser, check_picture_result
from process_operator import operate_process

# E:/class/grad/project/llm_testpath_find/input/app-debug.apk
# E:/class/grad/project/llm_testpath_find/input/test_step.json


appium_url = 'http://127.0.0.1:4723/wd/hub'
tmp_path = os.getenv("TMP_PATH")

def testpath_find(apk_path: str, test_path: str):
    # get test step file list
    file_to_test = []
    for file in os.listdir(test_path):
        if file.endswith(".json"):
            file_to_test.append(file)

    for file in file_to_test:
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
        test_object = {}
        with open(test_path + "/" + file) as json_file:
            test_object = json.load(json_file)
        print(test_object)

        step_count = 0
        assert_answer = True
        for step in test_object["steps"]:
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
