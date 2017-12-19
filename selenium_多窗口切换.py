#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 16:41
# @Author  : Cody
# @Site    : 
# @File    : selenium_多窗口切换.py
# @Software: PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获得百度搜索窗口句柄
#current_window_handle获得当前窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

#获得当前所有打开的窗口的句柄
#window_handles返回所有窗口的句柄到当前会话

all_handles = driver.window_handles

#进入注册窗口

for handle in all_handles:
    if handle != sreach_windows:
        #switch_to用于切换到相应的窗口
        driver.switch_to.window(handle)
        print('now register windows1')
        #driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('username')
        #driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('password')
        time.sleep(2)

driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('username')
driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('password')
title2 = driver.title
print(title2)
time.sleep(2)
driver.quit()