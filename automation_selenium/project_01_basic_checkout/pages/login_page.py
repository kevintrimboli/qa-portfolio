from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # 1. Definimos los "Planos" de la página (Locators)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 2. Definimos las "Acciones" que un humano puede hacer
    def enter_username(self, user):
        self.driver.find_element(*self.username_field).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password_field).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()