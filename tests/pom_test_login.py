import time
import pytest
import json
from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_confirmation_page import RegistrationConfirmationPage

@pytest.fixture(scope="module")
def setup():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_login_user_correct_email_password(setup):
    driver = setup

    # 1. Read registration data from the JSON file
    with open("registration_data.json", "r") as f:
        registration_data = json.load(f)
    
    # Retrieve email and password from JSON
    email = registration_data["email"]
    password = registration_data["password"]

    # 2. Navigate to home page
    driver.get("http://automationexercise.com")
    time.sleep(3)  # Wait for page to load

    # 3. Verify home page is visible successfully
    assert "Automation Exercise" in driver.title, "Home page is not loaded"

    # 4. Navigate to login page
    home_page = HomePage(driver)
    home_page.click_signup_login()

    # 5. Initialize login_page object now that the login page is loaded
    login_page = LoginPage(driver)

    # 6. Verify login page is visible
    login_page.verify_login_page()

    # 7. Enter correct email address and password from JSON file
    login_page.enter_credentials(email, password)
    login_page.click_login_button()
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