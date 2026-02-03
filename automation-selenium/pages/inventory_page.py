from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Localizador del título de la página para confirmar que entramos
        self.title = (By.CSS_SELECTOR, ".title")

    def get_title_text(self):
        return self.driver.find_element(*self.title).text