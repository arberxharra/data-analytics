/*
a) The Products table contains the items Northwind sells.

b) The Categories table contains the different types or categories of items Northwind sells.
*/

USE northwind;

SELECT * FROM employees;
-- The employee whose name sounds like a bird is Margaret Peacock.

SELECT * FROM products;
-- The products table returned 77 records. I can use the toolbar's row limit dropdown to display only 10 rows.
-- BONUS: I can limit the results by writing SELECT * FROM products LIMIT 10;
-- Source: MySQL Reference Manual (LIMIT Clause).

SELECT * FROM categories;
-- The category ID for Seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;