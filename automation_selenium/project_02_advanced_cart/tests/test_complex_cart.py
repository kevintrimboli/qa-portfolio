import time
from automation_selenium.project_01_basic_checkout.pages.login_page import LoginPage
from automation_selenium.project_02_advanced_cart.pages.inventory_advanced_page import InventoryAdvancedPage
from automation_selenium.project_02_advanced_cart.pages.cart_page import CartPage
from automation_selenium.project_01_basic_checkout.pages.checkout_page import CheckoutPage

def test_complex_cart_management(driver):
    login = LoginPage(driver)
    inventory = InventoryAdvancedPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    driver.get('https://www.saucedemo.com/')
    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()
    inventory.add_first_n_items(3)
    inventory.go_to_cart()
    cart.remove_item_by_index(0)
    assert inventory.get_cart_count() == '2'
    cart.click_checkout()
    checkout.fill_information('Kevin', 'Advanced', '99999')
    checkout.finish_order()
    assert checkout.get_success_message() == 'Thank you for your order!'
