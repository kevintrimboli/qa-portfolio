import time
from pages.login_page import LoginPage
from pages_advanced.inventory_advanced_page import InventoryAdvancedPage
from pages_advanced.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complex_cart_management(driver):
    login = LoginPage(driver)
    inventory = InventoryAdvancedPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    driver.get('https://www.saucedemo.com/')
    
    # Flujo: Login -> Agregar 3 -> Borrar 1 -> Checkout
    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()

    # Agregamos 3 productos
    inventory.add_first_n_items(3)
    time.sleep(2) # Pausa para tu video
    assert inventory.get_cart_count() == '3'

    # Borramos uno desde el carrito
    inventory.go_to_cart()
    time.sleep(2)
    cart.remove_item_by_index(0) # Borra el primero de la lista
    
    # Validamos que queden 2
    assert inventory.get_cart_count() == '2'
    time.sleep(2)

    # Terminamos la compra
    cart.click_checkout()
    checkout.fill_information('Kevin', 'Advanced', '99999')
    checkout.finish_order()
    
    assert checkout.get_success_message() == 'Thank you for your order!'
    time.sleep(2)
