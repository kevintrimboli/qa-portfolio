# 📝 Bug Reports Index

Este directorio centraliza los hallazgos de pruebas manuales, de API y de seguridad.

## 🐞 Bugs de UI & UX (OpenCart)
- [**BUG-01**](./BUG-01-invalid-name-dash.md) — Registration accepts "-"
- [**BUG-02**](./BUG-02-rate-limit-register.md) — Cloudflare Block (Error 1015) on Register
- [**BUG-03**](./BUG-03-slash-in-name.md) — Registration accepts "/" in names
- [**BUG-04**](./BUG-04-rate-limit-browsing.md) — Cloudflare Block on Product Browsing
- [**BUG-05**](./BUG-05-weak-email-validation.md) — Weak email validation (2@a.c)
- [**BUG-06**](./BUG-06-out-of-stock-cart.md) — Out-of-stock checkout allowed
- [**BUG-07**](./BUG-07-rate-limit-refresh.md) — Cloudflare Block on repeated Refresh

## 🔑 Bugs de Seguridad & Lógica (Nuevos)
- **BUG-09** — Registration accepts weak passwords (123) → [View Evidence](../evidence/P02-BUG-01-register-accepts-weak-password.png)
- **BUG-10** — Sign-in stuck on valid credentials (Incognito) → [View Video Evidence](../evidence/P03-BUG-02-signin-stuck-valid-credentials-incognito.mp4)

## ⚙️ Bugs de API & DB
- [**BUG-08**](./BUG-08-api-negative-price-acceptance.md) — API accepts negative prices (Business Logic)
- [**SQL-BUG**](../database-testing/README-SQL-PROJECTS.md) — Orphan Products (Referential Integrity)

---
*Evidencias adicionales de pruebas de API (GET/POST/PUT/DELETE) disponibles en [/evidence](../evidence).*
