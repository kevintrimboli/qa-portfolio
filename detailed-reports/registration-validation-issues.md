# Registration Validation Issues Report

## Summary

During testing of the registration process, multiple input validation issues were found.
The system allows the creation of user accounts using invalid characters and unrealistic email formats.

This can lead to:
- Fake accounts
- Security risks
- Database pollution
- Potential abuse (spam / bots)

---

## Environment

- Platform: OpenCart Demo Store
- URL: https://demo.opencart.com/
- Browser: Chrome / Safari (MacOS) / Windows / Ubuntu
- Date: February 2026

---

## Issue 1: Registration Allowed With Invalid Name Characters

### Description

The system allows users to register using special characters such as:
- "-"
- "/"

in the First Name and Last Name fields.

These characters should normally be restricted or validated.

### Steps to Reproduce

1. Open the registration page
2. Fill the form
3. Enter "-" or "/" in First Name
4. Enter "-" or "/" in Last Name
5. Complete registration

### Expected Result

The system should:
- Reject invalid characters
- Display a validation message
- Ask the user to correct the input

### Actual Result

The account is created successfully with invalid characters.

### Impact

- Poor data quality
- Possible injection or security risks
- Problems in reporting and analytics
- Potential compliance issues

### Severity

Medium

Reason:
Does not crash the system, but affects data integrity and security.

### Priority

High

Reason:
This affects all new registrations and can be easily abused.

---

## Issue 2: Weak Email Validation (Random / Invalid Emails Accepted)

### Description

The system accepts unrealistic or weak email formats such as:

- 2@a.c
- random@x.z
- test@test.t

These emails are technically valid but unusable in real scenarios.

### Steps to Reproduce

1. Open registration page
2. Enter a minimal/random email
3. Complete registration

### Expected Result

The system should:
- Enforce stronger email validation
- Require realistic domain formats
- Optionally verify email ownership

### Actual Result

The account is created without any verification.

### Impact

- Fake accounts creation
- Impossible user communication
- Spam risk
- Marketing and analytics distortion

### Severity

Medium

Reason:
Affects platform reliability and user management.

### Priority

Medium

Reason:
Important, but less urgent than system-breaking bugs.

---

## Overall Risk Assessment

If these issues remain unresolved:

- Platform credibility decreases
- Spam and bot activity increases
- Database quality deteriorates
- Customer trust is affected

These problems may grow over time if not addressed early.

---

## Recommendations

1. Implement input validation for name fields
2. Restrict special characters
3. Improve email format validation
4. Add email verification (confirmation link)
5. Add automated validation tests

---

## Conclusion

Although these issues do not cause system crashes, they represent long-term risks.
Fixing them early will improve security, data quality, and platform reliability.