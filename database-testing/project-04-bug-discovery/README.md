# Project 04: SQL Bug Discovery
**Goal:** Detect data inconsistencies that are hidden from the User Interface.

## 🐞 Bug Report: Orphan Products (Data Integrity Issue)
- **Description:** Products found in the 'Products' table with a CategoryID that does not exist in the 'Categories' table. This causes these products to be invisible on the website.
- **Impact:** High. Loss of sales for the affected products.
- **SQL Query to Detect:** ```sql
SELECT ProductName, CategoryID 
FROM Products 
WHERE CategoryID NOT IN (SELECT CategoryID FROM Categories);
```
- **Evidence:** [evidence/SQL-BUG-REPORT.png](../../evidence/SQL-BUG-REPORT.png)
