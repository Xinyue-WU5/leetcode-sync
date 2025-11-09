SELECT
    b.id
FROM Weather AS a
CROSS JOIN Weather AS b
WHERE DATEDIFF(b.recordDate,a.recordDate)=1 AND (b.recordDate>a.recordDate) AND b.temperature>a.temperature;