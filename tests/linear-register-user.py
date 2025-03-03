from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Generate email unik berdasarkan timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
random_email = f"testuser{timestamp}@example.com"

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. Launch browser and navigate to URL
driver.get("http://automationexercise.com")
driver.maximize_window()
time.sleep(3)  # Tunggu halaman load

# 2. Verify home page is visible successfully
assert "Automation Exercise" in driver.title, "Home page is not loaded"

# 3. Click on 'Signup / Login' button
signup_login_button = driver.find_element(By.XPATH, "//a[@href='/login']")
signup_login_button.click()
time.sleep(2)

# 4. Verify 'New User Signup!' is visible
assert "New User Signup!" in driver.page_source, "Signup section not found"

# 5. Enter name and email address
name_input = driver.find_element(By.NAME, "name")
email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
name_input.send_keys("Test User")
email_input.send_keys(random_email)  # Gunakan email unik yang dihasilkan
time.sleep(1)

# 6. Click 'Signup' button
signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
signup_button.click()
time.sleep(3)

# 7. Verify that 'ENTER ACCOUNT INFORMATION' is visible
assert "Enter Account Information" in driver.page_source, "Account Information page not found"

# 8. Fill details: Title, Name, Email, Password, Date of birth
driver.find_element(By.ID, "id_gender1").click()  # Select Title: Mr.
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Test@123")
driver.find_element(By.ID, "days").send_keys("10")  # Birth Day
driver.find_element(By.ID, "months").send_keys("May")  # Birth Month
driver.find_element(By.ID, "years").send_keys("1995")  # Birth Year

# 9. Select checkboxes for newsletter and special offers
driver.find_element(By.ID, "newsletter").click()
driver.find_element(By.ID, "optin").click()

# 10. Fill Address details
driver.find_element(By.ID, "first_name").send_keys("Test")
driver.find_element(By.ID, "last_name").send_keys("User")
driver.find_element(By.ID, "company").send_keys("Test Company")
driver.find_element(By.ID, "address1").send_keys("123 Test Street")
driver.find_element(By.ID, "address2").send_keys("Suite 100")
driver.find_element(By.ID, "country").send_keys("United States")
driver.find_element(By.ID, "state").send_keys("California")
driver.find_element(By.ID, "city").send_keys("Los Angeles")
driver.find_element(By.ID, "zipcode").send_keys("90001")
driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

# 11. Click 'Create Account' button
driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
time.sleep(3)

# 12. Verify that 'ACCOUNT CREATED!' is visible
assert "Account Created!" in driver.page_source, "Account was not created"

# 13. Click 'Continue' button
driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
time.sleep(2)

# 14. Verify 'Logged in as username' is visible
assert "Logged in as" in driver.page_source, "User is not logged in"

# 15. Click 'Delete Account' button
driver.find_element(By.XPATH, "//a[@href='/delete_account']").click()
time.sleep(3)

# 16. Verify 'ACCOUNT DELETED!' is visible and click 'Continue' button
assert "Account Deleted!" in driver.page_source, "Account was not deleted"
driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

# Close browser
driver.quit()