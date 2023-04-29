import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.apollohospitals.com/kolkataapolloconsultleads/')


username = driver.find_element(By.ID,'txtYourName')
selectCity = driver.find_element(By.ID,'city')

username.send_keys("you@email.com")
# password.send_keys("yourpassword")
# Step 4) Click Login
# submit.click()