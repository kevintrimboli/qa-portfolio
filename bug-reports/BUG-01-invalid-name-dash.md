# BUG-01 — Registration accepts invalid name character "-" (data validation)

## Summary
The application allows creating an account where **First Name** and **Last Name** are set to `-`.
This can pollute user data and impact invoices, reporting, and customer records.

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
3. Enter `-` in **First Name**
4. Enter `-` in **Last Name**
5. Fill other required fields with valid values
6. Submit the form (**Continue**)

## Actual Result
Account is created successfully with `-` as name values.

## Expected Result
The system should reject invalid name characters and show a clear validation message.

## Severity
Medium (Data integrity issue)

## Priority
P2

## Evidence
- /evidence/BUG-01.png
