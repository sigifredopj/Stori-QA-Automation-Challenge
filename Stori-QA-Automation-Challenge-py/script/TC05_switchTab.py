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
    def test_switchTab(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        openTab = driver.find_element(by=By.XPATH, value='//*[@id="opentab"]').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,2000);")
        time.sleep(3)
        driver.save_screenshot("Switch Tab.png")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

if __name__ == "__main__": 
    unittest.main()
