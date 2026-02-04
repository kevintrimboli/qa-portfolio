from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CSS_SELECTOR, '.title')
        self.add_backpack_btn = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_backpack_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_backpack_btn)
        ).click()
        
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
