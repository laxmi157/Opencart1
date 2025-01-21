import pytest
from pageobjects.Loginpage import Loginpage
from pageobjects.LogoutOrg import Logoutpage
from selenium import webdriver
from utilities import XLutils
from utilities.readProperities import ReadConfig
from utilities.customLogger import LogGen
import os
import time

class Test_003_login_DDT():
    
    baseURL=ReadConfig.getOrangeURL()
    logger=LogGen.loggen() #for logging
    
    path=os.path.abspath(os.curdir)+"\\testCases\\testData\\OrgLoginpage.xlsx"
    
      
    
    def test_Orange_Login(self,setup):
        self.logger.info("****test_003_OrangeLogin_Datadriven started *****")
        self.rows=XLutils.getRowCount(self.path,'Sheet1')
        lst_status=[]
        
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
                    
        
        self.Lp=Loginpage(self.driver) #Login page object class
        self.lgout=Logoutpage(self.driver) #Logout page object class
        self.logger.info("Providing username details for login") 
        
        for r in range(2,self.rows+1):
        
            self.Lp=Loginpage(self.driver) 
            self.user=XLutils.readData(self.path,"Sheet1",r,1)
            self.pswd=XLutils.readData(self.path,"Sheet1",r,2)
            self.exp=XLutils.readData(self.path,"Sheet1",r,3)
            self.Lp.setusername(self.user)
            self.Lp.setpassword(self.pswd)
            self.Lp.setloginclick()                    
                
            self.targetpage=self.Lp.DaashboardExists()
            self.logger.info("Dashboard page verification")        
        
           
            if self.exp=='valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.lgout=Logoutpage(self.driver)
                    self.lgout.Orgdrpdasbbpard()
                    self.lgout.OrgclickLogout()
                else:
                    lst_status.append('Fail')        
            elif self.exp=='Invalid':
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.lgout=Logoutpage(self.driver)
                    self.lgout.Orgdrpdasbbpard()
                    self.lgout.OrgclickLogout()
                else:
                    lst_status.append('Pass')
                
        #final validation    
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******End of test_003_Loginpage_datadriven******")    
                
                
            
        
