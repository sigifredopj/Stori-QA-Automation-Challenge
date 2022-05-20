from audioop import add
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
    def test_webTable(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        time.sleep(2)

        #values = driver.find_element(by=By.XPATH, value='//table[@class="table-display"]/tbody/tr[2]/td[2]').text
        #//div[@class='left-align']//table[@id='product']
        #print(values)
        
        rows=len(driver.find_elements(by=By.XPATH, value='//table[@class="table-display"]/tbody/tr'))
        cols=len(driver.find_elements(by=By.XPATH, value='//table[@class="table-display"]/tbody/tr[1]/th'))
        #print(rows)
        #print(cols)

        for n in range(2, rows+1):
            for b in range(1, cols+1):
                value = driver.find_element(by=By.XPATH, value='//table[@class="table-display"]/tbody/tr['+str(n)+']/td['+str(b)+']').text
                #print(value, end='  | ')  
                #print() 
                if value == "25":
                    print ("Found " + value )
                    

                
                

if __name__ == "__main__": 
    unittest.main()
