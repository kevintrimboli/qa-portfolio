import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Configuramos opciones para que Chrome no moleste
    chrome_options = Options()
    chrome_options.add_argument('--incognito')  # Abre en incógnito
    chrome_options.add_argument('--disable-save-password-bubble') # Desactiva el cartel de guardar pass
    chrome_options.add_argument('--disable-notifications') # Desactiva notificaciones
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    driver.quit()
