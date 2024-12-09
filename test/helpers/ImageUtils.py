import uuid
from PIL import Image
from PIL import ImageChops
from pathlib import Path
import allure


def compare_images_from_file(expected_path, result_path, criteria: float):
    image_expected = Image.open(expected_path).convert('RGB')
    image_result = Image.open(result_path).convert('RGB')
    return compare_images_from_image(image_expected, image_result, criteria)


def compare_images(expected_path, result: Image, criteria: float):
    """
    Compare images with exact match
    :param expected_path: Expected image path
    :param result: Result image path
    :return: Same is True, otherwise is False
    """
    image_expected = Image.open(expected_path).convert('RGB')
    return compare_images_from_image(image_expected, result, criteria)


def compare_images_from_image(expected: Image, result: Image, criteria: float):
    """
    Compare images with exact match
    :param expected: Expected image
    :param result: Result image path
    :return: Same is True, otherwise is False
    """
    try:
        image_diff = ImageChops.difference(expected, result)
        # image_diff.show()
        # print(image_diff)
        if test_criteria_from_image(image_diff, criteria):
            return True
        else:
            image_diff.show()
            save_and_report_result(expected, result, image_diff)
            return False
    except ValueError as e:
        return False


def compare_images_from_image_display(before: Image, result: Image, criteria: float, offset: float):
    """
    Compare images with display line ignored
    :param before: Before image
    :param result: Result image path
    :return: Same is True, otherwise is False
    """
    try:
        image_diff = ImageChops.difference(before, result)
        # image_diff.show()
        # print(image_diff)
        if test_criteria_from_image_display(before, image_diff, criteria, offset):
            return True
        else:
            image_diff.show()
            save_and_report_result(before, result, image_diff)
            return False
    except ValueError as e:
        return False


def ai_preprocess(path, color):
    image = Image.open(path).convert('RGB')
    return ai_preprocess_from_image(image, color)


def ai_preprocess_from_image(image, color):
    pixel = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = pixel[x, y]
            if abs(r - color[0]) <= 35 and abs(g - color[1]) <= 35 and abs(b - color[2]) <= 35:
                pixel[x, y] = (255, 255, 255)
            else:
                pixel[x, y] = (0, 0, 0)
    return image


def test_color_in_image(path, color):
    image = Image.open(path).convert('RGB')
    return test_color_in_image_from_image(image, color)


def test_color_in_image_from_image(image: Image, color, ration = 1, offset = 0):
    colorList = Image.Image.getcolors(image, 200000)
    for i in colorList:
        if (i[1][0] >= color[0] * ration - offset and i[1][0] <= color[0] * ration + offset) and (i[1][1] >= color[1] * ration - offset and i[1][1] <= color[1] * ration + offset) and (i[1][2] >= color[2] * ration - offset and i[1][2] <= color[2] * ration + offset):
            return True
    # print(sorted(colorList, reverse=True))
    # print("\n")
    return False


def test_criteria(path, criteria):
    image_diff = Image.open(path)
    return test_criteria_from_image(image_diff, criteria)


def test_criteria_from_image(image_diff: Image, criteria):
    diff_count = 0.0
    pixel_count = image_diff.size[0] * image_diff.size[1]
    pixel = image_diff.load()
    for x in range(image_diff.size[0]):
        for y in range(image_diff.size[1]):
            r, g, b = pixel[x, y]
            if not(r <= 5 or g <= 5 or b <= 5):
                # print(r,g,b)
                diff_count += 1
    # print(diff_count)
    # print(pixel_count)
    return (1 - diff_count / pixel_count > criteria)


def test_criteria_from_image_display(before: Image, image_diff: Image, criteria, offset):
    diff_count = 0.0
    pixel_count = image_diff.size[0] * image_diff.size[1]
    pixel = image_diff.load()
    before_pixel = before.load()
    for x in range(image_diff.size[0]):
        for y in range(image_diff.size[1]):
            r, g, b = pixel[x, y]
            rb, gb, bb = before_pixel[x, y]
            if not(r <= 5 or g <= 5 or b <= 5):
                diff_count += 1
    # print(diff_count)
    # print(pixel_count)
    return (1 - diff_count / pixel_count >= criteria - offset) and (1 - diff_count / pixel_count <= criteria + offset)


def crop_image(image: Image, x: int, y: int, width: int, height: int):
    image_crop = Image.new('RGB', image.size, (0, 0, 0))
    image_crop.paste(image, (0, 0))
    image_crop = image_crop.crop((x, y, x + width, y + height))
    return image_crop


def ai_crop_image(image: Image, x: int, y: int, width: int, height: int, size: int):
    image_crop = crop_image(image, x, y, width, height)
    image_ai = Image.new('RGB', [size, size], (0, 0, 0))
    image_ai.paste(image_crop, (int((size - width) / 2),
                   int((size - height) / 2)))
    return image_ai


def mask_image(image: Image, x: int, y: int, width: int, height: int):
    """
    Mask area in image
    :param image: Image
    :param x: X coordinate of top left corner of mask area
    :param y: Y coordinate of top left corner of mask area
    :param width: Width of mask area
    :param height: Height of mask area
    :return: Masked image
    """
    image_mask = Image.new('RGB', image.size, (0, 0, 0))
    mask_blank = Image.new('RGB', (width, height), (0, 0, 0))
    image_mask.paste(image, (0, 0))
    image_mask.paste(mask_blank, (x, y))
    return image_mask


def crop_element_with_path(path, element: dict):
    """
    Crop area in image with image path
    :param path: str path of image
    :param element: the element to crop
    """
    image = Image.open(str(path)).convert('RGB')
    image = crop_image(
        image, element['x'], element['y'], element['width'], element['height'])
    return image


def crop_element_with_image(image: Image, element: dict):
    """
    Crop area in image with image path
    :param image: Image
    :param element: the element to crop
    """
    image = crop_image(
        image, element['x'], element['y'], element['width'], element['height'])
    return image


def mask_elements_in_image(path, *elements: dict):
    image = Image.open(str(path)).convert('RGB')
    for element in elements:
        image = mask_image(
            image, element['x'], element['y'], element['width'], element['height'])
    return image


# this is for screen which will be moved by control panel
def mask_elements_in_image_with_offset(path, offset: int, *elements: dict):
    image = Image.open(str(path)).convert('RGB')
    for element in elements:
        image = mask_image(
            image, element['x'] - offset, element['y'], element['width'], element['height'])
    return image


def save_and_report_result(expected: Image, result: Image, difference: Image):
    id = uuid.uuid4()
    pathdir = Path("result/img/")
    pathdir.mkdir(parents=True, exist_ok=True)
    result_path = pathdir/f"{id}_result.png"
    result.save(result_path)
    allure.attach.file(result_path, "Result",
                       attachment_type=allure.attachment_type.PNG)
    # print(f"[[ATTACHMENT|{result_path}]]")
    expected_path = pathdir/f"{id}_expected.png"
    expected.save(expected_path)
    allure.attach.file(expected_path, "Expected",
                       attachment_type=allure.attachment_type.PNG)
    difference_path = pathdir/f"{id}_difference.png"
    difference.save(difference_path)
    allure.attach.file(difference_path, "Difference",
                       attachment_type=allure.attachment_type.PNG)
    return id


def save_and_report_result_with_video(result_list: list, video: bytes):
    id = uuid.uuid4()
    pathdir = Path("result/img/")
    pathdir.mkdir(parents=True, exist_ok=True)
    for i, result in enumerate(result_list):
        result_path = pathdir/f"{id}_result{str(i)}.png"
        result.save(result_path)
        allure.attach.file(result_path, "Result" + str(i), attachment_type=allure.attachment_type.PNG)
    video_path = pathdir/f"{id}_video.png"
    with open(video_path, 'wb') as record_video:
        record_video.write(video)
    allure.attach.file(video_path, "Video",
                       attachment_type=allure.attachment_type.MP4)
    return id