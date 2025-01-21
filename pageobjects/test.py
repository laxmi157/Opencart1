# from selenium.webdriver.common.by import By
# from selenium import webdriver

# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.get("https://demo.opencart.com/")
# # def Homepage():
   
# #     driver.find_element(By.LINK_TEXT)
# #     driver.find_element(By.LINK_TEXT)
# #     

# # Homepage()
# print("This is test report")
# tlt=driver.title
# print(tlt)


import os

# Create logs folder
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Test file creation
log_file = os.path.join(log_dir, "test.log")
with open(log_file, "w") as f:
    f.write("Test log file created successfully.\n")

print(f"Test log file created at: {log_file}")
    