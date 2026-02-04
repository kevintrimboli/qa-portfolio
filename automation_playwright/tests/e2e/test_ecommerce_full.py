import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_complete_purchase_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.load()
    login.login("standard_user", "secret_sauce")

    # Verificamos que entramos
    expect(inventory.header_title).to_have_text("Products")

    # Añadimos producto y verificamos carrito
    inventory.add_first_available_item()
    expect(inventory.shopping_cart_badge).to_have_text("1")