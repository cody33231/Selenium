from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/')
assert "知乎" in browser.title

browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a[2]").click()
browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span").click()
browser.implicitly_wait(10)
browser.find_element_by_name("account").send_keys("cody_chen@163.com")
browser.find_element_by_name("account").send_keys(Keys.TAB)
browser.find_element_by_name("password").send_keys("cody.33231")
browser.find_element_by_name("password").send_keys(Keys.ENTER)


#browser.quit()

