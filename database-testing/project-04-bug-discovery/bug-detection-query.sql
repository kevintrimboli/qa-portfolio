-- SQL Bug Discovery: Detect Orphan Products
-- Scenario: Find products linked to a CategoryID that no longer exists in the Categories table.
-- This represents a Critical Data Integrity failure.

SELECT p.ProductName, p.CategoryID
FROM Products p
WHERE p.CategoryID NOT IN (SELECT CategoryID FROM Categories)
OR p.CategoryID IS NULL;
