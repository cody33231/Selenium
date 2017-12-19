#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 10:36
# @Author  : Cody
# @Site    : 
# @File    : selenium_调用JavaScript代码.py

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#设置浏览器分辨率为500 * 500
driver.set_window_size(500, 500)

#搜索
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)

# 通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)

sleep(5)

driver.quit()



