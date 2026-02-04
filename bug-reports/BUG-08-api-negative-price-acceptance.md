# BUG-08 — API accepts negative values in price field

## Summary
The API endpoint for product creation accepts negative integers in the "price" field without validation. This is a critical business logic flaw that could lead to financial loss.

## Environment
- Endpoint: https://jsonplaceholder.typicode.com/posts
- Tool: Postman
- Date: 2026-02-03

## Steps to Reproduce
1. Open Postman.
2. Set method to **POST**.
3. URL: https://jsonplaceholder.typicode.com/posts
4. Body (raw JSON): {"title": "Test", "price": -500}
5. Click Send.

## Actual Result
Status Code **201 Created**. The resource is created with a negative price.

## Expected Result
Status Code **400 Bad Request**. The API should validate the input and reject negative values for financial fields.

## Severity
Critical (Business Logic)

## Priority
High (P1)

## Evidence
- [View API Evidence](../evidence/API-BUG-01.png)
