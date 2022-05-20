from selenium import webdriver

def setUp(self):
    self.driver = webdriver.Chrome(executable_path=r"C:\SeleniumWebDrivers\Chrome\chromedriver.exe")
    driver = self.driver

