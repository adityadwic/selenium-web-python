from selenium.webdriver.common.by import By

class RegistrationConfirmationPage:
    ACCOUNT_CREATED_HEADER = (By.XPATH, "//h2[text()='Account Created!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    def __init__(self, driver):
        self.driver = driver

    def verify_account_created(self):
        assert "Account Created!" in self.driver.page_source, "Account was not created"

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()