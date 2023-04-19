from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
browser = webdriver.Chrome()
# Step 2) Navigate to Facebook
browser.get("https://www.apollohospitals.com/kolkataapolloconsultleads/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("txtYourName")
# password = browser.find_element_by_id("pass")
# submit   = browser.find_element_by_id("loginbutton")
username.send_keys("you@email.com")
# password.send_keys("yourpassword")
# Step 4) Click Login
# submit.click()