from appium.webdriver.webdriver import WebDriver

'''
example omniparser output:
[{'from': 'omniparser', 'shape': {'x': 71.0, 'y': 8.999998, 'width': 102.0, 'height': 42.0}, 'text': '10.47', 'type': 'text'}, 
{'from': 'omniparser', 'shape': {'x': 692.99994, 'y': 21.0, 'width': 28.0, 'height': 14.0}, 'text': 'AUTO', 'type': 'text'}, 
{'from': 'omniparser', 'shape': {'x': 387.1589, 'y': 2411.6807, 'width': 294.433, 'height': 36.319336}, 'text': 'None', 'type': 'icon'}]
'''

# check and operate with suggested action
def operate_process(driver: WebDriver, process, parsed_content_list):
    print(process)
    print(process["action"])
    print(parsed_content_list)
    if process["action"].find("click") != -1:
        click_operate(driver, parsed_content_list[int(process["label ID"][0])])

# deal click with position marked by omniparser
def click_operate(driver: WebDriver, to_operate):
    print(to_operate)
    # find center point to click
    x = to_operate['shape']['x'] + to_operate['shape']['width'] / 2
    y = to_operate['shape']['y'] + to_operate['shape']['height'] / 2
    
    driver.tap([(x, y)], None)