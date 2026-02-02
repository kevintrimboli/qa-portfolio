# Test Cases — OpenCart Demo (Manual)

Application under test:
- https://demo.opencart.com/

Environment (example):
- OS: macOS
- Browser: Chrome

---

## TC-01 — Register with valid data (Account created)

**Preconditions**
- User is on the Register Account page

**Steps**
1. Open https://demo.opencart.com/
2. Go to **My Account** → **Register**
3. Fill all required fields with valid data
4. Accept privacy policy (if required)
5. Click **Continue**

**Expected Result**
- Account is created
- User is redirected to a success/confirmation page

---

## TC-02 — Register with existing email (Error shown)

**Preconditions**
- An account already exists with the email address used

**Steps**
1. Go to Register Account page
2. Fill the form using an existing email
3. Click **Continue**

**Expected Result**
- A clear validation error is shown (email already registered)
- Account is not created

---

## TC-03 — Login with valid credentials (User logged in)

**Preconditions**
- User has an existing account

**Steps**
1. Go to **My Account** → **Login**
2. Enter valid email + password
3. Click **Login**

**Expected Result**
- User is logged in
- Account dashboard is displayed

---

## TC-04 — Login with wrong password (Error shown)

**Preconditions**
- User has an existing account

**Steps**
1. Go to Login
2. Enter valid email + invalid password
3. Click **Login**

**Expected Result**
- Error message displayed
- User remains logged out

---

## TC-05 — Logout (Session ends)

**Preconditions**
- User is logged in

**Steps**
1. Click **Logout**

**Expected Result**
- Session ends
- User is redirected to logout confirmation page
- Protected pages require login again

---

## TC-06 — Search existing product (Results shown)

**Preconditions**
- None

**Steps**
1. Use the search bar
2. Search for a known product name (e.g., "iPhone")

**Expected Result**
- Matching products are displayed in results

---

## TC-07 — Search non-existing product (No results message)

**Preconditions**
- None

**Steps**
1. Search for a random string (e.g., "zzzz-test-123")

**Expected Result**
- "No results" / "No products found" message is shown

---

## TC-08 — Add product to cart (Cart count increases)

**Preconditions**
- None

**Steps**
1. Open any product page
2. Click **Add to Cart**

**Expected Result**
- Product added successfully
- Cart count/indicator increases

---

## TC-09 — Update quantity in cart (Total updates)

**Preconditions**
- At least one item is in the cart

**Steps**
1. Open Shopping Cart
2. Change quantity
3. Click **Update** (if present)

**Expected Result**
- Quantity updates
- Total price updates accordingly

---

## TC-10 — Remove item from cart (Empty state)

**Preconditions**
- At least one item is in the cart

**Steps**
1. Open Shopping Cart
2. Remove the item

**Expected Result**
- Cart becomes empty
- Empty cart message is shown

---

## TC-11 — Navigate category (Product list shown)

**Preconditions**
- None

**Steps**
1. Click a top navigation category (e.g., Desktops / Components)

**Expected Result**
- Category product list page is displayed

---

## TC-12 — Open checkout (Checkout page opens if allowed)

**Preconditions**
- At least one item in cart

**Steps**
1. Open Shopping Cart
2. Click **Checkout**

**Expected Result**
- Checkout page opens (or a clear message is shown if checkout is restricted in demo)
