# BUG-07 — User blocked (Error 1015) when refreshing pages repeatedly

## Summary
Refreshing a page multiple times in a short period triggers Cloudflare rate limiting (Error 1015),
blocking legitimate users.

## Environment
- Website: https://demo.opencart.com/
- Browser: Chrome
- OS: macOS
- Area: General navigation
- Error: Cloudflare **1015** (Rate Limited)
- Date observed: 2026-02-01

## Preconditions
- User is browsing the store normally

## Steps to Reproduce
1. Open any product or page
2. Refresh the page repeatedly (5–10 times)
3. Continue refreshing within a short time

## Actual Result
User is blocked with Cloudflare Error 1015.

## Expected Result
User should be able to refresh without being blocked.
If protection is needed, show progressive warnings or captcha instead of hard blocking.

## Severity
Major (Blocks usage)

## Priority
High

## Evidence
- /evidence/BUG-07.png
