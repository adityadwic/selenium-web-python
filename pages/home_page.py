from selenium.webdriver.common.by import By

class HomePage:
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")  # Menambahkan elemen Products

    def __init__(self, driver):
        self.driver = driver

    def click_signup_login(self):
        self.driver.find_element(*self.SIGNUP_LOGIN_BUTTON).click()

    def click_products_button(self):
        self.driver.find_element(*self.PRODUCTS_BUTTON).click()  # Fungsi untuk klik tombol Products