# Test Cases – Project 01 Checkout

## TC-01 – Checkout blocks invalid input values

### Preconditions
- User is logged in
- At least one product added to the cart

### Steps
1. Navigate to Checkout > Your Information
2. Enter invalid values in the fields:
   - First Name: /root
   - Last Name: /admin
   - Postal Code: /.;/./,.231
3. Click Continue

### Expected Result
The system should validate input values and prevent submission.

### Actual Result
FAIL – Invalid input values are accepted.

### Linked Bug
- SCRUM-5
