from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.ID, 'checkout')
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_btn = (By.ID, 'continue')
        self.finish_btn = (By.ID, 'finish')
        self.complete_header = (By.CLASS_NAME, 'complete-header')

    def click_checkout(self):
        # Agregamos un pequeño scroll por si el botón está fuera de vista
        btn = self.driver.find_element(*self.checkout_btn)
        self.driver.execute_script('arguments[0].scrollIntoView();', btn)
        btn.click()

    def fill_information(self, name, lastname, zip):
        self.driver.find_element(*self.first_name).send_keys(name)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        self.driver.find_element(*self.postal_code).send_keys(zip)
        self.driver.find_element(*self.continue_btn).click()

    def finish_order(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_success_message(self):
        return self.driver.find_element(*self.complete_header).text
