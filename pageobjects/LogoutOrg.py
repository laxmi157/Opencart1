from selenium import webdriver
from selenium.webdriver.common.by import By

class Logoutpage():
    
    Org_Dropdown_xpath="//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    lnk_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver
    
    def Orgdrpdasbbpard(self):
        self.driver.find_element(By.XPATH, self.Org_Dropdown_xpath).click()
    
    def OrgclickLogout(self):
        self.driver.find_element(By.XPATH,self. lnk_logout_xpath).click()
        
    

