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

        #driver.find_elements(by=By.CSS_SELECTOR, value= 'html body div.block.large-row-spacer div.right-align fieldset div.tableFixHead table#product')
        rows=len(driver.find_elements(by=By.XPATH, value='/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr'))
        cols=len(driver.find_elements(by=By.XPATH, value='/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[1]/th'))
        for n in range(2, rows+1):
            for b in range(1, cols+1):
                value = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr['+str(n)+']/td['+str(b)+']and[contains(text(), "Engineer")]').text
                print(value, end='  | ')
        
        

if __name__ == "__main__": 
    unittest.main()
