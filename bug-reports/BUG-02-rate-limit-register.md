# BUG-02 — User blocked after only two registration attempts (Error 1015)

## Summary
After normal registration behavior (register → logout → register), the user is blocked by Cloudflare rate limiting.
This prevents legitimate users from continuing.

## Environment
- Website: https://demo.opencart.com/
- Browser: Chrome
- OS: macOS
- Area: Registration flow
- Error: Cloudflare **1015** (Rate Limited)

## Preconditions
- User can access Register page initially

## Steps to Reproduce
1. Open https://demo.opencart.com/
2. Register a new account (valid data)
3. Logout
4. Register a second new account
5. Try to access Register page again

## Actual Result
User is blocked with Cloudflare Error 1015 (rate limited).

## Expected Result
Normal users should not be blocked after standard behavior.
If protection is needed, it should be gradual (warning / captcha) rather than a hard block.

## Severity
High (Blocks user flow)

## Priority
P1

## Evidence
- /evidence/BUG-02.png
