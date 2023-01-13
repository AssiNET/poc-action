import time
import unittest
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


class SenturTests(unittest.TestCase):
    # Execute BEFORE Test Suite
    @classmethod
    def setUpClass(cls):

        # Check GitHub for ideas around configs/desired caps

        ### iOS
        ### "app" : "bs://a4f2b75f3106c2c7e9d8417e8458342ca804e024",

        userName =  os.getenv("BROWSERSTACK_USERNAME")
        accessKey =  os.getenv("BROWSERSTACK_ACCESS_KEY")

        desired_caps = {
            "platformName" : "ios",
            "platformVersion" : "15",
            "deviceName" : "iPhone 13 Pro",
            "app" : "bs://a4f2b75f3106c2c7e9d8417e8458342ca804e024", # "bs://b31e40b7195ee0c80d8578b426e5cf47127c9294"
        }

        cls.driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

        # print the session ID in the IDE's console
        print(cls.driver.session_id)
        os.environ['BROWSERSTACK_SESSION_ID'] = cls.driver.session_id
        with open('session_id.txt', 'w') as f:
            f.write(cls.driver.session_id)

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


    def test_100_login(self):

        # search_element = WebDriverWait(self.driver, 30).until(
        #             EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        #         )
        # search_element.click()


        time.sleep(15)
        print("Click Allow Notification")
        button_allow = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow')
        button_allow.click()
        time.sleep(5)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Log in').click()

        search_element = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Email"))
                )
        
        field_text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Email')
        field_text.clear()
        field_text.send_keys("tester1@mailinator.com")
        time.sleep(3)

        field_text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Password')
        field_text.clear()
        field_text.send_keys("Pass1234")
        time.sleep(3)
        

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Log in').click()

if __name__ == '__main__':
    unittest.main()
