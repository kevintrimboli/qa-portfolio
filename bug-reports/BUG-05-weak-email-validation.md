# Bug Report

Title:
System allows weak email format "2@a.c" during registration

Environment:
macOS, Chrome, OpenCart Demo

Precondition:
User is on Register Account page

Steps to Reproduce:
1. Open https://demo.opencart.com
2. Click "My Account"
3. Click "Register"
4. Enter valid name and password
5. Enter email: 2@a.c
6. Submit form

Expected Result:
System should reject weak or unrealistic email format

Actual Result:
Account is created successfully with email "2@a.c"

Severity:
Medium

Priority:
P2

Attachments:
BUG-05-weak-email.png

Notes:
Weak email validation may allow fake accounts and spam