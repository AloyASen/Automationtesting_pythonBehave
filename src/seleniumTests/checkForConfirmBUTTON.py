# wait for GFG to load 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as BY 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create the driver object for chrome 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#open the page to be tested for confirm box 

driver.get('file:///C:/Users/adysenlab/Documents/documenta/github/AloyASen/JavascriptTraining/test_alertBox.html')

driver.maximize_window()

###  Business Logic Here ###
# ---- Step 1 
#check if header is present and paragraph has no text in it 

pageHeader = driver.find_element(BY.ID, 'pageHeader').text
paragraph_beforePopup = driver.find_element(BY.ID, 'demoClick').text
assert pageHeader == 'JavaScript Confirm Box' , 'The page is not loaded as per requirement'
assert paragraph_beforePopup == '' , ' the page popup is not accesible please chek the page structure'

print (' the page is successfully loaded and testable for popup Confirm button')

# ---- Step 2
#click the popup button and capture the screenshot for the same 
clickButton = driver.find_element(BY.ID, 'clickButtonHere').click()
# driver.get_screenshot_as_file('./testData/confirmButtonCapture.png')
driver.switch_to.alert.accept()
paragraph_afterPopupClose = driver.find_element(BY.ID, 'demoClick').text

assert paragraph_afterPopupClose == 'You pressed OK!' , ' the page popup is not accesible please chek the page structure'

print (' the page is successfully loaded and tested for popup Confirm button')
