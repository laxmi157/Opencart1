import pytest
from pageobjects.Loginpage import Loginpage
from pageobjects.LogoutOrg import Logoutpage
from selenium import webdriver
from utilities import XLutils
from utilities.readProperities import ReadConfig
from utilities.customLogger import LogGen
import os
import time

class Test_002_loginpage:
    
    baseURL=ReadConfig.getOrangeURL()
    logger=LogGen.loggen() #for logging
    
    user=ReadConfig.getOrangeusername()
    pwd=ReadConfig.getOrgpasswd()
        
    @pytest.mark.sanity
    def test_Orange_Login(self,setup):
        self.logger.info("****test_002_OrangeLogin started *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        
        
        self.Logging= Loginpage(self.driver)
        self.logger.info("Providing username details for login") 
        self.Logging.setusername(self.user)
        self.Logging.setpassword(self.pwd)
        self.Logging.setloginclick()
        time.sleep(3)
        # self.logout=Logoutpage(self.driver)
        # self.logout.Orgdrpdasbbpard()
        # self.logout.OrgclickLogout()
        
        self.targetpage=self.Logging.DaashboardExists()
        self.logger.info("Dashboard page verification") 
        if self.targetpage==True:
            assert True
        else:
            # Save the screenshot
            screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            
            screenshot_path = os.path.join(screenshots_dir, "test_LoginOrgpage.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Login of Orgpage failed.")
            assert False
        self.logger.info("****test_002_OrangeLogin finished *****")
        
