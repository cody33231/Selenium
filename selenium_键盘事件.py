#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 15:21
# @Author  : Cody
# @Site    : 
# @File    : selenium_键盘事件.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("peter")

#删除一个peter 最后一个字母r
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#输入空格+教程
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

time.sleep(3)
#ctrl + a全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")

time.sleep(3)
#ctrl + x剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")

time.sleep(3)
#ctrl + v粘贴输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "v")

time.sleep(3)
#通过回车代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

driver.quit()