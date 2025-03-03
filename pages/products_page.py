from selenium.webdriver.common.by import By

class ProductsPage:
    PRODUCTS_HEADER = (By.XPATH, "//h2[text()='All Products']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='search_product']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='submit_search']")
    SEARCHED_PRODUCTS_HEADER = (By.XPATH, "//h2[text()='Searched Products']")
    PRODUCT_LIST = (By.XPATH, "//div[@class='product-image-wrapper']")

    def __init__(self, driver):
        self.driver = driver

    def verify_all_products_page(self):
        assert "All Products" in self.driver.page_source, "Not on All Products page"

    def enter_product_name_in_search(self, product_name):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def verify_searched_products_header(self):
        assert "Searched Products" in self.driver.page_source, "Searched Products header not found"

    def verify_products_are_visible(self):
        products = self.driver.find_elements(*self.PRODUCT_LIST)
        assert len(products) > 0, "No products are displayed for the search"