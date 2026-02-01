# BUG-07 — User Blocked by Rate Limiting When Refreshing Page

## Summary
User gets blocked (Error 1015) when refreshing the page multiple times in a short period.

## Environment
- Website: https://demo.opencart.com
- Browser: Chrome
- OS: macOS
- Date: 2026-02-01

## Precondition
User is browsing the store normally.

## Steps to Reproduce
1. Open any product or page
2. Refresh the page repeatedly (5–10 times)
3. Continue refreshing within a short time

## Expected Result
User should be able to refresh pages without being blocked.

If protection is needed, show a warning message.

## Actual Result
User is blocked and receives Cloudflare Error 1015 (Rate Limited).

Access is temporarily denied.

## Severity
Major  
(User is unable to use the website)

## Priority
High  
(Affects usability and user experience)

## Evidence
See: /evidence/BUG-07.png

## Notes
Normal user behavior is detected as bot activity.
This may block legitimate customers.