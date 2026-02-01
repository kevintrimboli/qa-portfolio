# Inventory Management & Stock Control Issues

## Overview
Multiple cases were found where products with insufficient stock can still be added to cart and purchased.

This represents a risk for business operations and customer trust.

## Affected Area
- Product availability validation
- Shopping cart logic
- Checkout process

## Related Bugs
- BUG-06-out-of-stock-checkout.md
- BUG-02-rate-limit-register.md

## Description
The system does not properly validate stock quantity before allowing purchases.

Users can:
- Add unavailable products
- Complete checkout
- Receive confirmation

This may result in failed deliveries and refunds.

## Business Impact
- Financial losses
- Customer dissatisfaction
- Increased support workload
- Reputation damage

## Risk Level
High

## Root Cause (Suspected)
- Missing stock validation on frontend
- Backend API not enforcing quantity limits

## Recommendations
1. Validate stock before add-to-cart
2. Block checkout when stock = 0
3. Show clear error messages
4. Add automated tests for inventory

## Priority
High

## Status
Open — Pending investigation