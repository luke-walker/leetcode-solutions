SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) AS count
    FROM Orders
    GROUP BY customer_number
)
WHERE count = (
    SELECT MAX(count)
    FROM (
        SELECT COUNT(*) AS count
        FROM Orders
        GROUP BY customer_number
    )
)
