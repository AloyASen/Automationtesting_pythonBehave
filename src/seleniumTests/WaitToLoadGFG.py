# wait for GFG to load 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as BY 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create the driver object for Chrome 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# get the page 
driver.get('https://www.geeksforgeeks.org/')

try:
    # the code halts executing for some time 
    element = WebDriverWait(driver= driver , timeout= 10 ).until(
        EC.presence_of_element_located( (BY.LINK_TEXT,'Courses'))
        )
finally:
    driver.quit()