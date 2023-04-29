import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.apollo247.com/appointment/index.html')
username = driver.find_element(By.ID,'firstName')
selectCity = driver.find_element(By.ID,'city')
phone_no = driver.find_element(By.ID,'phone')

username.send_keys("you@email.com") #mail
selectCity.send_keys("kolkata") #city Location
phone_no.send_keys("9991115554") #Number from user
btn = driver.find_element(By.ID,'submit')
btn.click()