from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(driver):
    # 1. Abrir la página
    driver.get("https://www.saucedemo.com/")
    
    # 2. Inicializar las páginas
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    
    # 3. Ejecutar acciones
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    
    # 4. Verificación (Assert) - El momento de la verdad
    # Si el texto es 'Products', el QA aprueba el test
    assert inventory.get_title_text() == "Products"