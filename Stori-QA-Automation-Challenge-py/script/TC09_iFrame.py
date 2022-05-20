import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class unitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\SeleniumWebDrivers\Chrome\chromedriver.exe")
    def test_webTableFixed(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='courses-iframe']"))
        text = driver.find_element_by_xpath("//li[contains(text(),'His mentorship program is most after in the softwa')]").text
        print (text)
        
if __name__ == "__main__": 
    unittest.main()
