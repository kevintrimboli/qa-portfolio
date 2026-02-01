# Rate Limiting and Bot Detection Issues Report

## Summary

During normal user navigation, the system triggers Error 1015
("You are being rate limited") when multiple actions are performed quickly.

This behavior affects legitimate users and creates a poor user experience.

---

## Environment

- Platform: OpenCart Demo Store
- URL: https://demo.opencart.com/
- Browser: Chrome / Safari (MacOS)
- Network: Mobile / Home WiFi
- Date: February 2026

---

## Issue: Legitimate Users Detected as Bots

### Description

When browsing products or performing actions quickly, the system blocks the user
and displays Error 1015, assuming automated behavior.

This happens even during normal manual usage.

---

### Steps to Reproduce

1. Open the homepage
2. Click on a product
3. Go back
4. Click another product
5. Repeat quickly (2–3 times)
6. Or open multiple tabs and browse products

---

### Expected Result

The system should:
- Allow normal browsing behavior
- Detect only real automated traffic
- Apply rate limits gradually
- Warn users before blocking

---

### Actual Result

The system blocks the user and displays:

"Error 1015 - You are being rate limited"

User access is temporarily restricted.

---

## Impact

- Legitimate users are blocked
- Browsing experience is interrupted
- Users may abandon the website
- Loss of potential sales
- Increased support complaints

---

## Severity

High

Reason:
Blocks access to the platform and prevents normal usage.

---

## Priority

High

Reason:
Directly affects user experience and business metrics.

---

## Security and UX Risk

Over-aggressive bot detection creates:

- False positives
- Poor customer trust
- Reduced conversion rates
- Negative reputation

While bot protection is necessary, incorrect configuration harms real users.

---

## Recommendations

1. Review rate limiting thresholds
2. Implement progressive throttling instead of hard blocks
3. Differentiate human vs automated behavior
4. Use CAPTCHA only when necessary
5. Add monitoring for false positives
6. Whitelist trusted user sessions

---

## Additional Notes

The issue is more frequent on slower networks,
where multiple requests are sent in short intervals.

This increases the probability of false detection.

---

## Conclusion

Current bot detection settings are too strict.
They protect the platform but negatively impact user experience.

Balancing security and usability is required to avoid blocking real customers.