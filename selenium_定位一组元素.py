#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 11:11
# @Author  : Cody
# @Site    : 
# @File    : selenium_定位一组元素.py
# @Software: PyCharm

#TODO:关于一组元素定位的点

from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(1)

#定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')

#循环遍历出每一条搜索结果的标题
for x in texts:
    print(x.text)

driver.quit()

