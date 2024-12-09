# #-*- coding:utf-8 -*-

# import datetime
# import os
# import platform
# import re
# import time
# #from .utils import
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# from PIL import ImageChops
# from PIL import ImageEnhance
# import pytest
# import subprocess

# #20210603 modify
# #docker appium/appium111 80a447b611ac--> appium/appium109 601e38e3ca19
# #serial=111 -->serial=109
# #install apk add serial=109

# # 第一步 - connect docker
#     #Eru 裡下 docker exec -it 601e38e3ca19 adb connect 192.168.150.100

# # 第二步 - connect server 
# def test_connect():
#     cmd = "curl -X GET 'http://192.168.150.200:20000/connect?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
   
# # 第三步 - install airmod
# def test_install_airmod():
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/install_apk?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
#     # 點擊確認安裝
#     #time.sleep(3)
#     #cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=296&y=2097'"
#     #p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #print(p.stdout)
    
# # 第四步 - open airmod
# def test_open_airmod():
#     #os.system("cural -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'")
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 第五步 - dump_log
# #def dump_log():
#     #os.system("curl -X GET 'http://192.168.150.200:20000/dump-log?docker-id=601e38e3ca19&location=192.168.150.100'")

# # 第六步 - pass permission
# def test_pass_permission():
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=558&y=492'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(0.5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=558&y=570'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(0.5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=558&y=530'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     time.sleep(0.5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - main_screen
# def test_main_screen():
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=main_screen'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_menu
# def test_button_menu():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_menu'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_menu&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
   
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_menu&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1711&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_silent 
# def test_button_silent():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1711&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_silent'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_silent&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
   
#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_silent&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1711&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_exit
# def test_button_exit():
#     # 點位置
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2202&y=58'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)

#     # 點no
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_exit_no'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_exit_no&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #判斷exit yes 是不是回到android desktop
# def test_apk_is_exit():
#     # 點button exit
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2202&y=58'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點button exit yes
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # check apk is exit and show android desktop
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/apk_is_exit?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 打開回airmod
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # permisson pass
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_event 
# def test_button_event():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2179&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_event'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_event&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_event&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點save
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1667&y=713'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_event_save'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_event_save&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_screenlock 
# def test_button_screenlock():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2042&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_screenlock'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_screenlock&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_screenlock&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 回main_screen
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2042&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_soundoutput
# def test_button_soundoutput():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1844&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_soundoutput'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_soundoutput&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_soundoutput&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置auto
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1864&y=741'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_soundoutput_auto'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_soundoutput_auto&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_soundoutput_auto&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1844&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置silent
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1864&y=838'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_soundoutput_silent'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_soundoutput_silent&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_soundoutput_silent&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1844&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置auto+spk
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1864&y=644'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_soundoutput_autospk'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_soundoutput_autospk&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - view_not_rbconnecting
# def test_view_not_rbconnecting():
#     # 截圖
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=view_not_rbconnecting'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=view_not_rbconnecting&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=view_not_rbconnecting&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_soundsetting
# def test_button_soundsetting():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=707&y=918'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_soundsetting'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_soundsetting&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_soundsetting&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點confirm
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1207&y=821'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_soundsetting_confirm'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_soundsetting_confirm&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_nc 
# def test_button_nc():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=487&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_nc'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_nc&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_nc&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點normal
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=517&y=741'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_nc_normal'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_nc_normal&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_nc_normal&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=487&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點newdual
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=517&y=838'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_nc_newdual'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_nc_newdual&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_freeze 
# def test_button_freeze():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=246&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_freeze'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_freeze&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_freeze&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=246&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button hidespec 
# def test_button_hidespec():
#     # 點位置
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_hidespec'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=button_hidespec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_hidespec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點位置
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=934'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 清空今日資料夾
# def test_clean_recordfolder():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_recordfolder?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - button_recordplay (排後面檢測 因為頻譜會改變）
# def test_button_recordplay():
#     # 點recordplay
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 點skip
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1217&y=645'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_recordplay'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 (遮住頻譜）
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_recordplay?task=button_recordplay&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_recordplay&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點recordplay
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=button_recordplay_spec&s=100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋頻譜以外
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_spec?task=button_recordplay_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對main_screen是否不同！！！！
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_diff?task=button_recordplay_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - 檔案數
# def test_check_file():
#     # 檢測json 檔案數 1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=json&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測wav 檔案數 1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=wav&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測txt 檔案數 1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=txt&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - 音檔長度 -2 +2sec
# def test_wav_duration():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-wav?docker-id=601e38e3ca19&serial=109&duration=14'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 清空今日資料夾
# def test_clean_recordfolder():
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_recordfolder?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout


# # 檢測 - 檔案數
# def test_check_file_after_clean_recordfolder():
#     # 檢測json 檔案數 0
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=json&count=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測wav 檔案數 0
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=wav&count=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測txt 檔案數 0
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=txt&count=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - archive 與 頻譜畫圖 
# def test_archive():
#     # 塞音檔folder進去
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/push_wavfolder?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊menu
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊archive
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=468'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊至goldensample音檔 等待15秒
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=468'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_archive_mainscreen'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 (遮住頻譜）
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_recordplay?task=menu_archive_mainscreen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=button_recordplay&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 截圖
#     time.sleep(10)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_archive_spec'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋頻譜以外
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_archive_spec?task=menu_archive_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_archive_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - AI and yellow alert
# def test_AI_with_yellow_alert():
#     # 點擊menu
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊settings
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=612'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 點擊打開AI
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=808'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 往下滑
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=30'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊打開yellow alert
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=808'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 返回main_screen
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 跳出airmod 點button exit
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2202&y=58'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點button exit yes
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空screenrecord
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 下滑兩次跳出工具列
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=680&y=540'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 開啟airmod
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # permission pass
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊menu
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊archive
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=468'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊至goldensample音檔 等待30秒
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
#     time.sleep(30)

#     # 關閉螢幕
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=26&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 打開螢幕 上滑解鎖
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/unlock_screen?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 關掉螢幕錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2000'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 打開airmod
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # permission pass
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 拉出螢幕錄影檔
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/pull_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 切成30片
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 分析yellow alert
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/analyze_yellow?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空cutframe
#     time.sleep(10)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 分析apnea
# def test_AI_with_apnea():
#     # 跳出airmod 點button exit
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2202&y=58'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點button exit yes
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空screenrecord
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 下滑兩次跳出工具列
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=680&y=540'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 開啟airmod
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # permission pass
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊menu
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊archive
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=468'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊至goldensample音檔 等待30秒
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
#     time.sleep(30)

#     # 關閉螢幕
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=26&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 打開螢幕 上滑解鎖
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/unlock_screen?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 關掉螢幕錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2000'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 打開airmod
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # permission pass
#     time.sleep(0.5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 拉出螢幕錄影檔
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/pull_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 切成30片
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 分析apnea alert
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/analyze_apnea?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空cutframe
#     time.sleep(10)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 關閉yellow 有無出現
# def test_AI_without_yellow_alert():
#     # 點擊menu
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊settings
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=612'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 往下滑
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=30'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊關閉yellow alert
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=808'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 返回main_screen
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 跳出airmod 點button exit
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2202&y=58'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點button exit yes
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空screenrecord
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 下滑兩次跳出工具列
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=680&y=540'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 開啟airmod
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # permission pass
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊menu
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊archive
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=468'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊至goldensample音檔 等待30秒
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
#     time.sleep(30)

#     # 關閉螢幕
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=26&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 打開螢幕 上滑解鎖
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/unlock_screen?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 關掉螢幕錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2000'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 打開airmod
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # permission pass
#     time.sleep(0.5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 拉出螢幕錄影檔
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/pull_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 切成30片
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 分析no yellow alert
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/analyze_none_yellow?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空cutframe
#     time.sleep(10)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 關閉AI 有無出現 apnea
# def test_close_AI_without_apnea():
#     # 點擊menu
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊settings
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=612'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊關閉AI
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=808'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 返回main_screen
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
 
#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_closeai'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=menu_setting_closeai&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)

#     # 跳出airmod 點button exit
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=2202&y=58'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點button exit yes
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空screenrecord
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 下滑兩次跳出工具列
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/swipe_toolbars?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=680&y=540'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 開啟airmod
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # permission pass
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊menu
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊archive
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=468'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊至goldensample音檔 等待30秒
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=380'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
#     time.sleep(30)

#     # 關閉螢幕
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=26&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 打開螢幕 上滑解鎖
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/unlock_screen?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 關掉螢幕錄影
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1010&y=2000'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 打開airmod
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/open_airmod?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # permission pass
#     time.sleep(0.5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1472&y=613'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 拉出螢幕錄影檔
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/pull_screenrecord?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 切成30片
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 分析沒有apnea
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/analyze_none_apnea?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清空cutframe
#     time.sleep(10)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_cutframe?docker-id=601e38e3ca19&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 測試about頁面是否相同
# def test_menu_about():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=756'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?task=about&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 測試about_privatepolicy頁面是否相同
# def test_menu_about_privatepolicy():
#     # 檢驗 - Private policy page1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1056&y=453'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - Private policy page2 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - Private policy page3
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - Private policy page4
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - Private policy page5
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - Private policy page6
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout


#     # 檢驗 - Private policy page7
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - Private policy page8
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_privatepolicy_page8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_privatepolicy_page8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_privatepolicy_page8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=855'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 測試about_termsofus頁面是否相同
# def test_menu_about_termsofus():
#     # 檢驗 - terms of us page1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1060&y=563'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - terms of us page2 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢驗 - terms of us page3
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout


#     # 檢驗 - terms of us page4
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout


#    # 檢驗 - terms of us page5
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#    # 檢驗 - terms of us page6
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#    # 檢驗 - terms of us page7
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#    # 檢驗 - terms of us page8
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#    # 檢驗 - terms of us page9
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page9'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page9'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#    # 檢驗 - terms of us page10
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page10'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page10'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page10&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#    # 檢驗 - terms of us page11
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_termsofus_page11'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/not_mask_screenshot?serial=109&task=about_termsofus_page11'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=about_termsofus_page11&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout


# # 檢測 - aobut 回主畫面
# def test_menu_about_back_main():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=855'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=about_back_main'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=about_back_main&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - view_rbconnecting
# def test_view_rbconnecting():
#     time.sleep(2)
#     # 操控滑軌往前 連接ralayboard
#     cmd = "curl -X GET 'http://192.168.150.180:8080/forward'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'forward' in p.stdout

#     # 點擊 打勾以後都不用連接確認
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=700&y=500'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊連接確認
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1740&y=770'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=view_rbconnecting'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=view_rbconnecting&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=view_rbconnecting&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
#     time.sleep(2)

# # 檢測 - 開啟read all channel 圖示
# def test_read_all_channel_screen():
#     # 點擊menu
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊settings
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=612'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊real all channel
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=434'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊back 返回main_screen
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=main_screen_readallchannel_ch1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=main_screen_readallchannel_ch1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen_readallchannel_ch1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ch1 開啟mutiple ch
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1478&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=main_screen_readallchannel_mutiple'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot?task=main_screen_readallchannel_mutiple&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=main_screen_readallchannel_mutiple&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ch2
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1508&y=644'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊recordplay
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點skip
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1217&y=645'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - four channels ch2 頻譜是否有變化
# def test_realallchannel_ch2_spec():
#     # 截圖比對 ch2一樣 
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(1)
#     # 遮蓋 (遮住頻譜）
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_recordplay?task=menu_setting_readallchannel_ch2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_readallchannel_ch2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對spec 是否有變
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch2_spec'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋頻譜以外
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_spec?task=menu_setting_readallchannel_ch2_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(3)
#     # 比對main_screen是否不同！！
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_diff?task=menu_setting_readallchannel_ch2_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - four channels ch3 頻譜是否有變化
# def test_realallchannel_ch3_spec():
#     # 點擊 ch2 開啟mutiple ch
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1478&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ch3
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1508&y=741'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對 ch3一樣 
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 (遮住頻譜）
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_recordplay?task=menu_setting_readallchannel_ch3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_readallchannel_ch3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對spec 是否有變
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch3_spec'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋頻譜以外
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_spec?task=menu_setting_readallchannel_ch3_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對main_screen是否不同！！
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_diff?task=menu_setting_readallchannel_ch3_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - four channels ch4 頻譜是否有變化
# def test_realallchannel_ch4_spec():
#     # 點擊 ch3 開啟mutiple ch
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1478&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ch4
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1508&y=838'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對 ch4一樣 
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 (遮住頻譜）
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_recordplay?task=menu_setting_readallchannel_ch4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_readallchannel_ch4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對spec 是否有變
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch4_spec'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋頻譜以外
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_spec?task=menu_setting_readallchannel_ch4_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對main_screen是否不同！！
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_diff?task=menu_setting_readallchannel_ch4_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - four channels ch1 頻譜是否有變化
# def test_realallchannel_ch1_spec():
#     # 點擊 ch4 開啟mutiple ch
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1478&y=935'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ch1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1508&y=547'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對 ch1一樣 
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 (遮住頻譜）
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_recordplay?task=menu_setting_readallchannel_ch1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_readallchannel_ch1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖比對spec 是否有變
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_readallchannel_ch1_spec'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋頻譜以外
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_screenshot_spec?task=menu_setting_readallchannel_ch1_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對main_screen是否不同！！
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_diff?task=menu_setting_readallchannel_ch1_spec&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 點擊recordplay
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # clean recoder
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_recordfolder?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - 音檔數
# def test_realallchannel_file_count():
#     # 錄10秒  點擊recordplay
#     time.sleep(10)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點skip
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1217&y=645'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 停止錄製
#     time.sleep(7)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測json 檔案數 12
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=json&count=12'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測wav 檔案數 12
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=wav&count=12'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 檢測txt 檔案數 1
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check-file?docker-id=601e38e3ca19&type=txt&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - 音檔長度 (應該ch1-4都要測）
# def test_realallchannel_file_duration():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/check_wav_fourchannel?docker-id=601e38e3ca19&serial=109&duration=10'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # clean recoder
#     time.sleep(8)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_recordfolder?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測 - 調整時間軸
# def test_adjust_screen_time():
#     # 點擊 menu
#     time.sleep(8)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 setting
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=612'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 下滑至screen time range 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 screen time range
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=808'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 輸入參數
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=613&y=459'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 輸入參數999  adb shell input text "999"
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/input_text?docker-id=601e38e3ca19&text=999'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 確認參數 adb shell input keyevent 66
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=66&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ok adb shell input tap 1648 602
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=602'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 back 回main screen
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_screentimerange_9915'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_screentimerange_9915&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_screentimerange_9915&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp1 up
# def test_setting_ch1_amp1_up():
#     # 點擊 recordplay
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 skip
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1217&y=645'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 1
#     time.sleep(4)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp2 up
# def test_setting_ch1_amp2_up():
#     # 自動手臂 點擊 +amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp3 up
# def test_setting_ch1_amp3_up():
#     # 自動手臂 點擊 +amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp4 up
# def test_setting_ch1_amp4_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp5 up
# def test_setting_ch1_amp5_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp6 up
# def test_setting_ch1_amp6_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp7 up
# def test_setting_ch1_amp7_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp8 up
# def test_setting_ch1_amp8_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp9 up
# def test_setting_ch1_amp9_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 9
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp9'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp8 down
# def test_setting_ch1_amp8_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch1 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp7 down
# def test_setting_ch1_amp7_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp6 down
# def test_setting_ch1_amp6_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch1 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp5 down
# def test_setting_ch1_amp5_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch1 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp4 down
# def test_setting_ch1_amp4_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch1 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp3 down
# def test_setting_ch1_amp3_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp2 down
# def test_setting_ch1_amp2_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch1 amp1 down
# def test_setting_ch1_amp1_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch1 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch1_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch1_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch1_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp1 up
# def test_setting_ch2_amp1_up():
#     # 自動手臂 點擊 changechannel  
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/changechannel'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'changechannel' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 1
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp2 up
# def test_setting_ch2_amp2_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp3 up
# def test_setting_ch2_amp3_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp4 up
# def test_setting_ch2_amp4_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp5 up
# def test_setting_ch2_amp5_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp6 up
# def test_setting_ch2_amp6_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp7 up
# def test_setting_ch2_amp7_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp8 up
# def test_setting_ch2_amp8_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp9 up
# def test_setting_ch2_amp9_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 9
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp9'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp8 down
# def test_setting_ch2_amp8_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch2 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp7 down
# def test_setting_ch2_amp7_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp6 down
# def test_setting_ch2_amp6_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch2 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp5 down
# def test_setting_ch2_amp5_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch2 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp4 down
# def test_setting_ch2_amp4_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch2 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp3 down
# def test_setting_ch2_amp3_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp2 down
# def test_setting_ch2_amp2_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch2 amp1 down
# def test_setting_ch2_amp1_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch2 amp 1
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch2_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch2_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch2_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp1 up
# def test_setting_ch3_amp1_up():
#     # 自動手臂 點擊 changechannel  
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/changechannel'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'changechannel' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 1
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp2 up
# def test_setting_ch3_amp2_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp3 up
# def test_setting_ch3_amp3_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp4 up
# def test_setting_ch3_amp4_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp5 up
# def test_setting_ch3_amp5_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp6 up
# def test_setting_ch3_amp6_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp7 up
# def test_setting_ch3_amp7_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp8 up
# def test_setting_ch3_amp8_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp9 up
# def test_setting_ch3_amp9_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 9
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp9'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp8 down
# def test_setting_ch3_amp8_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch3 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp7 down
# def test_setting_ch3_amp7_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout


# #檢測 - ch3 amp6 down
# def test_setting_ch3_amp6_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch3 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp5 down
# def test_setting_ch3_amp5_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch3 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp4 down
# def test_setting_ch3_amp4_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch3 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp3 down
# def test_setting_ch3_amp3_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp2 down
# def test_setting_ch3_amp2_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch3 amp1 down
# def test_setting_ch3_amp1_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch3 amp 1
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch3_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch3_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch3_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp1 up
# def test_setting_ch4_amp1_up():
#     # 自動手臂 點擊 changechannel  
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/changechannel'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'changechannel' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 1
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp2 up
# def test_setting_ch4_amp2_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp3 up
# def test_setting_ch4_amp3_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp4 up
# def test_setting_ch4_amp4_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp5 up
# def test_setting_ch4_amp5_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp6 up
# def test_setting_ch4_amp6_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp7 up
# def test_setting_ch4_amp7_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp8 up
# def test_setting_ch4_amp8_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp9 up
# def test_setting_ch4_amp9_up():
#     # 自動手臂 點擊 +amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/increaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'increaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 9
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp9'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
    
#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp9&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp8 down
# def test_setting_ch4_amp8_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch4 amp 8
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp8'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp8&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp7 down
# def test_setting_ch4_amp7_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 7
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp7'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp7&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp6 down
# def test_setting_ch4_amp6_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch4 amp 6
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp6'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp6&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp5 down
# def test_setting_ch4_amp5_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch4 amp 5
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp5'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp5&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp4 down
# def test_setting_ch4_amp4_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout
    
#     # 截圖 遮蓋 比對 ch4 amp 4
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp4'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp4&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp3 down
# def test_setting_ch4_amp3_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 3
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp3&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp2 down
# def test_setting_ch4_amp2_down():
#     # 自動手臂 點擊 -amp
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 2
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp2'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp2&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# #檢測 - ch4 amp1 down
# def test_setting_ch4_amp1_down():
#     # 自動手臂 點擊 -amp 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/decreaseamp'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'decreaseAmp' in p.stdout

#     # 截圖 遮蓋 比對 ch4 amp 1
#     time.sleep(5)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/screenshot?docker-id=601e38e3ca19&task=menu_setting_ch4_amp1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 遮蓋 new
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/mask_readallchannel_adjust_amp?task=menu_setting_ch4_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 比對是否相同
#     time.sleep(3)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/contrast_same?task=menu_setting_ch4_amp1&serial=109'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout







# # 檢測完 - 關掉real all channel / screen time adjust to origin 15s
# def test_close_realallchannel():
#     # 自動手臂 點擊 changechannel
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.180:8181/changechannel'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'changechannel' in p.stdout

#     # 點擊 recordplay 關閉錄音
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1131&y=909'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊menu
#     time.sleep(1)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=119&y=50'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊settings
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=612'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 關閉real all channel
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=434'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 下滑至screen time range 
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=20&count=19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 screen time range
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=808'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 輸入參數
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=613&y=459'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=613&y=459'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清除參數
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=67&count=3'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 確認參數 adb shell input keyevent 66
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/keyevent?docker-id=601e38e3ca19&keyevent=66&count=1'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊 ok adb shell input tap 1648 602
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=1648&y=602'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 點擊back 返回main_screen
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=88&y=0'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

#     # 清除音檔 clean recoder
#     time.sleep(6)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/clean_recordfolder?docker-id=601e38e3ca19'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout

# # 檢測完 - 滑軌後退
# def test_slide_backward():
#     time.sleep(2)
#     # 操控滑軌後退 連接relayboard
#     cmd = "curl -X GET 'http://192.168.150.180:8080/backward'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'backward' in p.stdout

# # 最後一步 - remove airmod
# def test_uninstall():
#     time.sleep(2)
#     cmd = "curl -X GET 'http://192.168.150.200:20000/uninstall_apk?docker-id=601e38e3ca19&location=192.168.150.100'"
#     p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     #time.sleep(5)
#     #cmd = "curl -X GET 'http://192.168.150.200:20000/tap?docker-id=601e38e3ca19&x=286&y=2087'"
#     p = subprocess.run(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print(p.stdout)
#     assert b'success' in p.stdout
