class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.header_title = page.locator(".title")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    def add_first_available_item(self):
        self.page.locator(".inventory_item").first.locator("button").click()