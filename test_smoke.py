import time
import unittest
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By



class SenturTests(unittest.TestCase):
    # Execute BEFORE Test Suite
    @classmethod
    def setUpClass(cls):
        userName =  os.getenv("BROWSERSTACK_USERNAME")
        accessKey =  os.getenv("BROWSERSTACK_ACCESS_KEY")


        desired_caps = {
            'autoGrantPermissions' : 'true', # accept all alerts
            "platformName" : "Android",
            "platformVersion" : "11.0",
            "deviceName" : "Samsung Galaxy S21",
            "app" : "bs://8267220e96a2ca0658d6d511f988bc5862a26c1e", # "bs://b31e40b7195ee0c80d8578b426e5cf47127c9294"
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
        
        button_login = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Log in"))
                )
        button_login.click()

        WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText"))
                )


        inputs = self.driver.find_elements(By.CLASS_NAME, "android.widget.EditText")
        email_input = inputs[0]
        password_input = inputs[1]
        email_input.click()
        time.sleep(1)
        email_input.send_keys("tester1@mailinator.com")
        time.sleep(1)

        password_input.click()
        time.sleep(1)
        password_input.send_keys("Pass1234")
        time.sleep(1)

        WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Log in"))).click()

        time.sleep(5)

    def test_200_Verify_Tab_Home(self):
        WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Meditations & Exercises")))

        ########################
        ########################
        ########################

    def test_300_Verify_Tab_Parts(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Parts\nTab 2 of 5").click()
        WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Self")))
        time.sleep(1)

    def test_400_Verify_Tab_Self(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Self\nTab 3 of 5").click()
        WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Week\nTab 1 of 4")))
        time.sleep(1)

    def test_500_Verify_Tab_Trailheads(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Trailheads\nTab 4 of 5").click()
        WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Creating New Trailheads")))
        time.sleep(1)

    def test_600_Verify_Tab_Journal(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Journal\nTab 5 of 5").click()
        WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Your Journal")))
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
