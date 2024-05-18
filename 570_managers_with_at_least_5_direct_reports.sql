-- PostgreSQL

SELECT e1.name
FROM Employee e1
JOIN (
    SELECT e2.managerId, COUNT(*) AS num
    FROM Employee e2
    GROUP BY e2.managerId
) rep_count ON e1.id = rep_count.managerId
WHERE rep_count.num >= 5;