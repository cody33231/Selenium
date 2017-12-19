#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 10:40
# @Author  : Cody
# @Site    : 
# @File    : uuzc_test.py
# @Software: PyCharm

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://192.168.0.8/uuzc/bazhong/huodong1224/')
#最大化浏览器
browser.maximize_window()
#点击立即申请补贴
browser.find_element_by_xpath('//*[@id="divbg"]/div/a/div').click()
def from1(num, mobile):
    '''第一个表单输入的账号和密码并提交'''
    # 输入姓名
    browser.find_element_by_id('name1').send_keys(num)
    # 输入手机号
    browser.find_element_by_id('mobile1').send_keys(mobile)
    # 点击立即申请补贴
    browser.find_element_by_id('btn1').click()
    return

time.sleep(3)

