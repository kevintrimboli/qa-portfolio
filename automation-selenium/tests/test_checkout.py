import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_full_checkout_flow(driver):
    driver.get('https://www.saucedemo.com/')
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    checkout = CheckoutPage(driver)
    
    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    time.sleep(2) # <--- Pausa para que veas
    login.click_login()
    
    inventory.add_backpack_to_cart()
    time.sleep(2) # <--- Pausa
    inventory.go_to_cart()
    
    checkout.click_checkout()
    checkout.fill_information('Kevin', 'QA', '12345')
    time.sleep(2) # <--- Pausa
    checkout.finish_order()
    
    assert checkout.get_success_message() == 'Thank you for your order!'
    time.sleep(3) # <--- Pausa final antes de cerrar
