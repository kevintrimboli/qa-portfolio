# BUG-06 — Out of Stock Product Can Be Added to Cart

## Summary
Products marked as out of stock can still be added to the shopping cart and proceed to checkout.

## Environment
- Website: https://demo.opencart.com
- Browser: Chrome
- OS: macOS
- Date: 2026-02-01

## Precondition
User is browsing the store without being logged in.

## Steps to Reproduce
1. Open the store homepage
2. Select a product marked as "*** Out of Stock"
3. Click "Add to Cart"
4. Go to Shopping Cart
5. Proceed to Checkout

## Expected Result
System should block adding out-of-stock products and show an error message.

## Actual Result
Product is added successfully and checkout is allowed.

## Severity
Major (affects purchasing flow)

## Priority
High (business impact)

## Evidence
See: /evidence/BUG-06.png

## Notes
This may cause customer frustration and incorrect orders.