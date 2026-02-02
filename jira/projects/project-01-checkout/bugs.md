# Bugs – Project 01 Checkout

## P01-BUG-01 – Checkout accepts invalid characters in customer information fields

- Jira ID: SCRUM-5
- Jira Link: https://trimboliit.atlassian.net/browse/SCRUM-5
- Priority: High
- Severity: Major
- Status: To Do
- Evidence: ../../../evidence/P01-BUG-01-checkout-invalid-input-validation.mp4

### Preconditions
- User is logged in
- At least one item added to the cart

### Steps to Reproduce
1. Navigate to Checkout > Your Information
2. Enter `/root` in First Name
3. Enter `/admin` in Last Name
4. Enter `/.;/./,.231` in the Postal Code field
5. Click Continue

### Actual Result
The system accepts invalid input values and allows the user to proceed.

### Expected Result
The system should validate input fields and block invalid values,
displaying appropriate validation messages.
