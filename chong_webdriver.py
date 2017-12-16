#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 16:01
# @Author  : Cody
# @Site    : 
# @File    : chong_webdriver.py


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
url = "http://www.baidu.com"
print("now access %s" % url)
#访问百度
browser.get(url)

browser.maximize_window()
browser.find_element_by_id("kw").send_keys("chenchuan")
emil = browser.find_element_by_id("kw")
emil.send_keys(Keys, RETURN)

sleep(3)
browser.find_element_by_id("kw").clear()
#使用变量date 接受 id为cp的元素文本使用方法.text
data = browser.find_element_by_name("tj_login").text

print(data)
print(browser.title)


'''second_url = "http://news.baidu.com"

sleep(3)
browser.get(second_url)
print("访问百度新闻网站 %s" % second_url)

#返回百度首页
browser.back()
print("返回上一页")


sleep(3)
#前进到新闻页
browser.forward()
print("前进到新闻页")


print(browser.title)
#隐式地等待一个无素被发现或一个命令完成；这个方法每次会话只需要调用一次
#browser.implicitly_wait(3)
#固定等待3秒
sleep(3)
#设置浏览器的分辨率
browser.set_window_size(480, 800)
print("设置浏览器的分辨率480 * 800")
index = browser.find_element_by_id("kw")
#index.send_keys("chenchuan")
#index.send_keys(Keys.RETURN)
#browser.find_element_by_link_text("贴吧").click()
browser.find_element_by_partial_link_text("贴").click()
sleep(5)'''
browser.quit()

