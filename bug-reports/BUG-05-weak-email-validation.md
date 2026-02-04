# BUG-05 — Registration accepts unrealistic email format (weak email validation)

## Summary
The system allows registering accounts using minimal/unrealistic email formats (e.g., `2@a.c`).
Even if technically valid, it increases spam/fake account risk and harms communications reliability.

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
3. Fill required fields with valid values
4. Enter email: `2@a.c`
5. Submit the form (**Continue**)

## Actual Result
Account is created successfully.

## Expected Result
The system should enforce stronger validation and/or email verification (confirmation step).

## Severity
Medium (Data quality / abuse risk)

## Priority
P2

## Evidence
- [View Evidence Image](../evidence/BUG-05.png)
