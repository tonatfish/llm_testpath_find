from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
import time
import os

from openai_qa import check_picture_result


tmp_path = os.getenv("TMP_PATH")

'''
example omniparser output:
[{'from': 'omniparser', 'shape': {'x': 71.0, 'y': 8.999998, 'width': 102.0, 'height': 42.0}, 'text': '10.47', 'type': 'text'}, 
{'from': 'omniparser', 'shape': {'x': 692.99994, 'y': 21.0, 'width': 28.0, 'height': 14.0}, 'text': 'AUTO', 'type': 'text'}, 
{'from': 'omniparser', 'shape': {'x': 387.1589, 'y': 2411.6807, 'width': 294.433, 'height': 36.319336}, 'text': 'None', 'type': 'icon'}]
'''

# check and operate with suggested action
def operate_process(driver: WebDriver, process):
    print(process)
    print(process["action"])
    if process["action"].find("long click") != -1:
        long_click_operate(driver, process["to_operate"])
    elif process["action"].find("click") != -1:
        click_operate(driver, process["to_operate"])
    elif process["action"].find("scroll up") != -1:
        scroll_up_operate(driver, process)
    elif process["action"].find("scroll down") != -1:
        scroll_down_operate(driver, process)
    elif process["action"].find("edit") != -1:
        # TODO:T find a way to edit target
        edit_operate(driver, process["to_operate"], process["value"])
    elif process["action"].find("wait") != -1:
        time.sleep(float(process["value"]))

# deal click with position marked by omniparser
def click_operate(driver: WebDriver, to_operate, click_rate: float = 0.5):
    # print(to_operate)
    # find center point to click
    x = to_operate['shape']['x'] + to_operate['shape']['width'] * click_rate
    y = to_operate['shape']['y'] + to_operate['shape']['height'] / 2
    
    driver.tap([(x, y)], None)


# deal long click with position marked by omniparser
def long_click_operate(driver: WebDriver, to_operate):
    # print(to_operate)
    # find center point to click
    x = to_operate['shape']['x'] + to_operate['shape']['width'] / 2
    y = to_operate['shape']['y'] + to_operate['shape']['height'] / 2
    
    touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=touch_input)
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(1.5)
    actions.w3c_actions.pointer_action.release()
    actions.w3c_actions.pointer_action.click_and_hold()
    actions.perform()


# deal scroll with certain coordinate
def scroll_operate(driver: WebDriver, x, start_y, end_y):
    # swipe with little inertia (1.1sec):
    touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=touch_input)
    actions.w3c_actions.pointer_action.move_to_location(x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=200)
    actions.w3c_actions.pointer_action.move_to_location(x, end_y)
    actions.w3c_actions.pointer_action.release()
    actions.w3c_actions.pointer_action.click_and_hold()
    actions.perform()


# deal scroll up with screen provided to find value in screen
def scroll_up_operate(driver: WebDriver, to_operate):
    # TODO:T get well-specified answer from chatgpt to avoid adjust of not exist property
    if not 'value' in to_operate:
        to_operate['value'] = to_operate['target']
    # test with screen size first
    # TODO:T get some target section instead of window
    screen_size = driver.get_window_size()
    x = screen_size["width"] / 2
    start_y = screen_size["height"] * 1 / 4
    end_y = screen_size["height"] * 3 / 4

    # avoid inifinite scroll
    scroll_count = 0
    while (scroll_count < 10):
        scroll_operate(driver, x, start_y, end_y)
        time.sleep(0.2)
        screenshot = str(f"{tmp_path}/scroll_check{scroll_count}.png")
        driver.save_screenshot(screenshot)
        if (check_picture_result(to_operate["value"], screenshot)):
            break


# deal scroll down with screen provided to find value in screen
def scroll_down_operate(driver: WebDriver, to_operate):
    # TODO:T get well-specified answer from chatgpt to avoid adjust of not exist property
    if not 'value' in to_operate:
        to_operate['value'] = to_operate['target']
    # test with screen size first
    # TODO:T get some target section instead of window
    screen_size = driver.get_window_size()
    x = screen_size["width"] / 2
    start_y = screen_size["height"] * 3 / 4
    end_y = screen_size["height"] * 1 / 4

    # avoid inifinite scroll
    scroll_count = 0
    while (scroll_count < 10):
        scroll_operate(driver, x, start_y, end_y)
        time.sleep(0.2)
        screenshot = str(f"{tmp_path}/scroll_check{scroll_count}.png")
        driver.save_screenshot(screenshot)
        if (check_picture_result(to_operate["value"], screenshot)):
            break


from selenium.webdriver.common.keys import Keys
# deal edit with screen provided to input value
def edit_operate(driver: WebDriver, to_operate, value):
    # click first to focus on element
    click_operate(driver, to_operate, 0.9)
    actions = ActionChains(driver)
    for i in range(10):
        actions.send_keys(Keys.BACKSPACE)
    actions.send_keys(value)
    actions.perform()