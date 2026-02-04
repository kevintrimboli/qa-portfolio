import pytest
import json
import os
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Función para cargar los datos del JSON
def load_test_data():
    path = os.path.join(os.path.dirname(__file__), "../../data/user_data.json")
    with open(path) as f:
        return json.load(f)

def test_complete_purchase_flow(page):
    # Cargamos la data
    data = load_test_data()
    user = data["standard_user"]["user"]
    password = data["standard_user"]["pass"]

    login = LoginPage(page)
    inventory = InventoryPage(page)

    # 1. Login usando data del JSON
    login.load()
    login.login(user, password)

    # 2. Validaciones (Aserciones)
    expect(inventory.header_title).to_have_text("Products")
    
    # 3. Flujo de compra
    inventory.add_first_available_item()
    expect(inventory.shopping_cart_badge).to_have_text("1")
    
    page.click(".shopping_cart_link")
    page.click("#checkout")
    
    # Rellenar con data dinámica o fija (podrías meter esto en el JSON también)
    page.fill("#first-name", "Kevin")
    page.fill("#last-name", "QA")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    
    # 4. Finalización y verificación de éxito
    page.click("#finish")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")