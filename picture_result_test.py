from dotenv import load_dotenv


import json
import shutil
import os
from os import listdir
from os.path import isfile, join

# load .env for sensitive info
load_dotenv()

from openai_qa import check_picture_result

img_path = "E:\\class\\grad\\project\\llm_testpath_find\\experiment_record\\assert_image_list\\"
json_path = img_path + "judge.json"

# Open and read the JSON file
with open(json_path, 'r') as file:
    data = json.load(file)

total_exist_count = 0
total_not_exist_count = 0
total_correct_exist = 0
total_correct_not_exist = 0
exist_fail_list = []
not_exist_fail_list = []
# run through all imgs and exist / not exist to get answer and check
for img_data in data:
    exist_count = 0
    not_exist_count = 0
    correct_exist = 0
    correct_not_exist = 0
    print(img_data["img_filename"] + ":")

    print("should exist")
    for should_exist in img_data["exist"]:
        exist_count += 1
        result = check_picture_result(should_exist, img_path + img_data["img_filename"])
        if result == True:
            correct_exist += 1
        else:
            exist_fail_list.append(img_data["img_filename"] + "_" + should_exist)
        print(should_exist + ": " + str(result))
    
    print("should not exist")
    for should_not_exist in img_data["not_exist"]:
        not_exist_count += 1
        result = check_picture_result(should_not_exist, img_path + img_data["img_filename"])
        if result == False:
            correct_not_exist += 1
        else:
            not_exist_fail_list.append(img_data["img_filename"] + "_" + should_not_exist)
        print(should_not_exist + ": " + str(result))
    
    if exist_count > 0:
        print("True correctness: " + str(1.0 * correct_exist / exist_count))
    if not_exist_count > 0:
        print("False correctness: " + str(1.0 * correct_not_exist / not_exist_count))

    total_exist_count += exist_count
    total_not_exist_count += not_exist_count
    total_correct_exist += correct_exist
    total_correct_not_exist += correct_not_exist

print("Total exist test: " + str(total_exist_count))
print("Total correct exist: " + str(total_correct_exist))
if total_exist_count > 0:
    print("Total True correctness: " + str(1.0 * total_correct_exist / total_exist_count))
print("Total not exist test: " + str(total_not_exist_count))
print("Total correct not exist: " + str(total_correct_not_exist))
if total_not_exist_count > 0:
    print("Total False correctness: " + str(1.0 * total_correct_not_exist / total_not_exist_count))

print("failed exist:", exist_fail_list)

print("failed not exist:", not_exist_fail_list)