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
    def test_webTableFixed(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')

        driver.find_elements_by_xpath('')
        #for int i=1;i<=list.length;i+ :
        #text1 = driver.find_element_by_xpath("//*[@class='general_table']/div["+i+"]/div[1]").text;
        #text2 = driver.find_element_by_xpath("//*[@class='general_table']/div["+i+"]/div[2]").text;


if __name__ == "__main__": 
    unittest.main()