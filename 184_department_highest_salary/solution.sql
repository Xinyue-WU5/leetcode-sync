SELECT
    Department,
    Employee,
    Salary
FROM (SELECT
        d.name AS Department,
        e.name AS Employee,
        salary AS Salary,
        DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS sarank
    FROM Employee AS e LEFT JOIN Department AS d ON e.departmentId = d.id) AS deem
WHERE sarank = 1;