#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 10:45
# @Author  : Cody
# @Site    : 
# @File    : selenium_窗口截图.py
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

#截取当前窗口，并指定截图图片的保持位置

driver.get_screenshot_as_file("E:\\python_code\\Selenium\\baiduindex.jpg")

driver.quit()
