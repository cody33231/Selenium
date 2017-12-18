#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 17:11
# @Author  : Cody
# @Site    : 
# @File    : selenium_警告框处理.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()


#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()

#保存设置
driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
time.sleep(2)

#接受警告框
#通过switch_to_alert()方法获取当前页面上的警告框，并使用accept()方法接受警告框。
driver.switch_to_alert().accept()

driver.quit()

