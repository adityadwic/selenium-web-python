import time
import pytest
from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage  # Mengimpor HomePage yang sudah diperbarui
from pages.products_page import ProductsPage
from pages.login_page import LoginPage  # Optional, depending on your test setup

@pytest.fixture(scope="module")
def setup():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_search_product(setup):
    driver = setup

    # 1. Navigate to home page
    driver.get("http://automationexercise.com")
    time.sleep(3)  # Wait for page to load

    # 2. Verify home page is visible successfully
    assert "Automation Exercise" in driver.title, "Home page is not loaded"

    # 3. Navigate to Products page
    home_page = HomePage(driver)  # Menggunakan HomePage yang sudah diperbarui
    home_page.click_products_button()  # Mengklik tombol Products

    # 4. Verify user is navigated to All Products page
    products_page = ProductsPage(driver)
    products_page.verify_all_products_page()

    # 5. Enter product name in search input and click search button
    product_name = "T-shirt"
    products_page.enter_product_name_in_search(product_name)
    products_page.click_search_button()
    time.sleep(3)

    # 6. Verify 'SEARCHED PRODUCTS' header is visible
    products_page.verify_searched_products_header()

    # 7. Verify that products related to search are visible
    products_page.verify_products_are_visible()

    # Close the browser after the test
    driver.quit()