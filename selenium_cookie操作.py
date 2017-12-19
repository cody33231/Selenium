#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 10:02
# @Author  : Cody
# @Site    : 
# @File    : selenium_cookie操作.py
# @Software: PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

#获取cookie信息
'''cookie = driver.get_cookies()

#打印获取的cookie
print(cookie)'''

#向cookie的name 和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

#遍历cookies中的 name和value并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()