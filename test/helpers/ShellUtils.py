from appium.webdriver.webdriver import WebDriver


def command(driver: WebDriver, command="", args=[], timeout=5000):
    result = driver.execute_script('mobile: shell', {
        "command": command,
        "args": args,
        "includeStderr": True,
        "timeout": timeout
    })
    assert result["stderr"] == ""
    return result["stdout"]


def remove_file(driver: WebDriver, to_remove):
    result = command(driver, "rm", [to_remove])
    return result


def copy_file(driver: WebDriver, location, destination):
    # print(location)
    # print(destination)
    result = command(driver, "cp", [location, destination], 10000)
    result = command(driver, "chmod", ['777', destination])
    return result


def move_file(driver: WebDriver, location, destination):
    result = command(driver, "chmod", ['777', location])
    result = command(driver, "mv", [location, destination])
    result = command(driver, "chmod", ['777', destination])
    return result


def listFile(driver: WebDriver, path: str):
    result = command(driver, "ls", [path])
    return result


def create_folder(driver: WebDriver, location):
    result = command(driver, "mkdir", ["-p", location])
    return result


def tap(driver: WebDriver, x, y):
    result = command(driver, "input", ["tap", x, y])
    return result


def type(driver: WebDriver, input: str):
    result = command(driver, "input", ["text", input])
    return result


def tap_element(driver: WebDriver, element: dict):
    tap_x = element["x"] + element["width"] / 2
    tap_y = element["y"] + element["height"] / 2
    return tap(driver, tap_x, tap_y)
