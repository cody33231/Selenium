#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 11:39
# @Author  : Cody
# @Site    : 
# @File    : selenium_iframe.py
# @Software: PyCharm

from selenium import webdriver
import os
import time

browser = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath('frame.html')

browser.get(file_path)

browser.implicitly_wait(30)

browser.switch_to_frame('f1')

browser.switch_to_frame('f2')

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()

