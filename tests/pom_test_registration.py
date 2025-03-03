import time
import pytest
import json
from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.registration_confirmation_page import RegistrationConfirmationPage
from datetime import datetime

@pytest.fixture(scope="module")
def setup():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_user_registration(setup):
    driver = setup

    # 1. Navigate to home page
    driver.get("http://automationexercise.com")
    time.sleep(3)  # Wait for page to load

    # 2. Verify home page is visible successfully
    assert "Automation Exercise" in driver.title, "Home page is not loaded"

    # 3. Navigate to signup page
    home_page = HomePage(driver)
    home_page.click_signup_login()

    # 4. Initialize signup_page object now that the page is loaded
    signup_page = SignupPage(driver)

    # 5. Enter name and email address for registration
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_email = f"testuser{timestamp}@example.com"
    signup_page.enter_account_details("Test User", random_email)
    signup_page.click_signup_button()  # Click the signup button to continue registration
    time.sleep(3)

    # 6. Verify signup page is visible
    signup_page.verify_account_creation_page()

    # 7. Fill out the registration form (account details)
    signup_page.fill_account_creation_form(
        password="Test@123",
        day="10", month="May", year="1995",
        first_name="Test", last_name="User", company="Test Company",
        address1="123 Test Street", address2="Suite 100", country="United States",
        state="California", city="Los Angeles", zipcode="90001", mobile_number="1234567890"
    )
    signup_page.click_create_account_button()

    # 8. Save registration details to a JSON file for future login
    registration_data = {
        "name": "Test User",
        "email": random_email,
        "password": "Test@123"  # Add the password if needed for login
    }
    with open("registration_data.json", "w") as f:
        json.dump(registration_data, f)

    # 9. Verify that account was created
    registration_confirmation_page = RegistrationConfirmationPage(driver)
    registration_confirmation_page.verify_account_created()

    # 10. Click continue after account creation
    registration_confirmation_page.click_continue_button()
    time.sleep(2)

    # 11. Verify that the user is logged in
    assert "Logged in as" in driver.page_source, "User is not logged in"