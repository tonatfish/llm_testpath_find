import os, shutil
from appium.webdriver.webdriver import WebDriver
from pathlib import Path

from openai_qa import check_picture_result
from DriverUtils import swipe_element_down

backup_path = 'tmp/'
# setup tmp folder for screenshots
if os.path.exists(backup_path):
    shutil.rmtree(backup_path)
os.mkdir(backup_path)
def scroll_until_exist(description: str, driver: WebDriver, tmp_path: Path, element):
    scroll_count = 0
    driver.save_screenshot(str(tmp_path / "scrolled_img.png"))
    possible_score = check_picture_result(description, str(tmp_path / "scrolled_img.png"))
    driver.save_screenshot(str(backup_path + "/scrolled_img_" + description + "_" + str(scroll_count) + "_" + str(possible_score) + ".png"))
    
    while possible_score < 0.9:
        swipe_element_down(driver, element, 3000)
        scroll_count += 1
        driver.save_screenshot(str(tmp_path / "scrolled_img.png"))
        possible_score = check_picture_result(description, str(tmp_path / "scrolled_img.png"))
        driver.save_screenshot(str(backup_path + "/scrolled_img_" + description + "_" + str(scroll_count) + "_" + str(possible_score) + ".png"))
        if (scroll_count > 10):
            break