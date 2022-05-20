import unittest
#import HtmlTestRunner
#import xmlrunner
from xml.dom.minidom import Element
from   selenium import webdriver
from   selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class unitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\SeleniumWebDrivers\Chrome\chromedriver.exe")
    def test_suggestionClass(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/') 
        searchBar = driver.find_element_by_xpath('//*[@id="autocomplete"]')
        searchBar.send_keys('Me')
        #driver.implicitly_wait(5)
        #driver.find_element_by_xpath('//div[contains(text(), "Mexico")]').click()
        time.sleep(1)
        for a in driver.find_elements_by_xpath('//div[contains(text(), "Mexico")]'):
                if  a.text == 'Mexico':
                    assert  a.text == 'Mexico'
                    a.click()
                break
        time.sleep(4)      
if __name__ == "__main__":
    unittest.main()

