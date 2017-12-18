#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 14:47
# @Author  : Cody
# @Site    : 
# @File    : selenium_浏览器操作.py
# @Software: PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
#访问百度首页
driver.get("http://m.baidu.com")
print("now access %s" % '百度首页')
#设置数字像素点
print("设置浏览器宽480 、高800显示")
driver.set_window_size(480, 800)

#访问新闻页面
news_url = 'http://news.baidu.com'
print("now access %s" % news_url)
driver.get(news_url)

#后退返回百度首页
print("back to " '百度首页')
driver.back()

#前进到新闻页面
print("forward to " '新闻页')
driver.back()

#刷新页面
driver.refresh()