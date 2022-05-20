import unittest
import HtmlTestRunner
import time
from xml.dom.minidom import Element
from   selenium import webdriver
from   selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class unitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\SeleniumWebDrivers\Chrome\chromedriver.exe")
    def test_dropDown(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/') 
     
        searchDropDown = driver.find_element_by_xpath('//*[@id="dropdown-class-example"]').click()   
        for a in driver.find_elements_by_xpath('//*[@id="dropdown-class-example"]/option'):
                if  a.text == 'Option2':
                    assert  a.text == 'Option2'
                    a.click()
                    time.sleep(3)
                if a.text == 'Option3':
                    assert  a.text == 'Option3'
                    a.click()
                    driver.implicitly_wait(3)

                break
        
if __name__ == "__main__":
    unittest.main()

