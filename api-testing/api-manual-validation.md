# API Testing — Manual Validation (Postman)

## 🎯 Project Overview
This project documents the manual validation of a REST API using **Postman**. The goal was to verify the backend's behavior through different HTTP methods and perform **Negative Testing** to identify logic flaws.

---

## 🧪 Executed Test Cases

### 1. [POST] Create Resource
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Goal:** Verify if the server correctly processes and persists new entries.
- **Payload:** JSON containing title, body, and userId.
- **Result:** **201 Created**. Assigned ID: 101.
- **Evidence:** `../evidence/API-POST-01.png`

### 2. [GET] Read Resource
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Goal:** Validate that specific data can be retrieved from the server.
- **Result:** **200 OK**. Correct data structure returned.
- **Evidence:** `../evidence/API-GET-01.png`

### 3. [PUT] Update Resource
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Goal:** Ensure existing data can be modified correctly.
- **Result:** **200 OK**. Fields updated as requested.
- **Evidence:** `../evidence/API-PUT-01.png`

### 4. [DELETE] Remove Resource
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Goal:** Verify the deletion flow and server response.
- **Result:** **200 OK**.
- **Evidence:** `../evidence/API-DELETE-01.png`

---

## 🐞 Negative Testing (Bug Discovery)

### [BUG-08] Acceptance of Negative Price
- **Scenario:** Validating input for a financial field.
- **Test:** Sending a POST request with a negative value in the "price" field.
- **Actual Result:** **201 Created**. The API accepts negative prices.
- **Expected Result:** **400 Bad Request**. The API should validate that prices are positive values.
- **Evidence:** `../evidence/API-BUG-01.png`
- **Detailed Report:** `../bug-reports/BUG-08-api-negative-price-acceptance.md`
