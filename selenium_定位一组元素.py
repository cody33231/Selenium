#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 11:11
# @Author  : Cody
# @Site    : 
# @File    : selenium_定位一组元素.py
# @Software: PyCharm

from selenium import webdriver
import time
import os

dr = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

inputs = dr.find_elements_by_tag_name('input')

for x in inputs:
    if x.__getattribute__('type') == 'checkbox':
        x.click()


time.sleep(20)
dr.quit()



