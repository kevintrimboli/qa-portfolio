# Bugs — Project 03 (RealWorld Authentication)

## P03-BUG-02 — Sign in button gets stuck with valid credentials (Incognito)

- Jira ID: SCRUM-9
- Jira Link: https://trimboliit.atlassian.net/browse/SCRUM-9
- Severity: Critical
- Priority: High
- Status: To Do
- Evidence: ../../../evidence/P03-BUG-02-signin-stuck-valid-credentials-incognito.mp4

### Environment
- Browser: Chrome
- Mode: Incognito
- OS: macOS
- Sign in URL: https://react-redux.realworld.io/#/login
### Preconditions
- User has an existing account (registered successfully)

### Steps to Reproduce
1. Open the application in Incognito mode
2. Navigate to the Sign in page
3. Enter valid user credentials
4. Click the "Sign in" button

### Actual Result
The "Sign in" button remains stuck in a loading state.
The user is not authenticated and no feedback is displayed.

### Expected Result
The user should be authenticated and redirected to the Home page,
or a clear error message should be displayed if authentication fails.
