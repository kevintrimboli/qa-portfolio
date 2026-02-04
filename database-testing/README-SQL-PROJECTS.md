# 🗄️ SQL QA & Database Testing

Este módulo demuestra mi capacidad para validar la integridad de los datos, realizar pruebas de regresión en la DB y detectar errores de lógica de negocio mediante consultas complejas.

## 📊 Proyectos de Validación
1. [**Inventory Validation**](./project-01-inventory/) - Control de stock y filtrado de catálogo premium.
2. [**User Data Integrity**](./project-02-users/) - Verificación de segmentación geográfica y registros.
3. [**Order Business Logic**](./project-03-orders/) - Auditoría de transacciones cronológicas.

---

## 🐞 Caso de Éxito: Detección de Bug mediante SQL
### Bug: "Orphan Products" (Integridad de Datos)
- **Escenario:** Productos que existen en la tabla `Products` pero no tienen una categoría válida o asignada.
- **Impacto:** Estos productos son "invisibles" en el Frontend, resultando en pérdida de ingresos.
- **Consulta de Detección:**
```sql
SELECT ProductName, CategoryID 
FROM Products 
WHERE CategoryID NOT IN (SELECT CategoryID FROM Categories)
OR CategoryID IS NULL;
```
- **Evidencia:** [Ver Captura de Resultado](../evidence/SQL-BUG-REPORT.png)

---
*Herramientas utilizadas: SQL (MySQL/PostgreSQL compatible), W3Schools Test Environment.*
