# Bug Report

Title:
System allows account creation with "-" as First Name and Last Name

Environment:
macOS, Chrome, OpenCart Demo

Precondition:
User is on Register Account page

Steps to Reproduce:
1. Open https://demo.opencart.com
2. Click "My Account"
3. Click "Register"
4. Enter "-" in First Name
5. Enter "-" in Last Name
6. Enter valid email and password
7. Click "Continue"

Expected Result:
System should reject invalid names and show validation error

Actual Result:
Account is created successfully with "-" as name

Severity:
Medium

Priority:
P2

Attachments:
BUG-01-invalid-name.png

Notes:
Invalid user data may affect invoices, orders, and reports