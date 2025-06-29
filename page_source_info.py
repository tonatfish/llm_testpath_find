from PIL import Image, ImageDraw, ImageFont
import time
import json
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement

import xml.etree.ElementTree as ET

appium_url = 'http://127.0.0.1:4723/wd/hub'
tmp_path = "E:/class/grad/project/llm_testpath_find/tmp/"

# process tests in folder

# 遞迴函式遍歷所有節點
# clickable to check if it's able to click
# class name with 'edit' to check if it can deal with input


def iterate_nodes(node: ET.Element, object_list, depth=0):
    indent = "  " * depth  # 用來顯示層級
    clickable = node.attrib.get('clickable', '')
    scrollable = node.attrib.get('scrollable', '')
    bounds = node.attrib.get('bounds', '')
    bounds = bounds.replace(']', ',').replace('[', '').split(',')
    del bounds[-1]
    bounds = [float(x) for x in bounds]
    if clickable == 'true':
        node_text = get_node_text(node)
        class_name = node.attrib.get('class', '')

        # print(f"{indent}Class: {class_name}, "
        #     f"Resource-ID: {node.attrib.get('resource-id', 'N/A')}, "
        #     f"Text: {node_text}, "
        #     f"clickable: {node.attrib.get('clickable', 'N/A')}, "
        #     f"bounds: {bounds}")

        obj_type = 'button'
        if class_name.find('Edit') != -1:
            obj_type = 'edit'

        obj = {'shape': {'x': bounds[0], 'y': bounds[1], 'width': bounds[2] - bounds[0],
                         'height': bounds[3] - bounds[1], }, 'text': node_text, 'type': obj_type}
        object_list.append(obj)
    else:
        if scrollable == 'true':
            obj = {'shape': {'x': bounds[0], 'y': bounds[1], 'width': bounds[2] -
                             bounds[0], 'height': bounds[3] - bounds[1], }, 'text': [], 'type': 'scroll'}
            object_list.append(obj)
        # print(f"{indent}Class: {node.attrib.get('class', 'N/A')}, "
        #     f"Resource-ID: {node.attrib.get('resource-id', 'N/A')}, "
        #     f"Text: {node.attrib.get('text', 'N/A')}, "
        #     f"clickable: {node.attrib.get('clickable', 'N/A')}, "
        #     f"bounds: {bounds}")

        # 遍歷所有子節點
        for child in node:
            iterate_nodes(child, object_list, depth + 1)


def get_node_text(node: ET.Element):
    text_list = []
    text = node.attrib.get('text', '')
    if text != '':
        text_list.append(text)
    for child in node:
        text_list.extend(get_node_text(child))
    return text_list


def find_scroll_nodes(node: ET.Element, object_list, depth=0):
    indent = "  " * depth  # 用來顯示層級
    clickable = node.attrib.get('clickable', '')
    scrollable = node.attrib.get('scrollable', '')
    bounds = node.attrib.get('bounds', '')
    bounds = bounds.replace(']', ',').replace('[', '').split(',')
    del bounds[-1]
    bounds = [float(x) for x in bounds]
    if clickable != 'true':
        if scrollable == 'true':
            obj = {'shape': {'x': bounds[0], 'y': bounds[1], 'width': bounds[2] -
                             bounds[0], 'height': bounds[3] - bounds[1], }, 'text': [], 'type': 'scroll'}
            object_list.append(obj)
        # print(f"{indent}Class: {node.attrib.get('class', 'N/A')}, "
        #     f"Resource-ID: {node.attrib.get('resource-id', 'N/A')}, "
        #     f"Text: {node.attrib.get('text', 'N/A')}, "
        #     f"clickable: {node.attrib.get('clickable', 'N/A')}, "
        #     f"bounds: {bounds}")

        # 遍歷所有子節點
        for child in node:
            find_scroll_nodes(child, object_list, depth + 1)


def test_process():
    global object_list
    apk_path = "E:/class/grad/project/llm_testpath_find/input/app-debug_1_6_2_b.apk"
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
    time.sleep(5)
    encryption_key = "Abcd1234!"
    element: WebElement = driver.find_element(AppiumBy.ID,
                                              "tw.heroicfaith.fa3:id/dialog_input")
    element.clear()
    element.send_keys(encryption_key)
    element: WebElement = driver.find_element(AppiumBy.ID,
                                              "android:id/button1")
    element.click()
    time.sleep(0.5)

    element: WebElement = driver.find_element(AppiumBy.ID,
                                              "tw.heroicfaith.fa3:id/dialog_input")
    element.clear()
    element.send_keys(encryption_key)
    element: WebElement = driver.find_element(AppiumBy.ID,
                                              "android:id/button1")
    element.click()
    time.sleep(1)
    test_input = ''
    while test_input != 'l':
        test_input = input()
        if (test_input == 'p'):
            get_page_info(driver, str(f"{tmp_path}/test_page_source.png"))


# mode: what to search. if mode == 1 then search for scroll only
def get_page_info(driver: WebDriver, path: str, mode: int = 0):
    object_list = []

    # 取得 view hierarchy
    view_hierarchy = driver.page_source
    # print(view_hierarchy)

    # 解析 XML
    root = ET.fromstring(view_hierarchy)
    if mode == 0:
        iterate_nodes(root, object_list)
    else:
        find_scroll_nodes(root, object_list)
    print(object_list)

    driver.save_screenshot(path)
    # print(driver.get_window_size())

    im = Image.open(path).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.load_default(size=20)

    for idx, obj in enumerate(object_list):
        color = (0, 204, 255)

        draw.rectangle((obj['shape']['x'], obj['shape']['y'], obj['shape']['x'] + obj['shape']
                       ['width'], obj['shape']['y'] + obj['shape']['height']), outline=color, width=5)
        draw.rectangle((obj['shape']['x'], obj['shape']['y'], obj['shape']
                       ['x'] + 30, obj['shape']['y'] + 22), fill=color, outline=color)
        draw.text((obj['shape']['x'] + 5, obj['shape']['y']),
                  str(idx), fill=(255, 255, 255), font=font, stroke_width=0)

    im.save(path, quality=95)
    return object_list


if __name__ == "__main__":
    test_process()
