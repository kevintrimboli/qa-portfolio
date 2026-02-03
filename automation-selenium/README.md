# 🚀 Selenium E2E Automation - SauceDemo

## 🇺🇸 Project Overview (English)
This project automates the complete purchase flow of a professional e-commerce sandbox (**SauceDemo**). It covers the entire lifecycle from login to order confirmation.

### Key Features:
* **Architecture:** Page Object Model (POM) for high maintainability.
* **Pattern:** Decoupled locators and actions for cleaner test scripts.
* **Stability:** Implemented **Explicit Waits** (WebDriverWait) to handle asynchronous elements.
* **Configuration:** Custom Chrome options for Incognito mode and alert handling.

> **Note:** For demonstration/recording purposes, 2-second pauses were added to the video. However, the production code uses smart waits for maximum speed (as seen in the 4.44s execution).

---

## 🇪🇸 Resumen del Proyecto (Español)
Este proyecto automatiza el flujo completo de compra en la plataforma **SauceDemo**, cubriendo desde el inicio de sesión hasta la confirmación del pedido.

### Características Principales:
* **Arquitectura:** Page Object Model (POM) para facilitar el mantenimiento.
* **Patrón:** Localizadores y acciones desacoplados para scripts de prueba más limpios.
* **Estabilidad:** Implementación de **Esperas Explícitas** (WebDriverWait) para manejar elementos asíncronos.
* **Configuración:** Opciones de Chrome personalizadas para modo incógnito y gestión de alertas.

---

### 🛠️ Tech Stack
* **Language:** Python 3.14+
* **Tool:** Selenium WebDriver
* **Test Runner:** Pytest
* **Pattern:** Page Object Model (POM)

### 🚀 Execution
1. Activate environment: `source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run test: `pytest automation-selenium/tests/test_checkout.py`
