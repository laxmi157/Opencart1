import pytest
import pytest_html

from selenium import webdriver
import logging
from datetime import datetime
import os



@pytest.fixture()
def setup(browser):
    if browser=='Firefox':
        driver=webdriver.Firefox()
        print("launching firefox browser..")
        
        
    elif browser=='edge':
        driver=webdriver.Edge()
        print("Launching edge browser...")
        
    else:
        driver=webdriver.Chrome()
        print("Launching chrome browser...")
        
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")
    

@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")




##############pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Python", None)
    metadata.pop("Base URL", None)
    metadata.pop("Platform", None)
    metadata.pop("Packages", None)
    metadata.pop("Driver", None)
    metadata.pop("Capabilities", None)
    metadata["Execution Date"] = "2025-01-19"
    metadata["Project Name"] = "OrangeHRM"
    metadata["URL"]="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    metadata[" Tester"]="Varalakshmi"
    metadata['Module Name'] = "OrangeHRM_Login_page"
   

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


####################Log file Config###################
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Get the log file path from pytest.ini
    log_file = config.getini("log_file")

    # Default to a fallback if log_file is not defined
    if not log_file:
        log_file = "logs/default_test_logs.log"

    # Ensure the logs directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure logging with append mode
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file, mode="a"),  # Append mode
            logging.StreamHandler()  # Optional: Show logs in the console
        ],
    )








































