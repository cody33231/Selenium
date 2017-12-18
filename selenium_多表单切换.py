#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 16:28
# @Author  : Cody
# @Site    : 
# @File    : selenium_多表单切换.py
# @Software: PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://mail.163.com")

driver.switch_to_frame('x-URS-iframe')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('username')
driver.find_element_by_name("password").clear()
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_id('dologin').click()
#在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面。
driver.switch_to_default_content()

#switch_to.frame() 默认可以直接取表单的id 或name属性。如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。
#先通过xpath定位到iframe
#xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')
#再将定位对象传给switch_to_frame()方法
#driver.switch_to_frame(xf)

driver.quit()

