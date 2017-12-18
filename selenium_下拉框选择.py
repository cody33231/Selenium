#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 17:21
# @Author  : Cody
# @Site    : 
# @File    : selenium_下拉框选择.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 鼠标悬停至“设置”链接
driver.find_element_by_link_text('设置').click()
sleep(1)

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

#搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")
#Select类用于定位select标签。 select_by_value() 方法用于定位下接选项中的value值。
Select(sel).select_by_value('50') #显示50条


driver.quit()