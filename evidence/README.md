# Evidence Repository

This folder contains screenshots and videos used as proof for reported bugs and executed test cases.
Each file is referenced from the corresponding bug report and Jira project documentation.

## Naming convention
- `BUG-XX.png` → OpenCart standalone bug-reports
- `PXX-BUG-YY-description.(png|mp4)` → Project-based Jira portfolio
- `API-XXX-01.png` → API testing validation (Postman)
- `SEL-PROJ-XX-description.mp4` → Selenium Automated Test Execution

## Evidence index

### 🤖 Automated Testing — Selenium & Python (E2E)
- **SEL-PROJ-01-basic-checkout.mp4** → Standard E2E flow (Login to Checkout).
- **SEL-PROJ-02-advanced-cart-logic.mp4** → Advanced logic: Dynamic item addition, removal, and badge validation.

### OpenCart bug-reports (screenshots)
- BUG-01.png
- BUG-02.png
- BUG-03.png
- BUG-04.png
- BUG-05.png
- BUG-06.png
- BUG-07.png

### Project 01 — Checkout Input Validation (SauceDemo)
- P01-BUG-01-checkout-invalid-input-validation.mp4 (Jira: SCRUM-5)

### Project 02 — Registration Weak Password (ExpandTesting)
- P02-BUG-01-register-accepts-weak-password.png (Jira: SCRUM-8)

### Project 03 — Sign In Stuck (RealWorld Conduit)
- P03-BUG-02-signin-stuck-valid-credentials-incognito.mp4 (Jira: SCRUM-9)

### API Testing & Validation (Postman)
- API-POST-01.png → Successful resource creation (201 Created).
- API-GET-01.png → Data retrieval validation (200 OK).
- API-PUT-01.png → Resource update validation (200 OK).
- API-DELETE-01.png → Resource deletion validation (200 OK).
- API-BUG-01.png → Evidence of negative price acceptance bug (Critical).
