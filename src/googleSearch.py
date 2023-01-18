# the below code runs on selenium 4 

from selenium import webdriver
from selenium.webdriver.common.by import By as BY
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# this extra package autometically updates the chomedriver if my chrome browser gets an upgrade pushed 
#from google
from webdriver_manager.chrome import ChromeDriverManager
print('sample test cases started')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# open a maximized window
driver.maximize_window()
#navigate to the url  
driver.get("https://www.google.com/") 
#identify the Google search text box and enter the value 

driver.find_element(BY.NAME,"q").send_keys("javatpoint")  
time.sleep(3)  
#click on the Google search button  
driver.find_element('name',"btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
#close the browser  
driver.close()  
print("sample test case successfully completed") 