# BUG-03 — Registration accepts special character "/" in name fields (data validation)

## Summary
The application allows account creation with `/` in First Name and Last Name.
This can cause data quality issues and potential downstream processing problems.

## Environment
- Website: https://demo.opencart.com/
- Browser: Chrome
- OS: macOS
- Area: Register Account

## Preconditions
- User is on **Register Account** page

## Steps to Reproduce
1. Open https://demo.opencart.com/
2. Go to **My Account** → **Register**
3. Enter `/` in **First Name**
4. Enter `/` in **Last Name**
5. Fill other required fields with valid values
6. Submit the form (**Continue**)

## Actual Result
Account is created successfully with `/` as name values.

## Expected Result
The system should reject special characters in name fields and show a validation message.

## Severity
Medium (Data integrity / potential security surface)

## Priority
P2

## Evidence
- /evidence/BUG-03.png
