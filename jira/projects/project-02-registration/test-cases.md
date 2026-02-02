# Test Cases — Project 02 (Registration)

## TC-01 — Registration rejects weak passwords

### Preconditions
- User is on the registration page

### Steps
1. Navigate to Register page
2. Enter a valid username
3. Enter a weak password (e.g. `1234`)
4. Confirm the password
5. Submit the form

### Expected Result
The system should reject weak passwords
and display password strength requirements.

### Actual Result
FAIL — Weak passwords are accepted.

### Linked Bug
- SCRUM-8
