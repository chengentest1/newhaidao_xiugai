import unittest

import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)


    def tearDown(self):
        time.sleep(3)
        self.driver.close()