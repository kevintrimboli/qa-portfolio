# Bug Report

Title:
User blocked after only two registration attempts (Error 1015)

Environment:
macOS, Chrome, OpenCart Demo

Precondition:
User registers and logs out normally

Steps to Reproduce:
1. Open https://demo.opencart.com
2. Register a new account
3. Logout
4. Register a second account
5. Try to access Register page again

Expected Result:
User should be able to continue using the site normally

Actual Result:
User is blocked with Cloudflare Error 1015 (rate limited)

Severity:
High

Priority:
P1

Attachments:
BUG-02-rate-limit.png

Notes:
Rate limit is triggered too early and blocks legitimate users