# #-*- coding:utf-8 -*-

# import datetime
# import os
# import platform
# import re
# import time
# #from PIL import Image
# #from PIL import ImageDraw
# #from PIL import ImageFont
# #from PIL import ImageChops
# #from PIL import ImageEnhance
# import pytest
# import subprocess
# import json

# arm_IP = "192.168.68.2"
# serial_tmp = "103"
# docker_id = "152634d9671a"
# server_IP = "http://192.168.150.200:20002/"
# location_IP = "192.168.68.51"
# element_file = "airmod_element_position_ROG5S_android11.json"
# data = None


# # connect HP server docker : docker exec -it 152634d9671a adb connect 192.168.150.103
# # http://192.168.150.200:20002/ --> ROG5S server
# # adb -s M8AIKN00D404KV9 tcpip 5555

# # Read json x & y element
# def test_element_position():
#     global data
#     with open(element_file, 'r') as obj:
#         data = json.load(obj)

# # Connect server
# def test_connect():
#     cmd = "curl -X GET '{server}connect?docker-id={ID}&location={IP}'".format(server=server_IP, ID=docker_id, IP=location_IP)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout
    
# # Install airmod
# def test_install_airmod():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}install_apk?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# ####################################################
# # funciton 1 - tap
# def tap(N, position):
#     time.sleep(0.5)
#     cmd = "curl -X GET '{server}tap?docker-id={ID}&x={x}&y={y}'".format(server=server_IP, ID=docker_id, x=data["cordinate"][N][position][0]["x"], y=data["cordinate"][N][position][0]["y"]) 
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 2 - screenshot
# def screenshot(task):
#     time.sleep(1)
#     cmd = "curl -X GET '{server}screenshot?docker-id={ID}&task={task}'".format(server=server_IP, ID=docker_id, task=task)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 3 - maskscreenshot
# def maskscreenshot(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}mask_screenshot?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 4 - maskscreenshot_maskspec
# def maskscreenshot_spec(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}mask_screenshot_recordplay?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 5 - maskscreenshot_maskoutspec
# def maskscreenshot_outspec(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}mask_screenshot_spec?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 6 - no_maskscreenshot
# def no_maskscreenshot(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}not_mask_screenshot?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 6 - contrast same
# def contrast_same(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}contrast_same?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 7 - contrast diff
# def contrast_diff(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}contrast_diff?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 8 - exit airmod
# def exit_airmod():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}apk_is_exit?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 9 - open airmod
# def open_airmod():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}open_airmod?docker-id={ID}&location={IP}'".format(server=server_IP, ID=docker_id, IP=location_IP)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 10 - pass 4 permission
# def pass_permission():
#     tap(0, "airmod_permission_first")
#     time.sleep(0.5)
#     tap(1, "airmod_permission_second")
#     time.sleep(0.5)
#     tap(2, "airmod_permission_third")
#     time.sleep(0.5)
#     tap(3, "airmod_permission_fourth")

# # function 11 - screenshot + mask + contrast same
# def contrast_same_golden(task):
#     screenshot(task)
#     maskscreenshot(task)
#     contrast_same(task)

# # function 12 - screenshot + mask_spec + contrast same
# def contrast_same_golden_outSpec(task):
#     screenshot(task)
#     maskscreenshot_spec(task)
#     contrast_same(task)

# # function 13 - screenshot + mask_outSpec + contrast same
# def contrast_same_golden_inSpec(task):
#     screenshot(task)
#     maskscreenshot_outspec(task)
#     contrast_same(task)

# # function 14 - screenshot + no_mask + contrast same
# def contrast_same_golden_nomask(task):
#     screenshot(task)
#     no_maskscreenshot(task)
#     contrast_same(task)

# # function 14 - screenshot + mask_outSpec + contrast same
# def contrast_diff_golden_inSpec(task):
#     screenshot(task)
#     maskscreenshot_outspec(task)
#     contrast_diff(task)

# # function 15 - check files
# def check_file(file_type, amount):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}check-file?docker-id={ID}&type={file_type}&count={N}&serial={tmp}'".format(server=server_IP, ID=docker_id, file_type=file_type, N=amount, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # function 16 - check audio duration
# def check_audio_duration(t):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}check-wav?docker-id={ID}&duration={t}&serial={tmp}'".format(server=server_IP, ID=docker_id, t=t, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout
    
# # function 17 - push audio to phone
# def push_audio():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}push_wavfolder?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 18 - keyevent
# def keyevent(key, count):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}keyevent?docker-id={ID}&keyevent={key}&count={count}'".format(server=server_IP, ID=docker_id, key=key, count=count)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 19 - input text
# def inputText(parameter):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}input_text?docker-id={ID}&text={P}'".format(server=server_IP, ID=docker_id, P=parameter)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 20 - input parameter for patient
# def inputParameter(parameter):
#     tap(45, "patient_all_input_parameter")
#     inputText(parameter)
#     tap(46, "patient_all_input_over")
#     tap(47, "patient_all_input_ok")

# # function 21 - swipe toolbars
# def swipe_toolbars():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}swipe_toolbars?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 22 - check event info
# def check_event_info():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}check-event?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 23 - check patient info
# def check_patient_info():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}check-patient?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 24 - pull screenrecord
# def pull_screenrecord():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}pull_screenrecord?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 25 - slice 30 piece/s
# def slice_piece():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}cutframe?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 26 - analyze yellow alert
# def analyze_with_yellow_alert():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}analyze_yellow?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     if b'failed' in p.stdout:
#         time.sleep(0.3)
#         cmd = "curl -X GET '{server}dump-log?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#         p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         #print(p.stdout)
#         assert b'failed' in p.stdout

#     else:
#         assert b'success' in p.stdout

# # function 27 - analyze without yellow alert
# def analyze_without_yellow_alert():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}analyze_none_yellow?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     if b'failed' in p.stdout:
#         time.sleep(0.3)
#         cmd = "curl -X GET '{server}dump-log?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#         p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         #print(p.stdout)
#         assert b'failed' in p.stdout

#     else:
#         assert b'success' in p.stdout

# # function 28 - analyze apnea alert
# def analyze_with_apnea_alert():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}analyze_apnea?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     if b'failed' in p.stdout:
#         time.sleep(0.3)
#         cmd = "curl -X GET '{server}dump-log?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#         p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         #print(p.stdout)
#         assert b'failed' in p.stdout

#     else:
#         assert b'success' in p.stdout


# # function 29 - analyze without apnea alert
# def analyze_without_apnea_alert():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}analyze_none_apnea?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     if b'failed' in p.stdout:
#         time.sleep(0.3)
#         cmd = "curl -X GET '{server}dump-log?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#         p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         #print(p.stdout)
#         assert b'failed' in p.stdout

#     else:
#         assert b'success' in p.stdout

# #function 30 - analyze with red alert
# def analyze_with_red_alert():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}analyze_red?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     if b'failed' in p.stdout:
#         time.sleep(0.3)
#         cmd = "curl -X GET '{server}dump-log?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#         p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         #print(p.stdout)
#         assert b'failed' in p.stdout

#     else:
#         assert b'success' in p.stdout

# # function 31 - mask_datetime
# def mask_datetime(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}mask_datetime?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 32 - contrast battery
# def contrast_battry(task):
#     screenshot(task)
#     mask_datetime(task)
#     contrast_same(task)

# # function 33 - battery level
# def battery_level():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}battery-level?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     return p.stdout

# # function 34 - battery set
# def battery_set(N):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}battery-set?docker-id={ID}&N={N}'".format(server=server_IP, ID=docker_id, N=N)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     #return p.stdout

# # function 35 - battery reset
# def battery_reset():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}battery-reset?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     #return p.stdout


# # function 36 - clean cutframe
# def clean_cutframe():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}clean_cutframe?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
    
# # function 37 - clean recordfolder
# def clean_recordfolder():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}clean_recordfolder?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 38 - clean screenrecord
# def clean_screenrecord():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}clean_screenrecord?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 39 - slide 
# def slide(direction):
#     time.sleep(0.3)
#     cmd = "curl -X GET 'http://{arm_ip}:8080/{d}'".format(arm_ip=arm_IP, d=direction)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)

# # function 40 - uninstall
# def uninstall():
#     time.sleep(1)
#     cmd = "curl -X GET '{server}uninstall_apk?docker-id={ID}&location={IP}'".format(server=server_IP, ID=docker_id, IP=location_IP)
#     p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
#     assert b'success' in p.stdout

# # function 41 - unlock screen
# def unlock_screen():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}unlock_screen?docker-id={ID}'".format(server=server_IP, ID=docker_id)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # function 42 - maskscreenshot_amp
# def maskscreenshot_amp(task):
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}mask_readallchannel_adjust_amp?task={task}&serial={tmp}'".format(server=server_IP, task=task, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # function 44 - pull data to local
# def pullData_toLocal():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}pull_dataToLocal?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # function 45 - unzip
# def unzip():
#     time.sleep(0.3)
#     cmd = "curl -X GET '{server}file_unzip?docker-id={ID}&serial={tmp}'".format(server=server_IP, ID=docker_id, tmp=serial_tmp)
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
# ############################################################
# # test 0 - open airmod and pass permission
# def test_open_airmod():
#     open_airmod()
#     pass_permission()
#     tap(254, "encryptPwd_input")
#     inputText("Zxcv1234@")
#     tap(46, "patient_all_input_over")
#     time.sleep(1)
#     tap(255, "encryptPwd_save")

# # test 1 - main screen
# def test_main_screen():
#     contrast_same_golden("main_screen")

#     # close AI and open record function
#     tap(43, "menu")
#     tap(108, "setting")
#     #tap(115, "setting_ai_enable")
#     tap(113, "setting_record_enable")
#     tap(112, "setting_back_main")

# # test 2 - button_menu
# def test_button_menu():
#     tap(43, "menu")
#     contrast_same_golden("button_menu")
#     tap(4, "buttonsilent")

# # test 3 - button_silent
# def test_button_silent():
#     tap(4, "buttonsilent")
#     contrast_same_golden("button_silent")
#     tap(4, "buttonsilent")

# # test 4 - battery of setting
# def test_button_battery():
#     A = battery_level()
#     battery_info = bytes.decode(A)
#     #print(battery_info)
#     #B = battery_info.split("\n")
#     #level = B[0].split(":")[1].strip()
#     #print(level)
#     if "100" in battery_info:
#         # test 100
#         battery_set("100")
#         time.sleep(1)
#         contrast_battry("battery_100_no_power")
#         # test 98
#         battery_set("98")
#         time.sleep(1)
#         contrast_battry("battery_98_no_power")
#         # test 79
#         battery_set("79")
#         time.sleep(1)
#         contrast_battry("battery_79_no_power")
#         # test 59
#         battery_set("59")
#         time.sleep(1)
#         contrast_battry("battery_59_no_power")
#         # test 49
#         battery_set("49")
#         time.sleep(1)
#         contrast_battry("battery_49_no_power")
#         # test 28
#         battery_set("28")
#         time.sleep(1)
#         contrast_battry("battery_28_no_power")
#         # test 19
#         battery_set("19")
#         time.sleep(1)
#         contrast_battry("battery_19_no_power")
#     else:
#         # test 100
#         battery_set("100")
#         time.sleep(1)
#         contrast_battry("battery_100_power")
#         # test 98
#         battery_set("98")
#         time.sleep(1)
#         contrast_battry("battery_98_power")
#         # test 79
#         battery_set("79")
#         time.sleep(1)
#         contrast_battry("battery_79_power")
#         # test 59
#         battery_set("59")
#         time.sleep(1)
#         contrast_battry("battery_59_power")
#         # test 49
#         battery_set("49")
#         time.sleep(1)
#         contrast_battry("battery_49_power")
#         # test 28
#         battery_set("28")
#         time.sleep(1)
#         contrast_battry("battery_28_power")
#         # test 19
#         battery_set("19")
#         time.sleep(1)
#         contrast_battry("battery_19_power")

#     battery_reset()

# # test 5 - button_exit
# def test_button_exit():
#     tap(6, "buttonexit")
#     time.sleep(0.5)
#     contrast_same_golden("button_exit")   
#     tap(8, "buttonexit_no")
#     time.sleep(0.5)
#     contrast_same_golden("button_exit_no")   

# # test 6 - button_exit_yes
# def test_airmod_is_exit():
#     tap(6, "buttonexit")
#     tap(7, "buttonexit_yes")
#     exit_airmod()
#     open_airmod()
#     tap(3, "airmod_permission_fourth")

# # test 7 - button_event
# def test_button_event():
#     tap(27, "button_event")
#     contrast_same_golden("button_event")
    
# # test 8 - button_event_PAO_TAO_Apnea
# def test_button_event_tag():
#     tap(247, "button_event_PAO")
#     #tap(248, "button_event_TAO")
#     #tap(249, "button_event_Apnea")
#     contrast_same_golden("button_event_tag")

# # test 9 - button_event_save
# def test_button_event_save():
#     tap(28, "button_event_save")
#     contrast_same_golden("button_event_save")

# # test 10 - button_screenlock
# def test_button_screenlock():
#     tap(26, "btnscreenlock")
#     contrast_same_golden("btnscreenlock")
#     tap(26, "btnscreenlock")

# # test 11 - button_soundoutput
# def test_button_soundoutput():
#     tap(39, "outputsoundmodel")
#     contrast_same_golden("button_soundoutput")

# # test 12 - button_soundoutput_Auto
# def test_button_soundoutput_auto():
#     tap(41, "auto")
#     contrast_same_golden("button_soundoutput_auto")

# # test 13 - button_soundoutput_Silent
# def test_button_soundoutput_silent():
#     tap(39, "outputsoundmodel")
#     tap(42, "silent")
#     contrast_same_golden("button_soundoutput_silent")

# # test 14 - button_soundoutput_Auto+Spk
# def test_button_soundoutput_autoSpk():
#     tap(39, "outputsoundmodel")
#     tap(40, "auto+spk")
#     contrast_same_golden("button_soundoutput_autospk")

# # test 15 - button_soundsetting
# def test_button_soundsetting():
#     tap(14, "buttonsoundsetting")
#     contrast_same_golden("button_soundsetting")

# # test 16 - button_soundsetting_HZbar
# def test_button_soundsetting_HZbar():
#     tap(16, "hz_rangeseekbar01")
#     contrast_same_golden("button_soundsetting_HZbar")

# # test 17 - button_soundsetting_resetDefault
# def test_button_soundsetting_resetDefault():
#     tap(22, "button_default")
#     contrast_same_golden("button_soundsetting_resetDefault")

# """
# # test 18 - button_soundsetting_checkboxenablepitch
# def test_button_soundsetting_checkboxenablepitch():
#     tap(17, "checkboxenablepitch")
#     contrast_same_golden("button_soundsetting_checkboxenablepitch")
#     tap(22, "button_default")

# # test 19 - button_soundsetting_pitchPitchseekbar1.0x
# def test_button_soundsetting_pitchPitchseekbar():
#     tap(18, "pitch_pitchseekbar1.0x")
#     contrast_same_golden("button_soundsetting_pitchPitchseekbar1.0x")
#     tap(22, "button_default")
# """

# # test 20 - button_soundsetting_spinnerbwe
# def test_button_soundsetting_spinnerbwe():
#     tap(19, "spinnerbwe")
#     contrast_same_golden("button_soundsetting_spinnerbwe")

# # test 21 - button_soundsetting_bweNormal
# def test_button_soundsetting_bweNormal():
#     tap(20, "bwe_normal")
#     contrast_same_golden("button_soundsetting_bweNormal")

# # test 22 - button_soundsetting_bweShift
# def test_button_soundsetting_bweShift():
#     tap(19, "spinnerbwe")
#     tap(21, "bwe_shift")
#     contrast_same_golden("button_soundsetting_bweShift")
#     tap(22, "button_default")

# # test 23 - button_soundsetting_confirm
# def test_button_soundsetting_confirm():
#     tap(15, "buttonsoundsetting_confirm")
#     contrast_same_golden("button_soundsetting_confirm")

# # test 24 - button_nc
# def test_button_nc():
#     tap(11, "spinnernoisecancel")
#     contrast_same_golden("button_nc")

# # test 25 - button_nc_normal
# def test_button_nc_normal():
#     tap(12, "nc_normal")
#     contrast_same_golden("button_nc_normal")

# # test 26 - button_nc_newdual
# def test_button_nc_newdual():
#     tap(11, "spinnernoisecancel")
#     tap(13, "nc_newdual")
#     contrast_same_golden("button_nc_newdual")

# # test 27 - button_freeze
# def test_button_freeze():
#     tap(10, "buttonfreeze")
#     contrast_same_golden("button_freeze")

# # test 28 - button_hidespec
# def test_button_hidespec():
#     tap(10, "buttonfreeze")
    
#     tap(43, "menu")
#     tap(44, "patient")
#     tap(112, "setting_back_main")
#     tap(9, "button_hidespec")
#     contrast_same_golden("button_hidespec")

# # test 29 - input patient info page 1 of menu 
# def test_patient_button_page1(): 
#     tap(9, "button_hidespec")
#     tap(43, "menu")
#     tap(44, "patient")
#     tap(48, "patient_id_parameter")
#     tap(45, "patient_all_input_parameter")
#     inputText("9487945")
#     tap(49, "patient_id_over")
#     tap(51, "patient_id_ok")
#     tap(52, "patient_birthday")
#     tap(53, "patient_birthday_set")
#     tap(54, "patient_recordplace")
#     inputParameter("Home")
#     contrast_same_golden_nomask("menu_patient_page1")
    
# # test 30 - input patient info page 2 of menu
# def test_patient_button_page2(): 
#     keyevent(20, 8)
#     tap(55, "patient_operator")
#     inputParameter("587")
#     tap(56, "patient_name")
#     inputParameter("123")
#     tap(57, "patient_bednumber")
#     inputParameter("C9")
#     tap(58, "patient_age")
#     inputParameter("87")
#     contrast_same_golden_nomask("menu_patient_page2")

# # test 31 - input patient info page 3 of menu
# def test_patient_button_page3(): 
#     keyevent(20, 12)
#     tap(59, "patient_gender")
#     tap(61, "patient_gender_female")
#     tap(63, "patient_height")
#     inputParameter("187")
#     tap(64, "patient_weight")
#     inputParameter("78")
#     tap(66, "patient_diagnose")
#     inputParameter("asthma")
#     contrast_same_golden_nomask("menu_patient_page3")

# # test 32 - input patient info page 4 of menu
# def test_patient_button_page4(): 
#     keyevent(20, 11)
#     tap(67, "patient_medicalhistory")
#     inputParameter("DM")
#     tap(68, "patient_treatmentorsurgery")
#     inputParameter("circumcision")
#     tap(69, "patient_bloodpressure")
#     tap(70, "patient_bloodpressure_systolicpressure")
#     #tap(45, "patient_all_input_parameter")
#     inputText("180")
#     tap(46, "patient_all_input_over")
#     tap(71, "patient_bloodpressure_diastolicpressure")
#     #tap(45, "patient_all_input_parameter")
#     inputText("120")
#     tap(46, "patient_all_input_over")
#     tap(73, "patient_bloodpressure_ok")
#     tap(74, "patient_heartrate")
#     inputParameter("220")
#     tap(75, "patient_spO2")
#     inputParameter("90")
#     contrast_same_golden_nomask("menu_patient_page4")

# # test 33 - input patient info page 5 of menu
# def test_patient_button_page5(): 
#     keyevent(20, 11)
#     tap(76, "patient_rr")
#     inputParameter("35")
#     tap(77, "patient_ventilationtype")
#     tap(82, "patient_ventilationtype_bipap")
#     tap(86, "patient_ventilationtype_ok")
#     tap(87, "patient_bodyposition")
#     tap(250, "patient_bodyposition_trachea")
#     tap(88, "patient_bodyposition_ok")
#     tap(89, "patient_breathingsoundprelabel")
#     tap(91, "patient_breathingsoundprelabel_wheeze")
#     tap(97, "patient_breathingsoundprelabel_ok")
#     contrast_same_golden_nomask("menu_patient_page5")

# # test 34 - input patient info page 6 of menu
# def test_patient_button_page6(): 
#     keyevent(20, 8)
#     tap(98, "patient_feedback")
#     inputParameter("poorAIC")
#     tap(99, "patient_Comment")
#     inputParameter("ok")
#     keyevent(20, 8)
#     tap(100, "patient_note")
#     inputParameter("testing")
#     contrast_same_golden_nomask("menu_patient_page6")

# # test 35 - button_recordplay_outspec
# def test_button_recordplay_outspec():
#     tap(112, "setting_back_main")
#     tap(23, "button_recordplay")
#     tap(24, "button_recordplay_ignore")
#     tap(25, "button_recordplay_skip")
#     contrast_same_golden_outSpec("button_recordplay")

# # test 36 - button_recordplay_spec
# def test_button_recordplay_diff_spec():
#     time.sleep(3)
#     tap(23, "button_recordplay")
#     time.sleep(0.5)
#     tap(253, "record_saving")
#     time.sleep(6)
#     contrast_diff_golden_inSpec("button_recordplay_spec")

# # test 37 - check zip and unzip under no relayboard
# def test_check_zipFile():
#     pullData_toLocal()
#     time.sleep(5)
#     unzip()   
#     check_file("zip", 1)

# # test 37 - event info
# def test_event_info():
#     check_event_info()

# # test 38 - patient info
# def test_patient_info():
#     check_patient_info()

# # test 39 - check files amount under no relayboard
# def test_check_files():
#     check_file("json", 1)    
#     check_file("wav", 1)    
#     check_file("txt", 0)    

# # test 40 - check audio duration -2 +2 sec
# def test_audio_duration():
#     check_audio_duration("11")


# # test 41 - Record(don't save file -->0)
# def test_record_unable():
#     clean_recordfolder()
#     tap(43, "menu")
#     tap(108, "setting")
#     tap(113, "setting_record_enable")
#     tap(112, "setting_back_main")
#     tap(23, "button_recordplay")
#     #tap(24, "button_recordplay_ignore")
#     tap(25, "button_recordplay_skip")
#     time.sleep(0.5)
#     tap(23, "button_recordplay")
#     time.sleep(0.5)
#     pullData_toLocal()
#     time.sleep(0.5)
#     check_file("zip", 0)    
#     check_file("json", 0)    
#     check_file("wav", 0)    
#     check_file("txt", 0)    
#     tap(43, "menu")
#     tap(108, "setting")
#     tap(113, "setting_record_enable")

# # test 42 - Read all channel
# def test_read_all_channel():
#     tap(114, "setting_readallchannel_enable")
#     tap(112, "setting_back_main")
#     contrast_same_golden("button_ch1")
#     tap(29, "button_channel")
#     contrast_same_golden("button_all_channel")
#     tap(30, "button_ch2")
#     contrast_same_golden("button_ch2")
#     tap(29, "button_channel")
#     tap(31, "button_ch3")
#     contrast_same_golden("button_ch3")
#     tap(29, "button_channel")
#     tap(32, "button_ch4")
#     contrast_same_golden("button_ch4")
#     tap(29, "button_channel")
#     tap(33, "button_ch1")
#     contrast_same_golden("button_ch1")
 
# # test 43 - hide event record UI of setting(contrast pic)
# def test_hide_event_record():
#     tap(43, "menu")
#     tap(108, "setting")
#     tap(114, "setting_readallchannel_enable")
#     #keyevent(20, 13)
#     keyevent(20, 14)
#     tap(235, "about")
#     #tap(232, "setting_system_resettodefault")
#     tap(112, "setting_back_main")
#     contrast_same_golden("button_no_record_event")

# # test 44 - hide recording UI of setting(contrast pic)
# def test_close_recording_button():
#     tap(43, "menu")
#     tap(108, "setting")
#     #tap(114, "setting_readallchannel_enable")
#     keyevent(20, 14)
#     tap(235, "about")
#     tap(232, "setting_system_resettodefault")
#     tap(112, "setting_back_main")
#     tap(35, "button_recording")
#     contrast_same_golden("button_close_recording")
#     time.sleep(1)
#     tap(23, "button_recordplay")
#     tap(25, "button_recordplay_skip")
#     time.sleep(0.5)
#     tap(23, "button_recordplay")
#     time.sleep(0.5)
#     pullData_toLocal()
#     time.sleep(0.5)
#     check_file("zip", 0)    
#     check_file("json", 0)    
#     check_file("wav", 0)    
#     check_file("txt", 0)    

# # test 45 - button recording and enable record UI of setting(check files)
# def test_open_recording_button():
#     tap(43, "menu")
#     tap(108, "setting")
#     tap(112, "setting_back_main")
    
#     tap(35, "button_recording")
#     contrast_same_golden("button_open_recording")
#     time.sleep(1)
#     tap(23, "button_recordplay")
#     tap(25, "button_recordplay_skip")
#     time.sleep(0.5)
#     tap(23, "button_recordplay")
#     time.sleep(0.5)
#     tap(253, "record_saving")
#     time.sleep(6)
#     time.sleep(0.5)
#     pullData_toLocal()
#     time.sleep(0.5)
#     unzip()   
#     time.sleep(0.5)
#     check_file("zip", 1)    
#     check_file("json", 1)    
#     check_file("wav", 1)    
#     check_file("txt", 0)

# # test 46 - spectrogram UI of setting(contrast pic)
# def test_change_spec_UI():
#     push_audio()
#     tap(43, "menu")
#     tap(108, "setting")
#     #keyevent(20, 18)
#     keyevent(20, 17)
#     tap(114, "setting_readallchannel_enable")
#     tap(235, "about")
#     contrast_same_golden_nomask("setting_ui_spectrogram")
#     tap(161, "setting_ui_spectrogram_purple")
#     tap(112, "setting_back_main")
#     tap(43, "menu")
#     tap(101, "archive")
#     tap(251, "archive_publicLocation")
#     tap(103, "archive_1000_test")
#     tap(105, "archive_test_spec")
#     time.sleep(18)
#     contrast_same_golden_inSpec("setting_change_ui_spec_purple")

# # test 47 - screen time range 15-->1599s UI of setting(contrast pic)
# def test_screen_time_range():
#     tap(43, "menu")
#     tap(108, "setting")
#     #keyevent(20, 18)
#     keyevent(20, 17)
#     tap(235, "about")
#     tap(159, "setting_ui_spectrogram_red")
#     tap(232, "setting_system_resettodefault")
#     inputParameter("99")
#     tap(112, "setting_back_main")
#     contrast_same_golden("menu_screentime_1599")
    
#     tap(43, "menu")
#     tap(108, "setting")
#     #keyevent(20, 18)
#     keyevent(20, 17)
#     tap(232, "setting_system_resettodefault")
#     tap(45, "patient_all_input_parameter")
#     tap(241, "system_screenrecord")
    
#     keyevent(67, 2)
#     tap(46, "patient_all_input_over")
#     tap(47, "patient_all_input_ok")
#     tap(112, "setting_back_main")


# # test 48 - archive
# def test_archive():
#     time.sleep(5)
#     tap(43, "menu")
#     tap(101, "archive")
#     tap(251, "archive_publicLocation")
#     tap(103, "archive_1000_test")
#     tap(105, "archive_test_spec")
#     time.sleep(5)
#     contrast_same_golden_outSpec("main_archive_outSpec")
#     time.sleep(10)
#     contrast_same_golden_inSpec("menu_archive_spec")


# # test 49 - main of about
# def test_menu_about():
#     clean_recordfolder()
#     tap(43, "menu")
#     tap(235, "about")
#     contrast_same_golden_nomask("menu_about")

# # test 50 - Private policy of about 
# def test_menu_about_privatePolicy():
#     tap(237, "about_button_privatepolicy")
#     contrast_same_golden_nomask("about_privatepolicy_page1")
#     keyevent(20, 3)
#     contrast_same_golden_nomask("about_privatepolicy_page2")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_privatepolicy_page3")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_privatepolicy_page4")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_privatepolicy_page5")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_privatepolicy_page6")
#     keyevent(20, 1)
#     contrast_same_golden_nomask("about_privatepolicy_page7")

# # test 51 - Terms of Use aobut
# def test_menu_about_termsofUse():
#     tap(238, "about_button_privatepolicy_ok")
#     tap(239, "about_button_termsofuse")
#     contrast_same_golden_nomask("about_termsofuse_page1")
#     keyevent(20, 3)
#     contrast_same_golden_nomask("about_termsofuse_page2")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_termsofuse_page3")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_termsofuse_page4")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_termsofuse_page5")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_termsofuse_page6")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_termsofuse_page7")
#     keyevent(20, 2)
#     contrast_same_golden_nomask("about_termsofuse_page8")
#     keyevent(20, 1)
#     contrast_same_golden_nomask("about_termsofuse_page9")

#     tap(240, "about_button_termsofuse_ok")
#     tap(236, "about_back_main")
# """
# # test 52 - button ai alarm
# def test_button_ai_alarm():
#     tap(43, "menu")
#     tap(108, "setting")
#     #tap(115, "setting_ai_enable")
#     keyevent(20, 30)
#     tap(182, "setting_alarm_yellowalert")
#     tap(181, "setting_alarm_apneaautorestart")
#     tap(45, "patient_all_input_parameter")
#     #time.sleep(2)
#     tap(241, "system_screenrecord")
#     keyevent(67, 3)
#     inputText("3")
#     tap(46, "patient_all_input_over")
#     tap(47, "patient_all_input_ok")
#     tap(112, "setting_back_main")
#     contrast_same_golden("button_ai_alarm")

# # test 53 - auto restart 20-->3s alarm of setting(contrast pic)
# def test_alarm_auto_restart():
#     tap(5, "buttonalarm")
#     contrast_same_golden("button_alarm_close")
#     time.sleep(3)
#     contrast_same_golden("button_alarm_open")

# # test 54 - RR show 9 bpm
# def test_RR_spec():
#     tap(43, "menu")
#     tap(101, "archive")
#     tap(103, "archive_1000_test")
#     tap(106, "RR9_27s_sample")
#     time.sleep(27.5)
#     screenshot("spec_RR")
#     maskscreenshot_amp("spec_RR")
#     contrast_same("spec_RR")
    
#     #contrast_same_golden("spec_RR")

# # test 55 - AI and yellow alert
# def test_AI_with_yellow_alert():
#     #tap(6, "buttonexit")
#     #tap(7, "buttonexit_yes")
#     swipe_toolbars()
#     swipe_toolbars()
#     swipe_toolbars()
#     tap(241, "system_screenrecord")
#     time.sleep(3)
#     tap(43, "menu")
#     tap(101, "archive")
#     tap(103, "archive_1000_test")
#     tap(104, "archive_1000_test_audiosample")
#     time.sleep(25)
#     keyevent(26, 1)
#     keyevent(26, 1)
#     unlock_screen()
#     pull_screenrecord()
#     slice_piece()
#     analyze_with_yellow_alert()

# # test 56 - AI with apnea alert
# def test_AI_with_apnea_alert():
#     analyze_with_apnea_alert()
#     clean_cutframe()

# # test 57 - white 15 --> 30s alarm of setting (no show white box)
# def test_AI_with_prolong_white_alert():
#     tap(43, "menu")
#     tap(108, "setting")
#     keyevent(20, 26)
#     tap(178, "setting_alarm_apneaalarmwhitebox")
#     inputParameter("1")
#     tap(179, "setting_alarm_apneaalarmredbox")
#     tap(45, "patient_all_input_parameter")
#     tap(241, "system_screenrecord")
#     keyevent(67, 2)
#     inputText("5")
#     tap(46, "patient_all_input_over")
#     tap(47, "patient_all_input_ok")
#     tap(112, "setting_back_main")
#     swipe_toolbars()
#     swipe_toolbars()
#     swipe_toolbars()
#     tap(241, "system_screenrecord")
#     time.sleep(3)
#     tap(43, "menu")
#     tap(101, "archive")
#     tap(103, "archive_1000_test")
#     tap(104, "archive_1000_test_audiosample")
#     time.sleep(25)
#     keyevent(26, 1)
#     keyevent(26, 1)
#     unlock_screen()
#     pull_screenrecord()
#     slice_piece()
#     analyze_without_apnea_alert()

# # test 58 - red 30 -->10s alarm of setting(show red box)
# def test_AI_with_red_alert():
#     analyze_with_red_alert()

# # test 59 - AI without yellow alert
# def test_AI_without_yellow_alert():
#     clean_cutframe()
#     tap(43, "menu")
#     tap(108, "setting")
#     #tap(115, "setting_ai_enable")
#     tap(112, "setting_back_main")
#     swipe_toolbars()
#     swipe_toolbars()
#     swipe_toolbars()
#     tap(241, "system_screenrecord")
#     time.sleep(3)
    
#     tap(43, "menu")
#     tap(101, "archive")
#     tap(103, "archive_1000_test")
#     tap(104, "archive_1000_test_audiosample")
#     time.sleep(25)
#     keyevent(26, 1)
#     keyevent(26, 1)
#     unlock_screen()
#     pull_screenrecord()
#     slice_piece()
#     analyze_without_yellow_alert()

# # test 60 - AI without apnea alert
# def test_AI_without_apnea_alert():
#     analyze_without_apnea_alert()
# """
# # test 61 - reset to default of setting
# def test_cleanData_resetSetting():
#     clean_cutframe()
#     clean_screenrecord()
#     clean_recordfolder()
#     tap(43, "menu")
#     tap(108, "setting")
#     keyevent(20, 36)
#     tap(232, "setting_system_resettodefault")
#     tap(234, "setting_system_resettodefault_ok")
#     tap(3, "airmod_permission_fourth")
#     time.sleep(0.5)
#     tap(254, "encryptPwd_input")
#     inputText("Zxcv1234@")
#     tap(46, "patient_all_input_over")
#     time.sleep(0.5)
#     tap(255, "encryptPwd_save")
#     time.sleep(0.5)
#     # close AI and open record function
#     tap(43, "menu")
#     tap(108, "setting")
#     #tap(115, "setting_ai_enable")
#     tap(113, "setting_record_enable")
#     tap(112, "setting_back_main")

# # test 62 - connect relay board by slide 
# def test_view_rbconnecting():
#     slide("forward")
#     time.sleep(3)
#     tap(244, "system_rb_connect_confirm")
#     time.sleep(1)
#     contrast_same_golden("view_reconnecting")

# # test 63 - test one channel record and file
# def test_one_channel_data():
#     tap(23, "button_recordplay")
#     tap(25, "button_recordplay_skip")
#     time.sleep(5)
#     tap(23, "button_recordplay")
#     time.sleep(0.5)
#     tap(253, "record_saving")
#     time.sleep(6)
#     time.sleep(1)
#     #screenshot("spec_amp")
#     #maskscreenshot_amp("spec_amp")
#     #contrast_same("spec_amp")
#     time.sleep(0.5)
#     pullData_toLocal()
#     time.sleep(0.5)
#     unzip()   
#     time.sleep(0.5)

#     check_file("json", 3)    
#     check_file("wav", 3)    
#     check_file("txt", 1)    

# # test 64 - test four channel record and file
# def test_four_channel_data():
#     clean_recordfolder()
#     time.sleep(3)
#     tap(43, "menu")
#     tap(108, "setting")
#     tap(114, "setting_readallchannel_enable")
#     tap(112, "setting_back_main")
#     time.sleep(3)
#     tap(23, "button_recordplay")
#     time.sleep(1)
#     tap(25, "button_recordplay_skip")
#     time.sleep(2)
#     screenshot("spec_amp")
#     maskscreenshot_amp("spec_amp")
#     contrast_same("spec_amp")
#     time.sleep(4.5)
#     tap(23, "button_recordplay")
#     time.sleep(0.5)
#     tap(253, "record_saving")
#     time.sleep(6)
#     time.sleep(2)
#     pullData_toLocal()
#     time.sleep(0.5)
#     unzip()   
#     time.sleep(0.5)
#     check_file("json", 12)    
#     check_file("wav", 12)    
#     check_file("txt", 1)    

# # test last - remove airmod 
# def test_uninstall():
#     clean_recordfolder()
#     slide("backward")
#     uninstall()


