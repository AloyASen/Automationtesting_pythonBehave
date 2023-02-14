from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as BY

#initialize the webdriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")
# to identify element and then click
s = driver.find_element(BY.XPATH, "//*[text()='Library']")
driver.execute_script("arguments[0].click();",s)
print("Page title after click: " + driver.title)
driver.implicitly_wait(2)