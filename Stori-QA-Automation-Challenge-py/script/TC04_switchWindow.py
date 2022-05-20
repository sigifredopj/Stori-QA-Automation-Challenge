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
    def test_switchWindow(self):
        driver = self.driver
        driver.maximize_window()
                                                   
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        #openTabButton = driver.find_element_by_xpath('//a[@id="opentab"]').click()
        openWindowButton = driver.find_element(by=By.XPATH, value='//button[@id="openwindow"]').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        #guaranteeText = driver.find_element_by_xpath('//h3[normalize-space()="30 day Money Back Guarantee"]')
        #guaranteeText = driver.find_element(by=By.XPATH, value='//*[@id="welcome"]/div/div/div/div[5]/div/div[2]/div/div[2]/h3')
        guaranteeText = driver.find_element(by=By.CSS_SELECTOR, value="div[class='col-sm-6'] div[class='col-sm-9'] h3")
        #guaranteeText = driver.find_element_by_css_selector("div[class='col-sm-6'] div[class='col-sm-9'] h3")
        try:
            assert  guaranteeText.is_displayed() == True
            print('Passed! Text is present')
        except:
            print('Failed! Text is not present')
            driver.close()
        

if __name__ == "__main__": 
    unittest.main()

