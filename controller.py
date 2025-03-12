import time
import json
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver


from openai_qa import get_process_answer, get_process_answer_omniparser, check_picture_result
from process_operator import operate_process
from format_checker import validate_test_input

# E:/class/grad/project/llm_testpath_find/input/app-debug.apk
# E:/class/grad/project/llm_testpath_find/input/test_step.json


appium_url = 'http://127.0.0.1:4723/wd/hub'
tmp_path = os.getenv("TMP_PATH")
output_path = os.getenv("OUTPUT_PATH")

# process tests in folder


def test_process(apk_path: str, test_path: str):
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
        if not validate_test_input(test_object):
            continue
        if test_object["tag"] == "new":
            record_steps = run_new_test(driver, test_object)

            # record steps to output
            output_json = {
                "tag": "record",
                "steps": record_steps
            }
            with open(output_path + "/record_" + file, "w") as output_file:
                json.dump(output_json, output_file)

        else:
            run_record_test(driver, test_object)
        driver.quit()


# run new test and make record
def run_new_test(driver: WebDriver, test_object):
    print("new test")

    step_count = 0
    assert_answer = True
    record_steps = []
    for step in test_object["steps"]:
        time.sleep(0.3)
        driver.save_screenshot(str(f"{tmp_path}/step{step_count}.png"))
        print(step)
        print(driver.get_window_size())
        if step['type'] == 'process':
            # get object on screen
            # try use screen size & image only to get coordinate
            print('process')
            process_answer = get_process_answer_omniparser(
                step['description'], f"{tmp_path}/step{step_count}.png")
            operate_process(driver, process_answer)
            # merge input to record
            process_answer.update(step)
            record_steps.append(process_answer)
        if step['type'] == 'assert':
            record_steps.append(step)
            print('assert')
            assert_result = check_picture_result(
                step['description'], f"{tmp_path}/step{step_count}.png")
            assert_answer = assert_answer and assert_result
            if not assert_result:
                print("assert false")
                break
        step_count += 1

    print("Final Assert Result:", assert_answer)
    return record_steps

# directly operate recorded test
def run_record_test(driver: WebDriver, test_object):
    print("old test")

    step_count = 0
    assert_answer = True
    for step in test_object["steps"]:
        time.sleep(0.3)
        driver.save_screenshot(str(f"{tmp_path}/step{step_count}.png"))
        print(step)
        print(driver.get_window_size())
        if step['type'] == 'process':
            operate_process(driver, step)
            time.sleep(0.5)
        if step['type'] == 'assert':
            print('assert')
            assert_result = check_picture_result(
                step['description'], f"{tmp_path}/step{step_count}.png")
            assert_answer = assert_answer and assert_result
            if not assert_result:
                print("assert false")
                break
        step_count += 1

    print("Final Assert Result:", assert_answer)
