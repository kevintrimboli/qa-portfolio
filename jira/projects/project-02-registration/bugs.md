# Bugs — Project 02 (Registration)

## P02-BUG-01 — Registration allows weak passwords without validation

- Jira ID: SCRUM-8
- Jira Link: https://trimboliit.atlassian.net/browse/SCRUM-8
- Priority: High
- Severity: Major
- Status: To Do
- Evidence: ../../../evidence/P02-BUG-01-register-accepts-weak-password.png

### Environment
- Browser: Chrome
- OS: macOS
- URL: https://practice.expandtesting.com/register

### Preconditions
- User is on the registration page

### Steps to Reproduce
1. Enter a valid username
2. Enter `1234` as password
3. Enter `1234` as confirm password
4. Submit the registration form

### Actual Result
The system allows registration using a weak password without any validation or warning.

### Expected Result
The system should enforce password strength rules
or display validation messages indicating password requirements.
