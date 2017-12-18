import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaiduSerach(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_serch_baidu_comd(self):
        driver = self.driver



if __name__ == '__main__':
    unittest.main()
