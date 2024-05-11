-- PostgreSQL

SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN (
    SELECT o.customerId
    FROM Orders o
    GROUP BY o.customerId
);