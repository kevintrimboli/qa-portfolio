from automation_selenium.project_01_basic_checkout.pages.login_page import LoginPage
from automation_selenium.project_01_basic_checkout.pages.inventory_page import InventoryPage
from automation_selenium.project_01_basic_checkout.pages.checkout_page import CheckoutPage

def test_full_checkout_flow(driver):
    driver.get('https://www.saucedemo.com/')
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    checkout = CheckoutPage(driver)
    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    checkout.click_checkout()
    checkout.fill_information('Kevin', 'QA', '12345')
    checkout.finish_order()
    assert checkout.get_success_message() == 'Thank you for your order!'
