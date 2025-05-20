import re
import json
import base64
from openai import OpenAI
# from OmniParser import omniparser
import os 

from format_checker import validate_openai_output, validate_action_structure
from page_source_info import get_page_info

# client of OpenAI
openai_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=openai_key)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# ask openai to get process with image directly
def get_process_answer(description: str, image_path: str): # -> tuple[str, object]:
    message = f"Provided Image is an UI image. To test this ui, we need to perform the action that {description}. What action shall we do? (output template: {{ \"action\": [click / double-click / long press / scroll], \"position\": [x, y] }})"
    base64_image = encode_image(image_path)
    messages = [
        {"role": "system", "content": "You are an UI testing analysis assistant."},
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": message,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url":  f"data:image/jpeg;base64,{base64_image}"
                },
                },
            ],
        }
    ]
    ans = get_llm_answer(messages)
    print(ans)

allowed_options = ['click', 'check', 'scroll up', 'scroll down']
config = {
    'som_model_path': 'OmniParser/weights/icon_detect/best.pt',
    'device': 'gpu',
    'caption_model_path': 'OmniParser/weights/icon_caption_florence',
    'draw_bbox_config': {
        'text_scale': 0.8,
        'text_thickness': 2,
        'text_padding': 3,
        'thickness': 3,
    },
    'BOX_TRESHOLD': 0.05
}
# parser = omniparser.Omniparser(config)

# # ask openai to get process with image processed by omniparser
# def get_process_answer_omniparser(task_structure: str, image_path: str): # -> tuple[str, object]:
#     image, parsed_content_list = parser.parse(image_path)
#     print(parsed_content_list)
#     image.save(image_path)
#     message = f"Here is a UI screenshot image with bounding boxes and corresponding labeled ID overlayed on top of it, and here is a list of icon/text box description: {parsed_content_list}."\
#             f" Your task is {task_structure['description']}. The action to process is {task_structure['action']}."
#     if 'target' in task_structure:
#         message += f" The target to process is {task_structure['target']}."
#     message += "Which bounding box label you should operate on? "\
#             f"put your answer in the format of \n‘‘‘{{\"label ID\": [xx]}}‘‘‘, do not include the word \"json\" in response.\n"
#     base64_image = encode_image(image_path)
#     messages = [
#         {"role": "system", "content": "You are an UI testing analysis assistant."},
#         {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": message,
#                 },
#                 {
#                 "type": "image_url",
#                 "image_url": {
#                     "url":  f"data:image/jpeg;base64,{base64_image}"
#                 },
#                 },
#             ],
#         }
#     ]

#     # try to get json object from GPT string feedback
#     err_count = 0
#     output_obj = {}
#     while (err_count < 5):
#         ans = get_llm_answer(messages)
#         print(ans)
#         positions = [match.start() for match in re.finditer("‘‘‘", ans)]
#         if len(positions) != 2:
#             print('‘‘‘ label not found')
#             # according to test result, sometimes ‘‘‘ will be replaced by ```
#             positions_alter = [match.start() for match in re.finditer("```", ans)]
#             if len(positions_alter) != 2:
#                 print('``` label not found')
#                 err_count += 1
#                 continue
#             positions = positions_alter
#         output = ans[positions[0] + 3: positions[1]]
#         print(output)
#         try:
#             output_obj = json.loads(output)
#             if not validate_openai_output(output_obj):
#                 print('not correct format')
#                 err_count += 1
#                 continue
#             break
#         except:
#             print('not json')
#             err_count += 1
#     output_obj["to_operate"] = parsed_content_list[int(output_obj["label ID"][0])]

#     # change format to float
#     output_obj["to_operate"]['shape']['x'] = float(output_obj["to_operate"]['shape']['x'])
#     output_obj["to_operate"]['shape']['y'] = float(output_obj["to_operate"]['shape']['y'])
#     output_obj["to_operate"]['shape']['width'] = float(output_obj["to_operate"]['shape']['width'])
#     output_obj["to_operate"]['shape']['height'] = float(output_obj["to_operate"]['shape']['height'])
#     task_structure.update(output_obj)
#     return task_structure


from appium.webdriver.webdriver import WebDriver
# ask openai to get process with image processed by view hierarchy
def get_process_answer_view_hierarchy(task_structure: str, image_path: str, driver: WebDriver): # -> tuple[str, object]:
    info_mode = 0
    if task_structure["action"].find('scroll') != -1:
        info_mode = 1
    parsed_content_list = get_page_info(driver, image_path, info_mode)
    # image, parsed_content_list = parser.parse(image_path)
    # print(parsed_content_list)
    # image.save(image_path)
    message = f"Here is a UI screenshot image with bounding boxes and corresponding labeled ID overlayed on top of it, and here is a list of icon/text box description: {parsed_content_list}."\
            f" Your task is {task_structure['description']}. The action to process is {task_structure['action']}."
    if 'target' in task_structure:
        message += f" The target to process is {task_structure['target']}."
    message += "Which bounding box label you should operate on? "\
            f"put your answer in the format of \n‘‘‘{{\"label ID\": [xx]}}‘‘‘, do not include the word \"json\" in response.\n"
    base64_image = encode_image(image_path)
    messages = [
        {"role": "system", "content": "You are an UI testing analysis assistant."},
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": message,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url":  f"data:image/jpeg;base64,{base64_image}"
                },
                },
            ],
        }
    ]

    # try to get json object from GPT string feedback
    err_count = 0
    output_obj = {}
    while (err_count < 5):
        ans = get_llm_answer(messages)
        print(ans)
        positions = [match.start() for match in re.finditer("‘‘‘", ans)]
        if len(positions) != 2:
            print('‘‘‘ label not found')
            # according to test result, sometimes ‘‘‘ will be replaced by ```
            positions_alter = [match.start() for match in re.finditer("```", ans)]
            if len(positions_alter) != 2:
                print('``` label not found')
                err_count += 1
                continue
            positions = positions_alter
        output = ans[positions[0] + 3: positions[1]]
        print(output)
        try:
            output_obj = json.loads(output)
            if not validate_openai_output(output_obj):
                print('not correct format')
                err_count += 1
                continue
        except:
            print('not json')
            err_count += 1

        # check if it's a correct index
        if int(output_obj["label ID"][0]) >= len(parsed_content_list):
            print('index out of range')
            err_count += 1
        else:
            break
        
    output_obj["to_operate"] = parsed_content_list[int(output_obj["label ID"][0])]

    # change format to float
    output_obj["to_operate"]['shape']['x'] = float(output_obj["to_operate"]['shape']['x'])
    output_obj["to_operate"]['shape']['y'] = float(output_obj["to_operate"]['shape']['y'])
    output_obj["to_operate"]['shape']['width'] = float(output_obj["to_operate"]['shape']['width'])
    output_obj["to_operate"]['shape']['height'] = float(output_obj["to_operate"]['shape']['height'])
    task_structure.update(output_obj)
    return task_structure



# ask openai to return process object and process to do
def get_structure_process(task_description: str):
    message = f"Please parse the following command into a structured format, do not include the word \"json\" in response."\
            f"put your answer in the format of \n‘‘‘{{\"action\": \"action\", \"target\": \"target\"}}‘‘‘."\
            f"following these rules: 1. The `\"action\"` field must be one of the following: `[\"click\", \"long click\", \"scroll up\", \"scroll down\", \"edit\", \"wait\"]`."\
            f" 2. The `\"target\"` field represents the object being acted upon (e.g., a button, input field, etc.)."\
            f" 3. If `\"action\"` is `\"edit\"`, the `\"value\"` field must be included to specify the input text."\
            f" 4. If `\"action\"` is `\"scroll up\"` or `\"scroll down\"`, the `\"target\"` field can be omitted."\
            f" 5. If `\"action\"` is `\"wait\"`, the `\"value\"` field should specify the duration.\n"\
            f"examples:\ninput: click the button with home icon\noutput:{{\"action\": \"click\",\"target\": \"button with home icon\"}}\n\n"\
            f"input: long-click the profile picture\noutput:{{\"action\": \"long-click\",\"target\": \"profile picture\"}}\n\n"\
            f"input: scroll down the icon list to find home icon\noutput:{{\"action\": \"scroll down\", \"target\": \"icon list\", \"value\": \"home icon\"}}\n\n"\
            f"input: edit the search bar with 'hello'\noutput:{{\"action\": \"edit\",\"target\": \"search bar\",\"value\": \"hello\"}}\n\n"\
            f"input: wait for 5 seconds\noutput:{{\"action\": \"wait\",\"value\": \"5\"}}\n"\
            f"parse the following command:{task_description}"
    messages = [
        {"role": "system", "content": "You are an UI testing analysis assistant."},
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": message,
                },
            ],
        }
    ]

    # try to get json object from GPT string feedback
    err_count = 0
    output_obj = {}
    while (err_count < 5):
        ans = get_llm_answer(messages)
        print(ans)
        positions = [match.start() for match in re.finditer("‘‘‘", ans)]
        if len(positions) != 2:
            print('‘‘‘ label not found')
            # according to test result, sometimes ‘‘‘ will be replaced by ```
            positions_alter = [match.start() for match in re.finditer("```", ans)]
            if len(positions_alter) != 2:
                print('``` label not found')
                err_count += 1
                continue
            positions = positions_alter
        output = ans[positions[0] + 3: positions[1]]
        print(output)
        try:
            output_obj = json.loads(output)
            if not validate_action_structure(output_obj):
                print('not correct format')
                err_count += 1
                continue
            break
        except:
            print('not json')
            err_count += 1
    return output_obj


# Get true / false answer from description and screenshot image to see if description matches screenshot
def check_picture_result(description: str, image_path: str):
    # message = f"We want to assert the ui provided as image. The image should contain: {description}. Provide us only a similarity_score between 0 to 1. Please only output a floating-point number between 0 and 1 (for example: 0.53)."
    message = f"We want to assert the ui provided as image. The image should contain: {description}. Provide us only a similarity_score, 1 for image contain what it should contain and 0 for no. Please only output a number which is either 0 or 1 (for example: 0)."
    base64_image = encode_image(image_path)
    messages = [
        {"role": "system", "content": "You are an UI testing analysis assistant."},
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": message,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url":  f"data:image/jpeg;base64,{base64_image}"
                },
                },
            ],
        }
    ]
    score = -1
    err_count = 0
    while score == -1 and err_count < 5:
        try:
            score = get_llm_answer(messages)
            score = float(score)
        except ValueError:
            err_count += 1
            print("llm response not float")
    
    # print(score)
    if (score < 0.7):
        return False
    return True

def get_llm_answer(messages):
    completion = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    # get_process_answer_omniparser("click green light button", "E:/class/grad/project/llm_testpath_find/tmp/step0.png")
    check_picture_result("version tag 1.4.2f", "about_language1.png")
