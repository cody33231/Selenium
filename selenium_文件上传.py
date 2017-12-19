#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 9:54
# @Author  : Cody
# @Site    : 
# @File    : selenium_文件上传.py
# @Software: PyCharm

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)

time.sleep(5)
#定位上传按钮，添加本地文件
#\\的意思是转义\
driver.find_element_by_name('file').send_keys("D:\\upload_file.txt")
time.sleep(5)
driver.quit()