from selenium.webdriver.common.by import By

class InventoryAdvancedPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_buttons = (By.CSS_SELECTOR, '.btn_inventory')
        self.cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.cart_link = (By.CLASS_NAME, 'shopping_cart_link')

    def add_first_n_items(self, count):
        btns = self.driver.find_elements(*self.add_buttons)
        for i in range(count):
            btns[i].click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
