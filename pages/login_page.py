from selenium.webdriver.common.by import By

class LoginPage:
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Login to your account']")

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_login_page(self):
        assert "Login to your account" in self.driver.page_source, "Login page not found"