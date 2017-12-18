#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 15:32
# @Author  : Cody
# @Site    : 
# @File    : selenium_获取断言信息.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print("Before search==============")

#打印当前页面的title
title = driver.title
print(title)

#打印当前页面的url
now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

sleep(1)

print("After search=============")

#再次打印当前页title
title = driver.title
print(title)

#打印当前页面url
now_url = driver.current_url
print(now_url)

#获得结果数
user = driver.find_element_by_class_name("nums").text
print(user)

driver.quit()