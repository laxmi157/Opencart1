from selenium.webdriver.common.by import By
from selenium import webdriver
# driver=webdriver.Chrome()

class Homepage():
    lnk_myaccount_xpth="//span[normalize-space()='My Account']"
    lnk_register_xpth="//a[normalize-space()='Register']"
    lnk_Login_linktext="Login"
    
   
    def __init__(self,driver):
        self.driver=driver
            
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpth).click()
        
    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_register_xpth).click()
    
    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_Login_linktext).click()