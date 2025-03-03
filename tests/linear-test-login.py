from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. Launch browser
driver.maximize_window()

# 2. Navigate to URL
driver.get("http://automationexercise.com")
time.sleep(3)  # Wait for the page to load

# 3. Verify home page is visible successfully
assert "Automation Exercise" in driver.title, "Home page is not loaded"

# 4. Click on 'Signup / Login' button
signup_login_button = driver.find_element(By.XPATH, "//a[@href='/login']")
signup_login_button.click()
time.sleep(2)

# 5. Verify 'Login to your account' is visible
assert "Login to your account" in driver.page_source, "Login section not found"

# 6. Enter correct email address and password
email_input = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
password_input = driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
email_input.send_keys("testuser@example.com")  # Replace with a valid test email
password_input.send_keys("testingQA-adc")  # Replace with the correct password
time.sleep(1)

# 7. Click 'login' button
login_button = driver.find_element(By.XPATH, "//button[@data-qa='login-button']")
login_button.click()
time.sleep(3)

# 8. Verify that 'Logged in as username' is visible
assert "Logged in as" in driver.page_source, "User is not logged in"

# 9. Click 'Delete Account' button
delete_account_button = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
delete_account_button.click()
time.sleep(3)

# 10. Verify that 'Account Deleted!' is visible
assert "Account Deleted!" in driver.page_source, "Account was not deleted"

# Close browser
driver.quit()