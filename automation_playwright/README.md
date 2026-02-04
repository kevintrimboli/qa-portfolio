# 🎭 Playwright E2E Automation Framework

This repository contains the end-to-end automation suite using **Playwright** and **Pytest**.

## 🏗️ Architecture: Page Object Model (POM)
The project is structured to ensure maintainability and scalability:
- **/pages**: Contains page classes with locators and actions.
- **/tests**: Test scripts organized by feature (e.g., e2e).
- **/data**: JSON files for data-driven testing.

## 🚦 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run all tests: `pytest`
3. Generate report: `pytest --html=report.html`
