from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace 'path/to/chromedriver' with the path to your ChromeDriver executable
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Open Facebook login page
driver.get("https://www.facebook.com")

# Locate the username and password fields using their HTML attributes
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")

# Replace 'your_email' and 'your_password' with your Facebook credentials
username_field.send_keys("your_email")
password_field.send_keys("your_password")

# Locate the login button and click it
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Wait for a few seconds to let the page load
time.sleep(5)

# Perform further actions or navigate to other pages as needed

# Close the browser
driver.quit()
