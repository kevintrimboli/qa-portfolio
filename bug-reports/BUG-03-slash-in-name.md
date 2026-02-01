# Bug Report

Title:
System allows special character "/" in First Name and Last Name

Environment:
macOS, Chrome, OpenCart Demo

Precondition:
User is on Register Account page

Steps to Reproduce:
1. Open https://demo.opencart.com
2. Click "My Account"
3. Click "Register"
4. Enter "/" in First Name
5. Enter "/" in Last Name
6. Enter valid email and password
7. Click "Continue"

Expected Result:
System should reject special characters in name fields

Actual Result:
Account is created successfully with "/" as name

Severity:
High

Priority:
P1

Attachments:
BUG-03-slash-name.png

Notes:
Special characters may break backend processing and reports