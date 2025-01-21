from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
import time


class AccountRegisterationpage():
    #Locators
    txtbox_Firstname_id="input-firstname"
    txtbox_Lastname_id="input-lastname"
    txtbox_Email_id="input-email"
    txtbox_Password_id="input-password"
    chackbox_Newsletter_id="input-newsletter"
    checkbox_privacy_xpath="//input[@name='agree']"
    button_continue_xpath="//button[@type='submit']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"
    
    #Constructor
    def __init__(self,driver):
        self.driver=driver
        
    #action methods
    def setfirstName(self,FirstName):
        FirstNametxt=self.driver.find_element(By.ID,self.txtbox_Firstname_id)
        FirstNametxt.send_keys(FirstName)
    
    def setLastName(self,lastName):
        lastnametxt=self.driver.find_element(By.ID,self.txtbox_Lastname_id)
        lastnametxt.send_keys(lastName)
    
    def setEmail(self,Email):
        Emailtxt=self.driver.find_element(By.ID,self.txtbox_Email_id)
        Emailtxt.send_keys(Email)
        
    def setpwd(self,pwd):
        pwdtxt=self.driver.find_element(By.ID,self.txtbox_Password_id)
        pwdtxt.send_keys(pwd)
    
    def setNewsLetterCheckbox(self):
        self.driver.find_element(By.ID,self.chackbox_Newsletter_id).click()
        
    def setPrivacyPolicy(self):
        #Scroll down the page till the end of the page
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        value=self.driver.execute_script("return window.pageYOffset;")
        print("Number of pixels moved: ",value)
        
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        element=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,self.checkbox_privacy_xpath)))
        element.click()
        
        # element = self.driver.find_element(By.XPATH, self.checkbox_privacy_xpath)
        # self.driver.execute_script("arguments[0].click();", element)
        # element = self.driver.find_element(By.XPATH, self.checkbox_privacy_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # element.click()

    def buttonContinue(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        value=self.driver.execute_script("return window.pageYOffset;")
        print("Number of pixels moved: ",value)
        
        button=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,self.button_continue_xpath)))
        # self.driver.find_element(By.XPATH,self.button_continue_xpath).click()    
        time.sleep(10)
        button.click()
        
        
    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None
            
       
        