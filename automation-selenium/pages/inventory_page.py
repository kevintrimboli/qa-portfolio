from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CSS_SELECTOR, '.title')
        self.add_backpack_btn = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def get_title_text(self):
        return self.driver.find_element(*self.title).text
    
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack_btn).click()
        
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
