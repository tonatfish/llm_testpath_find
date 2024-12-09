from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from helpers import ShellUtils
import time
import json
import base64
import pyzipper

with open('elements/mainwindow_drawer.json', 'r') as jsonFile:
    elements_drawer = json.load(jsonFile)

with open('elements/mainwindow.json', 'r') as jsonFile:
    elements_mainwindow = json.load(jsonFile)

with open('elements/archive.json', 'r') as jsonFile:
    elements_archive = json.load(jsonFile)

with open('elements/settings.json', 'r') as jsonFile:
    elements_setting = json.load(jsonFile)

def tap(driver: WebDriver, x, y):
    driver.tap([(x, y)], None)


def tap_element(driver: WebDriver, element: dict):
    tap_x = element["x"] + element["width"] / 2
    tap_y = element["y"] + element["height"] / 2
    tap(driver, tap_x, tap_y)


def swipe_element_up(driver: WebDriver, element: dict, duration: int = 0):
    swipe_x = element["x"] + element["width"] / 2 + 1
    swipe_start_y = element["y"] + 1
    swipe_end_y = element["y"] + element["height"] - 1
    driver.swipe(swipe_x, swipe_start_y, swipe_x, swipe_end_y, duration)


def swipe_element_down(driver: WebDriver, element: dict, duration: int = 0):
    swipe_x = element["x"] + element["width"] / 2 + 1
    swipe_start_y = element["y"] + element["height"] - 1
    swipe_end_y = element["y"] + 1
    driver.swipe(swipe_x, swipe_start_y, swipe_x, swipe_end_y, duration)


def swipe_part_element_down(driver: WebDriver, element: dict, duration: int = 0, part: float = 0):
    swipe_x = element["x"] + element["width"] / 2 + 1
    swipe_start_y = int(element["y"] + element["height"] * part - 1)
    swipe_end_y = element["y"] + 1
    driver.swipe(swipe_x, swipe_start_y, swipe_x, swipe_end_y, duration)


def load_audio(driver: WebDriver, audioName: str, sleep_time: float):
    driver.push_file(
        '/storage/emulated/0/Android/test.wav', None, audioName)
    # ShellUtils.create_folder(
    #     driver, '/storage/emulated/0/Download/')
    ShellUtils.move_file(driver, '/storage/emulated/0/Android/test.wav',
                         '/storage/emulated/0/Download/test.wav')
    time.sleep(2)
    ShellUtils.tap_element(driver, elements_drawer["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_archive["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_archive["publicSelect"])
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[3]').click()
    # already got nearly 9.5 second delay on clicking due to hardware
    time.sleep(sleep_time)


def push_file(driver: WebDriver, path: str, fileName: str, destination: str):
    driver.push_file(
        '/storage/emulated/0/Android/' + fileName, None, path + fileName)
    ShellUtils.create_folder(
        driver, '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM')
    ShellUtils.move_file(
        driver, '/storage/emulated/0/Android/' + fileName, destination + fileName)


def pull_file(driver: WebDriver, path: str, fileName: str) -> str:
    # print(path)
    # print(fileName)
    # print(path + fileName)
    ShellUtils.copy_file(driver, path + fileName,
                         '/storage/emulated/0/Android/' + fileName)
    file_base64 = driver.pull_file('/storage/emulated/0/Android/' + fileName)
    ShellUtils.remove_file(driver, '/storage/emulated/0/Android/' + fileName)
    return file_base64


def load_audio_no_click(driver: WebDriver, audioName: str):
    driver.push_file(
        '/storage/emulated/0/Android/test.wav', None, audioName)
    # ShellUtils.create_folder(
    #     driver, '/storage/emulated/0/Download/')
    ShellUtils.move_file(driver, '/storage/emulated/0/Android/test.wav',
                         '/storage/emulated/0/Download/test.wav')
    time.sleep(2)
    ShellUtils.tap_element(driver, elements_drawer["buttonArchive"])
    time.sleep(2)
    ShellUtils.tap_element(driver, elements_archive["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_archive["publicSelect"])
    time.sleep(1)


def load_used_audio(driver: WebDriver, audioName: str, sleep_time: int):
    driver.push_file(
        '/storage/emulated/0/Android/data/tw.heroicfaith.fa3/files/AIRM/test.wav', None, audioName)
    time.sleep(2)
    ShellUtils.tap_element(driver, elements_drawer["buttonArchive"])
    time.sleep(2)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout[4]').click()
    time.sleep(sleep_time)


def main_to_archive(driver: WebDriver):
    ShellUtils.tap_element(driver, elements_mainwindow["buttonMenu"])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements_drawer["buttonArchive"])
    time.sleep(1)


def main_to_setting(driver: WebDriver):
    main_to_drawer(driver)
    ShellUtils.tap_element(driver, elements_drawer["buttonSettings"])
    time.sleep(1)


def main_to_archive_public(driver: WebDriver):
    ShellUtils.tap_element(driver, elements_mainwindow["buttonMenu"])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements_drawer["buttonArchive"])
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements_archive["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_archive["publicSelect"])
    time.sleep(1)


def main_to_archive_private(driver: WebDriver):
    ShellUtils.tap_element(driver, elements_mainwindow["buttonMenu"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_drawer["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_archive["buttonArchive"])
    time.sleep(1)
    ShellUtils.tap_element(driver, elements_archive["privateSelect"])
    time.sleep(1)


def main_to_drawer(driver: WebDriver):
    ShellUtils.tap_element(driver, elements_mainwindow["buttonMenu"])
    time.sleep(1)


def main_to_about(driver: WebDriver):
    main_to_drawer(driver)
    ShellUtils.tap_element(driver, elements_drawer["buttonAbout"])
    time.sleep(1)


def main_to_patient(driver: WebDriver):
    main_to_drawer(driver)
    ShellUtils.tap_element(driver, elements_drawer["buttonPatient"])
    time.sleep(1)


def change_language_from_main_to_main(driver: WebDriver, language_index: int):
    main_to_setting(driver)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]').click()
    driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[' + str(language_index) + ']').click()
    ShellUtils.tap_element(driver, elements_setting["buttonReturn"])
    time.sleep(0.5)
    element: WebElement = driver.find_element(
        AppiumBy.ID, "android:id/button2")
    element.click()
    time.sleep(1)


def setting_language_setting(driver: WebDriver, language_index: int):
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    swipe_element_down(
        driver, elements_setting['mainContent'], 200)
    time.sleep(1)
    driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]').click()
    driver.find_element(
        AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[' + str(language_index) + ']').click()
    time.sleep(0.5)
    ShellUtils.tap_element(driver, elements_setting["buttonReturn"])
    time.sleep(0.5)
    driver.find_element(AppiumBy.ID, "android:id/button2").click()
    time.sleep(0.5)
    main_to_setting(driver)


def unzip_base64(zipFile_base64: str, local_zip_path: str, local_file_path: str, encryption_key: str) -> str:
    zipFile = base64.b64decode(zipFile_base64)
    with open(local_zip_path, "wb") as f:
        f.write(zipFile)

    # unzip data
    try:
        time.sleep(0.5)
        # os.system('7z x -o{f} -pZxcv@1234 {z}'.format(f=local_file_path, z=local_zip_path))
        with pyzipper.AESZipFile(local_zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(
                path=local_file_path, pwd=str.encode(encryption_key))
    except Exception as e:
        print(e)
        return e.__str__()
    return ""
