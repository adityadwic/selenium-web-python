from selenium.webdriver.common.by import By

class SignupPage:
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ACCOUNT_HEADER = (By.XPATH, "//h2[text()='Enter Account Information']")

    # Fields for account creation after Signup
    PASSWORD_INPUT = (By.ID, "password")
    BIRTHDAY_DAYS = (By.ID, "days")
    BIRTHDAY_MONTHS = (By.ID, "months")
    BIRTHDAY_YEARS = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")

    def __init__(self, driver):
        self.driver = driver

    def enter_account_details(self, name, email):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def verify_account_creation_page(self):
        assert "Enter Account Information" in self.driver.page_source, "Account Creation page not found"

    def fill_account_creation_form(self, password, day, month, year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile_number):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.BIRTHDAY_DAYS).send_keys(day)
        self.driver.find_element(*self.BIRTHDAY_MONTHS).send_keys(month)
        self.driver.find_element(*self.BIRTHDAY_YEARS).send_keys(year)
        self.driver.find_element(*self.NEWSLETTER_CHECKBOX).click()
        self.driver.find_element(*self.SPECIAL_OFFERS_CHECKBOX).click()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.COMPANY).send_keys(company)
        self.driver.find_element(*self.ADDRESS1).send_keys(address1)
        self.driver.find_element(*self.ADDRESS2).send_keys(address2)
        self.driver.find_element(*self.COUNTRY).send_keys(country)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(mobile_number)

    def click_create_account_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()