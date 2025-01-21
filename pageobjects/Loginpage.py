from selenium import webdriver
from selenium.webdriver.common.by import By

class Loginpage():
    #Locators
    txtbox_username_name="username"
    txtbox_password_name="password"
    button_Login_Xpath="//button[@type='submit']"
    Dassboard_Xpath="//h6[text()='Dashboard']"
    
        
    #Constructor
    def __init__(self,driver):
        self.driver=driver
        
    #action method
    def setusername(self,username):
        usernametxt=self.driver.find_element(By.NAME,self.txtbox_username_name)
        usernametxt.send_keys(username)
        
    def setpassword(self,psswd):
        passtxt=self.driver.find_element(By.NAME,self.txtbox_password_name)
        passtxt.send_keys(psswd)
        
    def setloginclick(self):
        self.driver.find_element(By.XPATH,self.button_Login_Xpath).click()
        
    def DaashboardExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.Dassboard_Xpath).is_displayed()
        except:
            return False
        
      
    