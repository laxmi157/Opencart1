from pageobjects.Homepage import Homepage
from pageobjects.AccountRegistrationpage import AccountRegisterationpage
from selenium import webdriver
from utilities import randomstring 
from utilities.readProperities import ReadConfig
from utilities.customLogger import LogGen
import pytest
import time
import os

class Test_001_AccountReg:
 
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() #for logging
    # Logger=LogGen.setup_logging()
    
    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("****test_001_AccountRegistration started *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
              
        
        # self.hp=Homepage(self.driver)
        # self.hp.clickMyAccount()
        # self.hp.clickRegister()
        
        self.regpage=AccountRegisterationpage(self.driver)
        self.logger.info("Providing customer details for registration")    
        self.regpage.setfirstName("John")
        
        self.regpage.setLastName("Candey")
        self.email=randomstring.generate_random_string()+'@gmail.com'
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("aabc")
        self.regpage.setpwd("abcd")
        self.regpage.setNewsLetterCheckbox()
        
        self.driver.execute_script("window.scrollBy(300,document.body.scrollHeight)")
        value=self.driver.execute_script("return window.pageYOffset;")
        print("Number of pixels moved: ",value)
        time.sleep(10)
        self.regpage.setPrivacyPolicy()
        
        
        self.regpage.buttonContinue()
        
        self.confmsg=self.regpage.getconfirmationmsg()
        # self.driver.close()
        
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Account registration passed")
            assert True
           
        else:
            # self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            # self.driver.save_screenshot("C:\Users\vlaxm\Documents\OpenCartProjectV1\pageobjects\screenshots\test_account.png")
            
            # Create the screenshots directory if it doesn't exist
            # screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            # os.makedirs(screenshots_dir, exist_ok=True)
            
            # Save the screenshot
            screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            
            screenshot_path = os.path.join(screenshots_dir, "test_account_reg2.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Account registration failed.")
            assert False
        self.logger.info("****test_001_AccountRegistration finished *****")
        
        
        
        
        