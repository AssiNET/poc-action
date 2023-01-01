import time
import unittest
import os
import datetime
import logging

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

class FeeldTests(unittest.TestCase):
    # Execute BEFORE Test Suite
    @classmethod
    def setUpClass(cls):

        # Check GitHub for ideas around configs/desired caps

        userName =  os.getenv("BROWSERSTACK_USERNAME")
        accessKey =  os.getenv("BROWSERSTACK_ACCESS_KEY")

        desired_caps = {
            "platformName" : "ios",
            "platformVersion" : "15",
            "deviceName" : "iPhone 13 Pro",
            "app" : "bs://12b6296384884c6d6ddf9e895889a88d57d9e8f2", # "bs://b31e40b7195ee0c80d8578b426e5cf47127c9294"
        }

        cls.driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
        
        # print the session ID in the IDE's console
        print(cls.driver.session_id)
        os.environ['BROWSERSTACK_SESSION_ID'] = cls.driver.session_id


    # Execute BEFORE each Test
    def setUp(self):
        pass

    # Execute AFTER each test
    def tearDown(self):
        pass

    # Execute AFTER Test Suite
    @classmethod
    def tearDownClass(cls):
        ####cls.driver.close()
        cls.driver.quit()
        print("Test Suite Completed")

    def test_100_update_about_info(self):

        time.sleep(15)
        print("Click Allow Notification")
        button_allow = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow')
        button_allow.click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
