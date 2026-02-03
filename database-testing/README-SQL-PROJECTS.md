# SQL QA Manual Projects

## Project 01: Inventory Validation
- **Scenario:** Filter products with Price > 50 to verify premium catalog.
- **Query:** SELECT ProductName, Price, Unit FROM Products WHERE Price > 50;
- **Evidence:** [evidence/SQL-PROJECT-01.png](../evidence/SQL-PROJECT-01.png)

## Project 02: User Data Integrity
- **Scenario:** Validate customer segmentation by Country (Mexico).
- **Query:** SELECT CustomerName, ContactName, City, Country FROM Customers WHERE Country = 'Mexico';
- **Evidence:** [evidence/SQL-PROJECT-02.png](../evidence/SQL-PROJECT-02.png)

## Project 03: Order Business Logic
- **Scenario:** Verify chronological order of transactions.
- **Query:** SELECT OrderID, CustomerID, OrderDate FROM Orders ORDER BY OrderDate DESC;
- **Evidence:** [evidence/SQL-PROJECT-03.png](../evidence/SQL-PROJECT-03.png)

## 🐞 Project 04: SQL Bug Discovery (Data Integrity)
- **Scenario:** Identification of "Orphan Products" (Products without a valid Category).
- **Bug Found:** Found products that exist in the database but are hidden from the UI because their CategoryID is null or invalid.
- **Query:** ```sql
  SELECT ProductName, CategoryID FROM Products 
  WHERE CategoryID IS NULL;
  ```
- **Evidence:** [evidence/SQL-BUG-REPORT.png](../evidence/SQL-BUG-REPORT.png)
- **Severity:** High (Impacts sales as products are not reachable by customers).
