# 📑 Test Plan: OpenCart E-Commerce Demo

## 1. Introduction
This plan defines the strategy for validating the core functionalities of the OpenCart platform, focusing on end-user experience and data integrity.

## 2. Scope
- **Modules:** Account Registration, Authentication, Catalog, Cart, and Checkout.
- **Testing Types:** Smoke Testing, Regression Testing, and Negative Testing.

## 3. Test Strategy
A combination of **Scripted Testing** (based on TC-01 to TC-12) and **Exploratory Testing** will be used to detect unexpected behaviors in form validations.

## 4. Risk Management
| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| Unstable Demo Environment | High | Periodically clear cookies/cache and restart session. |
| UI Changes in Demo Site | Medium | Keep locators and test steps updated. |

## 5. Exit Criteria
- 100% of Smoke Tests passed.
- No "Critical" or "High" severity Bugs remain open.
- Traceability matrix completed.
