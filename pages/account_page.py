from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    ACCOUNT_CREATED_LABEL = (By.XPATH, "//h2[contains(text(),'ACCOUNT CREATED!')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[contains(text(),'Continue')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(),'Delete Account')]")
    ACCOUNT_DELETED_LABEL = (By.XPATH, "//h2[contains(text(),'ACCOUNT DELETED!')]")

    def verify_account_created(self):
        return self.get_text(self.ACCOUNT_CREATED_LABEL)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BUTTON)

    def verify_account_deleted(self):
        return self.get_text(self.ACCOUNT_DELETED_LABEL)