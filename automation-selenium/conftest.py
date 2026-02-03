import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    # Setup: Se ejecuta ANTES de cada test
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) # Espera hasta 10 seg si un elemento no aparece
    driver.maximize_window()
    
    yield driver # Aquí es donde el test "pasa"
    
    # Teardown: Se ejecuta DESPUÉS de cada test
    driver.quit()