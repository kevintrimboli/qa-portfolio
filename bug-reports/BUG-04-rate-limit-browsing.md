# Bug Report

Title:
User blocked (Error 1015) after fast product browsing

Environment:
macOS, Chrome, OpenCart Demo

Precondition:
User browsing multiple products quickly

Steps to Reproduce:
1. Open https://demo.opencart.com
2. Open a product page
3. Immediately open another product
4. Repeat navigation quickly
5. Continue browsing

Expected Result:
User should be able to browse products normally

Actual Result:
Cloudflare Error 1015 displayed (rate limited)

Severity:
High

Priority:
P1

Attachments:
BUG-04-rate-limit-browsing.png

Notes:
Normal browsing behavior is detected as bot activity