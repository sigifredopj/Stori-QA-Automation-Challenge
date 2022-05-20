import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class unitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\SeleniumWebDrivers\Chrome\chromedriver.exe")
    def test_switchToAlert(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        openSimpleAlert = driver.find_element(by=By.XPATH, value='//*[@id="name"]')
        openSimpleAlert.send_keys('Stori Card')
        alertButton = driver.find_element(by=By.XPATH, value='//*[@id="alertbtn"]')
        alertButton.click()
        time.sleep(3)
        simpleAlert = driver.switch_to.alert
        simpleAlert.dismiss()
        time.sleep(3)
        openSimpleAlert = driver.find_element(by=By.XPATH, value='//*[@id="name"]').send_keys('Stori Card')
        confirmButton = driver.find_element(by=By.CSS_SELECTOR, value='#confirmbtn')
        confirmButton.click()
        simpleAlert
        time.sleep(3)
        simpleAlertText = driver.switch_to.alert.text
        print( simpleAlertText)
        
        simpleAlert.accept()



if __name__ == "__main__": 
    unittest.main()
