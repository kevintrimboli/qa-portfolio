# BUG-04 — User blocked (Error 1015) after fast product browsing

## Summary
Normal browsing behavior (opening products quickly) triggers Cloudflare rate limiting (Error 1015).
This blocks legitimate users and can reduce conversions.

## Environment
- Website: https://demo.opencart.com/
- Browser: Chrome
- OS: macOS
- Area: Product browsing
- Error: Cloudflare **1015** (Rate Limited)

## Preconditions
- User can access the store normally

## Steps to Reproduce
1. Open https://demo.opencart.com/
2. Open a product page
3. Immediately open another product
4. Repeat quickly (2–3 times)
5. Continue browsing

## Actual Result
User is blocked with Cloudflare Error 1015.

## Expected Result
Users should be able to browse products normally.
If anti-bot protection is needed, apply progressive protections (throttling / captcha) instead of blocking real users.

## Severity
High (Blocks site usage)

## Priority
P1

## Evidence
- /evidence/BUG-04.png
