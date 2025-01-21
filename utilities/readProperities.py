import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo','baseURL'))
        return url
    
    @staticmethod
    def getUsername():
        username=(config.get('commonInfo','email'))
        return username
    
    @staticmethod
    def getpassword():
        password=(config.get('commonInfo','password'))
        return password
    
    @staticmethod
    def getOrangeURL():
        Orangeurl=(config.get('commonInfo','OrangeURL'))
        return Orangeurl
        
    @staticmethod
    def getOrangeusername():
        Orgusername=(config.get('commonInfo','Orguser'))
        return Orgusername
    
    @staticmethod
    def getOrgpasswd():
        orgpasswd=(config.get('commonInfo','Orgpswd'))
        return orgpasswd
    
    