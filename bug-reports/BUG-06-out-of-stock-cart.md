# BUG-06 — Out-of-stock product can be added to cart and proceed to checkout

## Summary
Products marked as **Out of Stock** can still be added to cart and proceed to checkout.
This can cause failed orders, refunds, and customer dissatisfaction.

## Environment
- Website: https://demo.opencart.com/
- Browser: Chrome
- OS: macOS
- Area: Cart / Checkout

## Preconditions
- User can browse products

## Steps to Reproduce
1. Open the store homepage
2. Select a product marked as **Out of Stock**
3. Click **Add to Cart**
4. Go to **Shopping Cart**
5. Proceed to **Checkout**

## Actual Result
Out-of-stock product is added and checkout is allowed.

## Expected Result
System should block adding out-of-stock items and show a clear error message.

## Severity
Major (Business impact / purchasing flow)

## Priority
High

## Evidence
- /evidence/BUG-06.png
