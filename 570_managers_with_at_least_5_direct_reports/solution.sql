SELECT
    b.name
FROM Employee AS a
JOIN Employee AS b
    ON a.managerId = b.id
GROUP BY b.id, b.name
HAVING COUNT(*) >= 5;