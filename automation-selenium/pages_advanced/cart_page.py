from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.remove_buttons = (By.CSS_SELECTOR, '.cart_button')
        self.checkout_btn = (By.ID, 'checkout')

    def remove_item_by_index(self, index):
        btns = self.driver.find_elements(*self.remove_buttons)
        btns[index].click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
