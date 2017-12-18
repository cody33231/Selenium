#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 15:05
# @Author  : Cody
# @Site    : 
# @File    : selenium_鼠标事件.py
# @Software: PyCharm

from selenium import webdriver
#引入 ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#定位到要悬停的元素

above = driver.find_element_by_link_text("设置")
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

time.sleep(5)

driver.quit()