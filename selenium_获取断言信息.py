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