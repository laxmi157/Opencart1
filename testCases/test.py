# import pkg_resources

# installed_packages = [pkg.key for pkg in pkg_resources.working_set]
# if "pytest-metadata" in installed_packages:
#     print("pytest-metadata is installed")
# else:
#     print("pytest-metadata is not installed")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# import tensorflow as tf

from selenium import webdriver  

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.opencart.com/en-gb?route=account/register")
