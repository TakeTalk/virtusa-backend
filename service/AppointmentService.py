import time
from service.UserService import *
from collections import *
from service.UserService import *
from selenium import webdriver
from selenium.webdriver.common.by import By
def getAppointment():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.apollo247.com/appointment/index.html')
    username = driver.find_element(By.ID,'firstName')
    selectCity = driver.find_element(By.ID,'city')
    phone_no = driver.find_element(By.ID,'phone')

    username.send_keys(email) #mail
    selectCity.send_keys("Kolkata") #city Location
    phone_no.send_keys(getPhoneByEmail(email)) #Number from user
    btn = driver.find_element(By.ID,'submit')
    btn.click()